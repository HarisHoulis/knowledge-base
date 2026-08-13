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
    echo "initial" > "$repo_dir/README.md"
    git -C "$repo_dir" add README.md
    git -C "$repo_dir" commit -m "init" --quiet
    git -C "$repo_dir" branch -M main
}

make_mock_gh() {
    local mock_dir="$1"
    local calls_file="$2"
    cat > "$mock_dir/gh" << MOCK
#!/usr/bin/env bash
echo "gh \$*" >> "$calls_file"
echo "https://github.com/example/pr/1"
MOCK
    chmod +x "$mock_dir/gh"
}

make_mock_python() {
    local mock_dir="$1"
    local body="$2"
    for name in python python3; do
        cat > "$mock_dir/$name" << MOCK
#!/usr/bin/env bash
$body
MOCK
        chmod +x "$mock_dir/$name"
    done
}

assert_no_branch() {
    if git -C "$1" branch | grep -q "daily-ingest"; then
        echo "  FAIL: unexpected daily-ingest branch"
        return 1
    fi
}

assert_branch_exists() {
    if ! git -C "$1" branch | grep -q "daily-ingest"; then
        echo "  FAIL: expected daily-ingest branch"
        return 1
    fi
}

assert_no_gh_calls() {
    if [ -s "$1" ]; then
        echo "  FAIL: expected no gh calls, got: $(cat "$1")"
        return 1
    fi
}

assert_gh_pr_created() {
    if ! grep -q "pr create" "$1"; then
        echo "  FAIL: expected gh pr create, got: $(cat "$1")"
        return 1
    fi
}

assert_gh_pr_merged() {
    if ! grep -q "pr merge --auto --squash" "$1"; then
        echo "  FAIL: expected gh pr merge --auto --squash, got: $(cat "$1")"
        return 1
    fi
}

assert_gh_pr_not_merged() {
    if grep -q "pr merge" "$1"; then
        echo "  FAIL: expected no gh pr merge, got: $(cat "$1")"
        return 1
    fi
}

assert_gh_pr_commented() {
    if ! grep -q "pr comment" "$1"; then
        echo "  FAIL: expected gh pr comment, got: $(cat "$1")"
        return 1
    fi
}

test_clean_repo() {
    local test_dir; test_dir=$(mktemp -d)
    local repo_dir="$test_dir/repo"
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$repo_dir" "$mock_dir"

    setup_repo "$repo_dir"
    make_mock_gh "$mock_dir" "$calls_file"
    make_mock_python "$mock_dir" "exit 0"

    local rc
    set +e
    PATH="$mock_dir:$PATH" GH="$mock_dir/gh" KB_PATH="$repo_dir" KB_STATE="$test_dir/state.json" \
        bash "$SCRIPT_DIR/scripts/daily-ingest.sh" > "$test_dir/output" 2>&1
    rc=$?
    set -e
    rm -rf "$test_dir"

    [ "$rc" -eq 0 ] || { echo "FAIL: clean repo — expected exit 0, got $rc"; return 1; }
    echo "PASS: clean repo"
}

test_dirty_repo() {
    local test_dir; test_dir=$(mktemp -d)
    local repo_dir="$test_dir/repo"
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    local remote_dir="$test_dir/remote.git"
    mkdir -p "$repo_dir" "$mock_dir"

    setup_repo "$repo_dir"
    make_mock_gh "$mock_dir" "$calls_file"
    make_mock_python "$mock_dir" "mkdir -p \"$repo_dir/concepts\" && echo 'new concept' > \"$repo_dir/concepts/test.md\""
    git -C "$repo_dir" remote add origin "$remote_dir"
    git init --bare "$remote_dir" --quiet

    local rc
    set +e
    PATH="$mock_dir:$PATH" GH="$mock_dir/gh" KB_PATH="$repo_dir" KB_STATE="$test_dir/state.json" \
        bash "$SCRIPT_DIR/scripts/daily-ingest.sh" > "$test_dir/output" 2>&1
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "FAIL: dirty repo — expected exit 0, got $rc"; fail=1; }
    assert_branch_exists "$repo_dir" || fail=1
    assert_gh_pr_created "$calls_file" || fail=1
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: dirty repo"
}

