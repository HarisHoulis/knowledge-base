#!/usr/bin/env bash
set -euo pipefail

# Best-effort post-process after an agent-triage run, scoped to the PR the
# agent created for the current issue (matched by "#<n>" in the PR body):
#  1. Strip the action's footer from the PR body, starting at the "Triggered by"
#     marker. Combined with auto-implement's "final response must be exactly the
#     populated template" rule, the body ends up as just the template.
# Cleanup failures are logged, never fatal: the PR already exists.

ISSUE_NUMBER="${1:-}"

log() { echo "[agent-triage] post-process: $*" >&2; }

strip_footer() {
    sed '/^Triggered by /,$d'
}

find_agent_pr() {
    local expr
    expr="[.[] | select(((.headRefName | startswith(\"opencode/dispatch-\")) or (.headRefName | startswith(\"opencode/schedule-\"))) and (.body | test(\"#$ISSUE_NUMBER([^0-9]|\$)\"))) ] | sort_by(.createdAt)[-1] | .number // empty"
    gh pr list --state open --json number,headRefName,createdAt,body --jq "$expr"
}

main() {
    local pr cleaned tmpfile

    pr=$(find_agent_pr || true)
    if [ -z "$pr" ]; then
        log "no agent PR found; nothing to clean."
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
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main
fi
