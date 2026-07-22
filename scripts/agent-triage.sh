#!/usr/bin/env bash
set -euo pipefail

ISSUE_NUMBER="${1:-${ISSUE_OVERRIDE:-}}"

# Ignore "0" from the workflow_dispatch default input
if [ "$ISSUE_NUMBER" = "0" ]; then
    ISSUE_NUMBER=""
fi

if [ -z "$ISSUE_NUMBER" ]; then
    echo "[agent-triage] Finding oldest unassigned ready-for-agent issue..." >&2
    REPO_OWNER=$(gh repo view --json owner --jq '.owner.login')
    ISSUE_NUMBER=$(gh issue list \
        --label "ready-for-agent" \
        --assignee "" \
        --author "$REPO_OWNER" \
        --state open \
        --json number,createdAt \
        --jq 'sort_by(.createdAt) | .[0].number // empty') || true

    if [ -z "$ISSUE_NUMBER" ]; then
        echo "[agent-triage] No unassigned ready-for-agent issues found. Nothing to do." >&2
        exit 0
    fi

    echo "[agent-triage] Found issue #$ISSUE_NUMBER" >&2
fi

echo "[agent-triage] Validating issue #$ISSUE_NUMBER..." >&2
LABELS=$(gh issue view "$ISSUE_NUMBER" --json labels --jq '[.labels[].name] | join(",")')

if [[ ",$LABELS," != *",ready-for-agent,"* ]]; then
    echo "[agent-triage] Issue #$ISSUE_NUMBER does not have label 'ready-for-agent' (got: $LABELS). Exiting." >&2
    exit 1
fi

echo "[agent-triage] Assigning issue #$ISSUE_NUMBER to github-actions[bot]..." >&2
gh issue edit "$ISSUE_NUMBER" --add-assignee "github-actions[bot]"

echo "$ISSUE_NUMBER"