test_pipeline_failure() {
    local test_dir; test_dir=$(mktemp -d)
    local repo_dir="$test_dir/repo"
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$repo_dir" "$mock_dir"

    setup_repo "$repo_dir"
    make_mock_gh "$mock_dir" "$calls_file"
    make_mock_python "$mock_dir" "exit 42"

    local rc
    set +e
    PATH="$mock_dir:$PATH" GH="$mock_dir/gh" KB_PATH="$repo_dir" KB_STATE="$test_dir/state.json" \
        bash "$SCRIPT_DIR/scripts/daily-ingest.sh" > "$test_dir/output" 2>&1
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 42 ] || { echo "FAIL: pipeline failure — expected exit 42, got $rc"; fail=1; }
    assert_no_branch "$repo_dir" || fail=1
    assert_no_gh_calls "$calls_file" || fail=1
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: pipeline failure"
}

test_dry_run() {
    local test_dir; test_dir=$(mktemp -d)
    local repo_dir="$test_dir/repo"
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$repo_dir" "$mock_dir"

    setup_repo "$repo_dir"
    make_mock_gh "$mock_dir" "$calls_file"
    make_mock_python "$mock_dir" "mkdir -p \"$repo_dir/concepts\" && echo 'new concept' > \"$repo_dir/concepts/test.md\""

    local rc
    set +e
    PATH="$mock_dir:$PATH" GH="$mock_dir/gh" KB_PATH="$repo_dir" KB_STATE="$test_dir/state.json" \
        bash "$SCRIPT_DIR/scripts/daily-ingest.sh" --dry-run > "$test_dir/output" 2>&1
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "FAIL: dry run — expected exit 0, got $rc"; fail=1; }
    assert_no_branch "$repo_dir" || fail=1
    assert_no_gh_calls "$calls_file" || fail=1
    grep -q "Dry run" "$test_dir/output" || { echo "FAIL: expected 'Dry run' in output"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: dry run"
}

test_content_only_auto_merge() {
    local test_dir; test_dir=$(mktemp -d)
    local repo_dir="$test_dir/repo"
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    local remote_dir="$test_dir/remote.git"
    mkdir -p "$repo_dir" "$mock_dir"

    setup_repo "$repo_dir"
    make_mock_gh "$mock_dir" "$calls_file"
    make_mock_python "$mock_dir" "mkdir -p \"$repo_dir/concepts\" && echo 'new concept' > \"$repo_dir/concepts/test.md\""
    git -C "$repo_dir" remote add origin "$remote_dir"
    git init --bare "$remote_dir" --quiet

    local rc
    set +e
    PATH="$mock_dir:$PATH" GH="$mock_dir/gh" KB_PATH="$repo_dir" KB_STATE="$test_dir/state.json" \
        bash "$SCRIPT_DIR/scripts/daily-ingest.sh" > "$test_dir/output" 2>&1
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "FAIL: content-only repo — expected exit 0, got $rc"; fail=1; }
    assert_branch_exists "$repo_dir" || fail=1
    assert_gh_pr_created "$calls_file" || fail=1
    assert_gh_pr_merged "$calls_file" || fail=1
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: content-only repo auto-merges"
}

test_mixed_repo_comment() {
    local test_dir; test_dir=$(mktemp -d)
    local repo_dir="$test_dir/repo"
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    local remote_dir="$test_dir/remote.git"
    mkdir -p "$repo_dir" "$mock_dir"

    setup_repo "$repo_dir"
    make_mock_gh "$mock_dir" "$calls_file"
    make_mock_python "$mock_dir" "mkdir -p \"$repo_dir/concepts\" \"$repo_dir/scripts\" && echo 'new concept' > \"$repo_dir/concepts/test.md\" && echo '#!/usr/bin/env bash' > \"$repo_dir/scripts/tool.sh\" && chmod +x \"$repo_dir/scripts/tool.sh\""
    git -C "$repo_dir" remote add origin "$remote_dir"
    git init --bare "$remote_dir" --quiet

    local rc
    set +e
    PATH="$mock_dir:$PATH" GH="$mock_dir/gh" KB_PATH="$repo_dir" KB_STATE="$test_dir/state.json" \
        bash "$SCRIPT_DIR/scripts/daily-ingest.sh" > "$test_dir/output" 2>&1
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "FAIL: mixed repo — expected exit 0, got $rc"; fail=1; }
    assert_branch_exists "$repo_dir" || fail=1
    assert_gh_pr_created "$calls_file" || fail=1
    assert_gh_pr_not_merged "$calls_file" || fail=1
    assert_gh_pr_commented "$calls_file" || fail=1
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: mixed repo comments and skips auto-merge"
}

