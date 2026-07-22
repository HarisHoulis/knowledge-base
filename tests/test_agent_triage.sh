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

if echo "\$*" | grep -q "repo view --json owner"; then
    echo "\${MOCK_GH_REPO_OWNER:-test-owner}"
    exit 0
fi

if echo "\$*" | grep -q "^issue list "; then
    echo "\${MOCK_GH_LIST_RESULT-5}"
    exit 0
fi

if echo "\$*" | grep -q "issue view.*--json labels"; then
    for arg in "\$@"; do
        if [[ "\$arg" =~ ^[0-9]+\$ ]]; then
            if [ "\$arg" = "99" ]; then
                echo ""
            else
                echo "ready-for-agent"
            fi
            exit 0
        fi
    done
    echo "ready-for-agent"
    exit 0
fi

if echo "\$*" | grep -q "^issue edit "; then
    exit 0
fi

echo "gh: unrecognized invocation: \$*" >&2
exit 1
MOCK
    chmod +x "$mock_dir/gh"
}

test_no_issues_found() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"

    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    MOCK_GH_LIST_RESULT='' \
        PATH="$mock_dir:$PATH" \
        bash "$SCRIPT_DIR/scripts/agent-triage.sh" > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    grep -q "Nothing to do" "$test_dir/stderr" || { echo "  FAIL: expected 'Nothing to do' in stderr"; fail=1; }
    [ ! -s "$test_dir/stdout" ] || { echo "  FAIL: expected no output on stdout"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: no issues found"
}

test_finds_and_assigns_oldest() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"

    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    MOCK_GH_LIST_RESULT='5' \
        PATH="$mock_dir:$PATH" \
        bash "$SCRIPT_DIR/scripts/agent-triage.sh" > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    [ "$(cat "$test_dir/stdout")" = "5" ] || { echo "  FAIL: expected stdout '5', got '$(cat "$test_dir/stdout")'"; fail=1; }
    grep -q "edit.*--add-assignee.*github-actions" "$calls_file" || { echo "  FAIL: expected gh issue edit --add-assignee"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: finds and assigns oldest issue"
}

test_uses_provided_issue() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"

    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    PATH="$mock_dir:$PATH" \
        bash "$SCRIPT_DIR/scripts/agent-triage.sh" 42 > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    [ "$(cat "$test_dir/stdout")" = "42" ] || { echo "  FAIL: expected stdout '42', got '$(cat "$test_dir/stdout")'"; fail=1; }
    grep -q "issue view 42 --json labels" "$calls_file" || { echo "  FAIL: expected gh issue view 42"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: uses provided issue number"
}

test_rejects_issue_without_label() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"

    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    PATH="$mock_dir:$PATH" \
        bash "$SCRIPT_DIR/scripts/agent-triage.sh" 99 > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 1 ] || { echo "  FAIL: expected exit 1, got $rc"; fail=1; }
    grep -q "does not have label" "$test_dir/stderr" || { echo "  FAIL: expected 'does not have label' in stderr"; fail=1; }
    [ ! -s "$test_dir/stdout" ] || { echo "  FAIL: expected no output on stdout"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: rejects issue without ready-for-agent label"
}

test_assigns_to_github_actions_bot() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"

    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    MOCK_GH_LIST_RESULT='1' \
        PATH="$mock_dir:$PATH" \
        bash "$SCRIPT_DIR/scripts/agent-triage.sh" > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    grep -q "github-actions\[bot\]" "$calls_file" || { echo "  FAIL: expected assignment to github-actions[bot]"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: assigns to github-actions[bot]"
}

echo "=== agent-triage tests ==="
test_no_issues_found && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_finds_and_assigns_oldest && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_uses_provided_issue && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_rejects_issue_without_label && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_assigns_to_github_actions_bot && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
echo "=========================="
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] || exit 1
