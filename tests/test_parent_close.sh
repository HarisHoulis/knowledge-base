#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PASS=0
FAIL=0

make_mock_gh() {
    local mock_dir="$1"
    local calls_file="$2"
    cat > "$mock_dir/gh" << MOCK
#!/usr/bin/env bash
echo "gh \$*" >> "$calls_file"

# gh repo view --json nameWithOwner
if [[ "\$*" == repo\ view\ --json\ nameWithOwner* ]]; then
    echo '{"nameWithOwner": "test-owner/test-repo"}'
    exit 0
fi

# Extract URL from second arg
URL="\${2:-}"

# /issues/NUMBER/sub_issues — return open count
if echo "\$URL" | grep -q "/sub_issues"; then
    echo "\${MOCK_GH_OPEN_COUNT:-0}"
    exit 0
fi

# /issues/NUMBER --jq ... — return parent number
if echo "\$*" | grep -q -- "--jq.*parent"; then
    echo "\${MOCK_GH_PARENT:-}"
    exit 0
fi

# PATCH — close parent (just succeed)
if [[ "\$*" == *"-X PATCH"* ]]; then
    exit 0
fi

# gha missing — skip
echo "gh: unrecognized invocation: \$*" >&2
exit 1
MOCK
    chmod +x "$mock_dir/gh"
}

assert_gh_calls_contain() {
    local calls_file="$1"
    local expected="$2"
    if ! grep -q "$expected" "$calls_file"; then
        echo "  FAIL: expected gh call containing '$expected', got: $(cat "$calls_file")"
        return 1
    fi
}

assert_gh_calls_not_contain() {
    local calls_file="$1"
    local expected="$2"
    if grep -q "$expected" "$calls_file"; then
        echo "  FAIL: unexpected gh call containing '$expected', got: $(cat "$calls_file")"
        return 1
    fi
}

test_all_sub_issues_closed() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"

    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    PATH="$mock_dir:$PATH" GITHUB_REPOSITORY="test-owner/test-repo" \
        MOCK_GH_PARENT="42" MOCK_GH_OPEN_COUNT="0" \
        bash "$SCRIPT_DIR/scripts/close-completed-parent.sh" 1 > "$test_dir/output" 2>&1
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "FAIL: all closed — expected exit 0, got $rc"; fail=1; }
    assert_gh_calls_contain "$calls_file" "PATCH.*42" || { echo "  (expected parent #42 to be closed)"; fail=1; }
    grep -q "Closed parent" "$test_dir/output" || { echo "  FAIL: expected 'Closed parent' in output"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: all sub-issues closed"
}

test_sub_issues_remain_open() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"

    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    PATH="$mock_dir:$PATH" GITHUB_REPOSITORY="test-owner/test-repo" \
        MOCK_GH_PARENT="42" MOCK_GH_OPEN_COUNT="2" \
        bash "$SCRIPT_DIR/scripts/close-completed-parent.sh" 1 > "$test_dir/output" 2>&1
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "FAIL: open remaining — expected exit 0, got $rc"; fail=1; }
    assert_gh_calls_not_contain "$calls_file" "PATCH" || { echo "  (should not have closed parent)"; fail=1; }
    grep -q "open sub-issue" "$test_dir/output" || { echo "  FAIL: expected 'open sub-issue' in output"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: sub-issues remain open"
}

test_no_parent() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"

    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    PATH="$mock_dir:$PATH" GITHUB_REPOSITORY="test-owner/test-repo" \
        MOCK_GH_PARENT="" MOCK_GH_OPEN_COUNT="0" \
        bash "$SCRIPT_DIR/scripts/close-completed-parent.sh" 1 > "$test_dir/output" 2>&1
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "FAIL: no parent — expected exit 0, got $rc"; fail=1; }
    assert_gh_calls_not_contain "$calls_file" "sub_issues" || { echo "  (should not have checked sub-issues)"; fail=1; }
    assert_gh_calls_not_contain "$calls_file" "PATCH" || { echo "  (should not have closed anything)"; fail=1; }
    grep -q "no parent" "$test_dir/output" || { echo "  FAIL: expected 'no parent' in output"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: no parent"
}

test_no_issue_number() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"

    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    PATH="$mock_dir:$PATH" GITHUB_REPOSITORY="test-owner/test-repo" \
        bash "$SCRIPT_DIR/scripts/close-completed-parent.sh" > "$test_dir/output" 2>&1
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 1 ] || { echo "FAIL: no issue number — expected exit 1, got $rc"; fail=1; }
    grep -q "No issue number" "$test_dir/output" || { echo "  FAIL: expected 'No issue number' in output"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: no issue number"
}

echo "=== parent-close tests ==="
test_all_sub_issues_closed && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_sub_issues_remain_open && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_no_parent && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_no_issue_number && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
echo "=========================="
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] || exit 1
