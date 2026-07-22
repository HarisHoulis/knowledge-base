#!/usr/bin/env bash
set -euo pipefail

ISSUE_NUMBER="${1:-${ISSUE_NUMBER:-}}"
GITHUB_REPOSITORY="${GITHUB_REPOSITORY:-}"

if [ -z "$ISSUE_NUMBER" ]; then
    echo "[close-completed-parent] No issue number provided. Usage: $0 <issue-number>" >&2
    exit 1
fi

if [ -z "$GITHUB_REPOSITORY" ]; then
    GITHUB_REPOSITORY=$(gh repo view --json nameWithOwner -q .nameWithOwner 2>/dev/null || true)
    if [ -z "$GITHUB_REPOSITORY" ]; then
        echo "[close-completed-parent] Could not determine repository." >&2
        exit 1
    fi
fi

PARENT=$(gh api "/repos/$GITHUB_REPOSITORY/issues/$ISSUE_NUMBER" --jq '.parent.number // empty' 2>/dev/null || true)

if [ -z "$PARENT" ]; then
    echo "[close-completed-parent] Issue #$ISSUE_NUMBER has no parent. Nothing to do."
    exit 0
fi

OPEN_COUNT=$(gh api "/repos/$GITHUB_REPOSITORY/issues/$PARENT/sub_issues" --jq '[.[] | select(.state == "open")] | length' 2>/dev/null || echo "0")

if [ "$OPEN_COUNT" -gt 0 ]; then
    echo "[close-completed-parent] Parent #$PARENT has $OPEN_COUNT open sub-issue(s). Not closing."
    exit 0
fi

gh api -X PATCH "/repos/$GITHUB_REPOSITORY/issues/$PARENT" \
    -f state=closed \
    --silent

echo "[close-completed-parent] Closed parent #$PARENT — all sub-issues resolved."