test_non_md_skip_merge() {
    local test_dir; test_dir=$(mktemp -d)
    local repo_dir="$test_dir/repo"
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    local remote_dir="$test_dir/remote.git"
    mkdir -p "$repo_dir" "$mock_dir"

    setup_repo "$repo_dir"
    make_mock_gh "$mock_dir" "$calls_file"
    make_mock_python "$mock_dir" "mkdir -p \"$repo_dir/concepts\" && echo 'draft note' > \"$repo_dir/concepts/notes.txt\""
    git -C "$repo_dir" remote add origin "$remote_dir"
    git init --bare "$remote_dir" --quiet

    local rc
    set +e
    PATH="$mock_dir:$PATH" GH="$mock_dir/gh" KB_PATH="$repo_dir" KB_STATE="$test_dir/state.json" \
        bash "$SCRIPT_DIR/scripts/daily-ingest.sh" > "$test_dir/output" 2>&1
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "FAIL: non-md under concepts — expected exit 0, got $rc"; fail=1; }
    assert_branch_exists "$repo_dir" || fail=1
    assert_gh_pr_created "$calls_file" || fail=1
    assert_gh_pr_not_merged "$calls_file" || fail=1
    assert_gh_pr_commented "$calls_file" || fail=1
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: non-md under concepts skips auto-merge"
}

test_auto_merge_failure_exits_zero() {
    local test_dir; test_dir=$(mktemp -d)
    local repo_dir="$test_dir/repo"
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    local remote_dir="$test_dir/remote.git"
    mkdir -p "$repo_dir" "$mock_dir"

    setup_repo "$repo_dir"
    make_mock_gh "$mock_dir" "$calls_file"
    make_mock_python "$mock_dir" "mkdir -p \"$repo_dir/concepts\" && echo 'new concept' > \"$repo_dir/concepts/test.md\""
    git -C "$repo_dir" remote add origin "$remote_dir"
    git init --bare "$remote_dir" --quiet

    cat > "$mock_dir/gh" << MOCK
#!/usr/bin/env bash
echo "gh \$*" >> "$calls_file"
echo "https://github.com/example/pr/1"
if [[ "\$1" == "pr" && "\$2" == "merge" ]]; then
    exit 1
fi
MOCK
    chmod +x "$mock_dir/gh"

    local rc
    set +e
    PATH="$mock_dir:$PATH" GH="$mock_dir/gh" KB_PATH="$repo_dir" KB_STATE="$test_dir/state.json" \
        bash "$SCRIPT_DIR/scripts/daily-ingest.sh" > "$test_dir/output" 2>&1
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "FAIL: auto-merge failure — expected exit 0, got $rc"; fail=1; }
    grep -q "failed to enable auto-merge" "$test_dir/output" || { echo "FAIL: expected auto-merge warning in output"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: auto-merge failure is best-effort (exit 0)"
}

test_limit_flag() {
    local test_dir; test_dir=$(mktemp -d)
    local repo_dir="$test_dir/repo"
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$repo_dir" "$mock_dir"

    setup_repo "$repo_dir"
    make_mock_gh "$mock_dir" "$calls_file"
    local args_file="$test_dir/pipeline_args"
    make_mock_python "$mock_dir" "echo \"\$@\" > $args_file && exit 0"

    local rc
    set +e
    PATH="$mock_dir:$PATH" GH="$mock_dir/gh" KB_PATH="$repo_dir" KB_STATE="$test_dir/state.json" \
        bash "$SCRIPT_DIR/scripts/daily-ingest.sh" --limit=3 > "$test_dir/output" 2>&1
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "FAIL: limit flag — expected exit 0, got $rc"; fail=1; }
    grep -q -- "--limit=3" "$test_dir/pipeline_args" 2>/dev/null || { echo "FAIL: expected --limit=3 in pipeline args, got: $(cat "$test_dir/pipeline_args" 2>/dev/null)"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: limit flag"
}

echo "=== daily-ingest tests ==="
test_clean_repo && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_dirty_repo && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_pipeline_failure && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_dry_run && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_content_only_auto_merge && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_mixed_repo_comment && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_non_md_skip_merge && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_auto_merge_failure_exits_zero && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_limit_flag && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
echo "======================"
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] || exit 1
