#!/usr/bin/env bash
set -euo pipefail

# Best-effort post-process after an agent-triage run, scoped to the PR the
# agent created for the current issue (matched by "#<n>" in the PR body):
#  1. Strip the action's footer from the PR body, starting at the "Triggered by"
#     marker. Combined with auto-implement's "final response must be exactly the
#     populated template" rule, the body ends up as just the template.
#  2. Rename the head branch to issue/<n>-<slug>. GitHub is expected to retarget
#     the open PR because the new branch shares the old branch's tip commit, but
#     this is unverified against a real run.
# Cleanup failures are logged, never fatal: the PR already exists.

ISSUE_NUMBER="${1:-}"

log() { echo "[agent-triage] post-process: $*" >&2; }

strip_footer() {
    sed '/^Triggered by /,$d'
}

slugify() {
    local s
    s=$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]\{1,\}/-/g; s/^-//; s/-$//')
    if [ "${#s}" -gt 40 ]; then
        # Truncate at a word boundary: run-separators are already "-", so strip
        # back to the last one. A single >40-char token has no boundary, so it
        # is cut at 40.
        s=$(printf '%s' "$s" | cut -c1-40)
        s="${s%-*}"
    fi
    printf '%s' "$s"
}

find_agent_pr() {
    local expr
    expr="[.[] | select(((.headRefName | startswith(\"opencode/dispatch-\")) or (.headRefName | startswith(\"opencode/schedule-\"))) and (.body | test(\"#$ISSUE_NUMBER([^0-9]|\$)\"))) ] | sort_by(.createdAt)[-1] | .number // empty"
    gh pr list --state open --json number,headRefName,createdAt,body --jq "$expr"
}

main() {
    local pr title slug branch old_branch cleaned tmpfile

    pr=$(find_agent_pr || true)
    if [ -z "$pr" ]; then
        log "no agent PR found; nothing to clean."
        exit 0
    fi

    title=$(gh issue view "$ISSUE_NUMBER" --json title --jq '.title' 2>/dev/null || true)
    slug=$(slugify "$title")
    branch="issue/$ISSUE_NUMBER${slug:+-$slug}"

    old_branch=$(gh pr view "$pr" --json headRefName --jq '.headRefName' 2>/dev/null || true)
    if [ -z "$old_branch" ]; then
        log "could not read head branch of PR #$pr; aborting cleanup."
        exit 0
    fi

    cleaned=$(gh pr view "$pr" --json body --jq '.body' 2>/dev/null | strip_footer || true)
    if [ -n "$cleaned" ]; then
        tmpfile=$(mktemp)
        printf '%s\n' "$cleaned" > "$tmpfile"
        if gh pr edit "$pr" --body-file "$tmpfile"; then
            log "PR #$pr body trimmed to template."
        else
            log "failed to edit PR #$pr body."
        fi
        rm -f "$tmpfile"
    fi

    log "renaming branch $old_branch -> $branch"
    if git fetch origin "$old_branch" \
        && git checkout -b "$branch" "origin/$old_branch" \
        && git push -u origin "$branch" \
        && git push origin ":$old_branch"; then
        log "PR #$pr retargeted to $branch."
    else
        log "failed to rename branch to $branch."
    fi
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main
fi
