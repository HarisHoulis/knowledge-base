#!/usr/bin/env bash
set -euo pipefail

ISSUE_NUMBER="${1:-}"
WORKFLOW_DIR=".github/workflows"
PROPOSAL_DIR="docs/workflow-proposals"

tracked_changed=$(git diff --name-only HEAD -- "$WORKFLOW_DIR" || true)
untracked=$(git ls-files --others --exclude-standard -- "$WORKFLOW_DIR" || true)

if [ -z "$tracked_changed" ] && [ -z "$untracked" ]; then
    echo "[suggest-workflow-change] No workflow changes. Nothing to do."
    exit 0
fi

timestamp=$(date +%Y-%m-%d-%H%M%S)
proposal="$PROPOSAL_DIR/${ISSUE_NUMBER:+${ISSUE_NUMBER}-}${timestamp}.md"
mkdir -p "$PROPOSAL_DIR"

all_changed=$(printf '%s\n%s\n' "$tracked_changed" "$untracked" | sed '/^$/d' | sort -u)

{
    echo "# Workflow Proposal"
    echo
    echo "The agent cannot push changes to \`.github/workflows/\` (the run token lacks \`workflows\` permission), so this PR proposes them instead."
    echo "Apply the diff below manually after review."
    echo
    echo "- **Issue**: ${ISSUE_NUMBER:+#$ISSUE_NUMBER}"
    echo "- **Date**: ${timestamp}"
    echo "- **Files**: $(printf '%s' "$all_changed" | tr '\n' ', ' | sed 's/, $//')"
    echo
} > "$proposal"

while IFS= read -r file; do
    [ -n "$file" ] || continue
    echo "## $file" >> "$proposal"
    echo >> "$proposal"
    echo '```diff' >> "$proposal"
    if git ls-files --error-unmatch --quiet -- "$file" 2>/dev/null; then
        { git diff HEAD -- "$file" || true; } >> "$proposal"
    else
        git add -N -- "$file"
        { git diff HEAD -- "$file" || true; } >> "$proposal"
        git reset -q -- "$file"
    fi
    echo '```' >> "$proposal"
    echo >> "$proposal"
done <<< "$all_changed"

if [ -n "$tracked_changed" ]; then
    git restore --staged --worktree -- $tracked_changed
fi
if [ -n "$untracked" ]; then
    rm -- $untracked
fi

echo "[suggest-workflow-change] Proposed workflow changes in $proposal. Workflow files reverted. Apply the diff manually after PR review."
