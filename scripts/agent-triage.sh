#!/usr/bin/env bash
set -euo pipefail

ISSUE_NUMBER="${1:-${ISSUE_OVERRIDE:-}}"

if [ "$ISSUE_NUMBER" = "0" ]; then
    ISSUE_NUMBER=""
fi

if [ -n "$ISSUE_NUMBER" ]; then
    echo "[agent-triage] Validating provided issue #$ISSUE_NUMBER..." >&2
    LABELS=$(gh issue view "$ISSUE_NUMBER" --json labels --jq '[.labels[].name] | join(",")')
    if [[ ",$LABELS," != *",ready-for-agent,"* ]]; then
        echo "[agent-triage] Issue #$ISSUE_NUMBER does not have label 'ready-for-agent' (got: $LABELS). Exiting." >&2
        exit 1
    fi
    echo "[agent-triage] Claiming issue #$ISSUE_NUMBER with in-progress label..." >&2
    gh api -X PUT "repos/{owner}/{repo}/issues/$ISSUE_NUMBER/labels" -f labels[]=in-progress > /dev/null
    echo "$ISSUE_NUMBER"
    exit 0
fi

echo "[agent-triage] Finding viable ready-for-agent issue..." >&2
REPO_OWNER=$(gh repo view --json owner --jq '.owner.login')

CANDIDATES=$(gh issue list \
    --label "ready-for-agent" \
    --assignee "" \
    --author "$REPO_OWNER" \
    --state open \
    --json number,createdAt \
    --jq 'sort_by(.createdAt) | .[].number') || true

if [ -z "$CANDIDATES" ]; then
    echo "[agent-triage] No ready-for-agent issues found. Nothing to do." >&2
    exit 0
fi

SELECTED=""
for NUM in $CANDIDATES; do
    echo "[agent-triage] Checking issue #$NUM..." >&2

    BLOCKED=$(gh issue view "$NUM" --json blockedBy --jq '.blockedBy.totalCount')
    if [ "$BLOCKED" -gt 0 ]; then
        echo "[agent-triage] Issue #$NUM is blocked. Skipping." >&2
        continue
    fi

    SUB_COUNT=$(gh issue view "$NUM" --json subIssues --jq '.subIssues.totalCount')
    if [ "$SUB_COUNT" -gt 0 ]; then
        echo "[agent-triage] Issue #$NUM is a parent with $SUB_COUNT sub-issue(s)." >&2
        VIABLE_SUB=""
        SUB_NUMBERS=$(gh issue view "$NUM" --json subIssues --jq '.subIssues.nodes | sort_by(.number) | .[] | select(.state == "OPEN") | .number')
        for SUB in $SUB_NUMBERS; do
            SUB_BLOCKED=$(gh issue view "$SUB" --json blockedBy --jq '.blockedBy.totalCount')
            if [ "$SUB_BLOCKED" -eq 0 ]; then
                VIABLE_SUB="$SUB"
                break
            fi
        done

        if [ -n "$VIABLE_SUB" ]; then
            echo "[agent-triage] Picking unblocked sub-issue #$VIABLE_SUB." >&2
            SELECTED="$VIABLE_SUB"
        else
            echo "[agent-triage] All sub-issues blocked or closed. Implementing parent #$NUM." >&2
            SELECTED="$NUM"
        fi
        break
    fi

    SELECTED="$NUM"
    break
done

if [ -z "$SELECTED" ]; then
    echo "[agent-triage] No viable candidates found after scanning all issues." >&2
    gh issue create \
        --title "Agent Triage: No viable candidates found" \
        --label "needs-triage" \
        --body "The automated agent triage scan found no issues that are:
- Labeled ready-for-agent
- Not blocked
- Has viable parent -> sub-issue candidates

All ready-for-agent issues were either blocked or had all sub-issues blocked.
This may indicate a systemic bottleneck."
    exit 0
fi

echo "[agent-triage] Validating issue #$SELECTED..." >&2
LABELS=$(gh issue view "$SELECTED" --json labels --jq '[.labels[].name] | join(",")')
if [[ ",$LABELS," != *",ready-for-agent,"* ]]; then
    echo "[agent-triage] Issue #$SELECTED does not have label 'ready-for-agent' (got: $LABELS). Exiting." >&2
    exit 1
fi

echo "[agent-triage] Claiming issue #$SELECTED with in-progress label..." >&2
gh api -X PUT "repos/{owner}/{repo}/issues/$SELECTED/labels" -f labels[]=in-progress > /dev/null

echo "$SELECTED"
