#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PASS=0
FAIL=0

setup_repo() {
    local repo_dir="$1"
    git -C "$repo_dir" init --quiet
    git -C "$repo_dir" config user.email "test@test.com"
    git -C "$repo_dir" config user.name "Test"
    mkdir -p "$repo_dir/.github/workflows"
    cat > "$repo_dir/.github/workflows/daily-ingest.yml" << 'EOF'
name: Daily Ingest
on:
  schedule:
    - cron: "0 6 * * *"
EOF
    git -C "$repo_dir" add .
    git -C "$repo_dir" commit -m "init" --quiet
    git -C "$repo_dir" branch -M main
}

install_guard() {
    local repo_dir="$1"
    mkdir -p "$repo_dir/scripts" "$repo_dir/.githooks-ci"
    cp "$SCRIPT_DIR/scripts/suggest-workflow-change.sh" "$repo_dir/scripts/"
    chmod +x "$repo_dir/scripts/suggest-workflow-change.sh"
    cp "$SCRIPT_DIR/.githooks-ci/pre-commit" "$repo_dir/.githooks-ci/"
    chmod +x "$repo_dir/.githooks-ci/pre-commit"
}

proposal_files() {
    local repo_dir="$1"
    ls "$repo_dir/docs/workflow-proposals/" 2>/dev/null || true
}

test_no_workflow_changes_is_noop() {
    local test_dir; test_dir=$(mktemp -d)
    setup_repo "$test_dir"
    install_guard "$test_dir"

    echo "unrelated" > "$test_dir/README.md"

    local rc
    set +e
    (cd "$test_dir" && bash scripts/suggest-workflow-change.sh 42) > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    [ -z "$(proposal_files "$test_dir")" ] || { echo "  FAIL: expected no proposal files, got $(proposal_files "$test_dir")"; fail=1; }
    grep -qi "no workflow changes" "$test_dir/stdout" || { echo "  FAIL: expected 'no workflow changes' in stdout"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: no workflow changes is a no-op"
}

test_modified_tracked_workflow_becomes_proposal() {
    local test_dir; test_dir=$(mktemp -d)
    setup_repo "$test_dir"
    install_guard "$test_dir"

    printf 'name: Daily Ingest\non:\n  schedule:\n    - cron: "0 7 * * *"\n' > "$test_dir/.github/workflows/daily-ingest.yml"

    local rc
    set +e
    (cd "$test_dir" && bash scripts/suggest-workflow-change.sh 42) > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    local proposal
    proposal=$(proposal_files "$test_dir")
    case "$proposal" in
        *42-*.md) ;;
        *) echo "  FAIL: expected proposal named 42-*.md, got '$proposal'"; fail=1; ;;
    esac
    [ -f "$test_dir/docs/workflow-proposals/$proposal" ] || fail=1
    grep -q "daily-ingest.yml" "$test_dir/docs/workflow-proposals/$proposal" || { echo "  FAIL: proposal should mention daily-ingest.yml"; fail=1; }
    grep -q -- "- \*\*Files\*\*: .*daily-ingest.yml" "$test_dir/docs/workflow-proposals/$proposal" || { echo "  FAIL: proposal header should list affected files"; fail=1; }
    grep -q "0 7 \* \* \*" "$test_dir/docs/workflow-proposals/$proposal" || { echo "  FAIL: proposal should contain the new cron line in a diff"; fail=1; }
    [ "$(git -C "$test_dir" status --porcelain -- .github/workflows/)" = "" ] || { echo "  FAIL: workflow file should be reverted"; fail=1; }
    [ "$(git -C "$test_dir" status --porcelain -- docs/)" != "" ] || { echo "  FAIL: proposal should be untracked (pending commit)"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: modified tracked workflow becomes a proposal"
}

test_new_untracked_workflow_becomes_proposal() {
    local test_dir; test_dir=$(mktemp -d)
    setup_repo "$test_dir"
    install_guard "$test_dir"

    cat > "$test_dir/.github/workflows/weekly-digest.yml" << 'EOF'
name: Weekly Digest
on:
  schedule:
    - cron: "0 12 * * 1"
EOF

    local rc
    set +e
    (cd "$test_dir" && bash scripts/suggest-workflow-change.sh 42) > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    local proposal
    proposal=$(proposal_files "$test_dir")
    case "$proposal" in
        *42-*.md) ;;
        *) echo "  FAIL: expected proposal named 42-*.md, got '$proposal'"; fail=1; ;;
    esac
    grep -q "weekly-digest.yml" "$test_dir/docs/workflow-proposals/$proposal" || { echo "  FAIL: proposal should mention weekly-digest.yml"; fail=1; }
    grep -q "Weekly Digest" "$test_dir/docs/workflow-proposals/$proposal" || { echo "  FAIL: proposal should contain the new file content in a diff"; fail=1; }
    [ ! -e "$test_dir/.github/workflows/weekly-digest.yml" ] || { echo "  FAIL: new workflow file should be removed"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: new untracked workflow becomes a proposal"
}

test_precommit_hook_blocks_workflow_commits() {
    local test_dir; test_dir=$(mktemp -d)
    setup_repo "$test_dir"
    install_guard "$test_dir"
    git -C "$test_dir" config core.hooksPath .githooks-ci

    printf 'name: Daily Ingest\non:\n  schedule:\n    - cron: "0 7 * * *"\n' > "$test_dir/.github/workflows/daily-ingest.yml"
    git -C "$test_dir" add .github/workflows/daily-ingest.yml

    local rc
    set +e
    (cd "$test_dir" && git commit -m "chore: tweak cron" > "$test_dir/hookout" 2>&1)
    rc=$?
    set -e

    local fail=0
    [ "$rc" -ne 0 ] || { echo "  FAIL: commit should be blocked"; fail=1; }
    grep -q "suggest-workflow-change.sh" "$test_dir/hookout" || { echo "  FAIL: hook message should point at the guard script"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: pre-commit hook blocks workflow-file commits"
}

test_precommit_hook_allows_non_workflow_commits() {
    local test_dir; test_dir=$(mktemp -d)
    setup_repo "$test_dir"
    install_guard "$test_dir"
    git -C "$test_dir" config core.hooksPath .githooks-ci

    echo "unrelated" > "$test_dir/README.md"
    git -C "$test_dir" add README.md

    local rc
    set +e
    (cd "$test_dir" && git commit -m "docs: tweak readme" > "$test_dir/hookout" 2>&1)
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: non-workflow commit should succeed, got $rc: $(cat "$test_dir/hookout")"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: pre-commit hook allows non-workflow commits"
}

echo "=== suggest-workflow-change tests ==="
test_no_workflow_changes_is_noop && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_modified_tracked_workflow_becomes_proposal && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_new_untracked_workflow_becomes_proposal && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_precommit_hook_blocks_workflow_commits && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_precommit_hook_allows_non_workflow_commits && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
echo "=========================="
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] || exit 1
