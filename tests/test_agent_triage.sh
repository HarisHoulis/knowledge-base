#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PASS=0
FAIL=0

make_mock_gh() {
    local mock_dir="$1"
    local calls_file="$2"
    cat > "$mock_dir/gh" << 'MOCKEOF'
#!/usr/bin/env bash
echo "gh $*" >> "CF"

# repo view --json owner
if [ "$1" = "repo" ] && [ "$2" = "view" ]; then
    echo "${MOCK_GH_REPO_OWNER:-test-owner}"
    exit 0
fi

# issue list
if [ "$1" = "issue" ] && [ "$2" = "list" ]; then
    echo "${MOCK_GH_LIST_RESULT:-}"
    exit 0
fi

# issue create
if [ "$1" = "issue" ] && [ "$2" = "create" ]; then
    exit 0
fi

# issue edit
if [ "$1" = "issue" ] && [ "$2" = "edit" ]; then
    exit 0
fi

# issue view
if [ "$1" = "issue" ] && [ "$2" = "view" ]; then
    NUM="$3"
    TAG=""
    if echo "$*" | grep -q "blockedBy.*totalCount"; then
        TAG="BLOCKED"
    elif echo "$*" | grep -q "subIssues.*totalCount"; then
        TAG="SUBCOUNT"
    elif echo "$*" | grep -q "subIssues.*OPEN.*number"; then
        TAG="OPENSUBS"
    elif echo "$*" | grep -q "labels.*join"; then
        TAG="LABELS"
    elif echo "$*" | grep -q "assignees.*totalCount"; then
        TAG="ASSIGNEES"
    fi
    if [ -n "$TAG" ]; then
        VARNAME="MOCK_GH_VIEW_${NUM}_${TAG}"
        VAL="${!VARNAME:-}"
        if [ "$TAG" = "LABELS" ] && [ -z "$VAL" ]; then
            [ "$NUM" = "99" ] && echo "" || echo "ready-for-agent"
        else
            echo "${VAL:-0}"
        fi
        exit 0
    fi
    exit 0
fi

# api
if [ "$1" = "api" ]; then
    exit 0
fi

echo "gh: unrecognized invocation: $*" >&2
exit 1
MOCKEOF
    sed "s|CF|$calls_file|g" "$mock_dir/gh" > "$mock_dir/gh.tmp"
    mv "$mock_dir/gh.tmp" "$mock_dir/gh"
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

test_leaf_not_blocked() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"
    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    MOCK_GH_LIST_RESULT='5' \
    MOCK_GH_VIEW_5_BLOCKED='0' \
    MOCK_GH_VIEW_5_SUBCOUNT='0' \
        PATH="$mock_dir:$PATH" \
        bash "$SCRIPT_DIR/scripts/agent-triage.sh" > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    [ "$(cat "$test_dir/stdout")" = "5" ] || { echo "  FAIL: expected stdout '5', got '$(cat "$test_dir/stdout")'"; fail=1; }
    grep -q "api.*issues/5/labels" "$calls_file" || { echo "  FAIL: expected gh api labels claim for 5"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: leaf not blocked picks issue"
}

test_uses_provided_issue() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"
    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    MOCK_GH_VIEW_42_BLOCKED='0' \
    MOCK_GH_VIEW_42_SUBCOUNT='0' \
        PATH="$mock_dir:$PATH" \
        bash "$SCRIPT_DIR/scripts/agent-triage.sh" 42 > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    [ "$(cat "$test_dir/stdout")" = "42" ] || { echo "  FAIL: expected stdout '42', got '$(cat "$test_dir/stdout")'"; fail=1; }
    grep -q "issue view 42" "$calls_file" || { echo "  FAIL: expected gh issue view 42"; fail=1; }
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

test_leaf_blocked_skips_to_next() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"
    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    MOCK_GH_LIST_RESULT='5 6' \
    MOCK_GH_VIEW_5_BLOCKED='1' \
    MOCK_GH_VIEW_5_SUBCOUNT='0' \
    MOCK_GH_VIEW_6_BLOCKED='0' \
    MOCK_GH_VIEW_6_SUBCOUNT='0' \
        PATH="$mock_dir:$PATH" \
        bash "$SCRIPT_DIR/scripts/agent-triage.sh" > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    [ "$(cat "$test_dir/stdout")" = "6" ] || { echo "  FAIL: expected stdout '6', got '$(cat "$test_dir/stdout")'"; fail=1; }
    grep -q "api.*issues/6/labels" "$calls_file" || { echo "  FAIL: expected gh api labels claim for 6"; fail=1; }
    grep -q "issue view 5" "$calls_file" || { echo "  FAIL: expected gh issue view 5 (checking blocked)"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: leaf blocked skips to next candidate"
}

test_parent_picks_unblocked_sub() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"
    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    MOCK_GH_LIST_RESULT='10' \
    MOCK_GH_VIEW_10_BLOCKED='0' \
    MOCK_GH_VIEW_10_SUBCOUNT='2' \
    MOCK_GH_VIEW_10_OPENSUBS='11 12' \
    MOCK_GH_VIEW_11_BLOCKED='1' \
    MOCK_GH_VIEW_12_BLOCKED='0' \
        PATH="$mock_dir:$PATH" \
        bash "$SCRIPT_DIR/scripts/agent-triage.sh" > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    [ "$(cat "$test_dir/stdout")" = "12" ] || { echo "  FAIL: expected stdout '12', got '$(cat "$test_dir/stdout")'"; fail=1; }
    grep -q "api.*issues/12/labels" "$calls_file" || { echo "  FAIL: expected gh api labels claim for 12"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: parent picks oldest unblocked sub-issue"
}

test_parent_skips_in_progress_sub() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"
    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    MOCK_GH_LIST_RESULT='10' \
    MOCK_GH_VIEW_10_BLOCKED='0' \
    MOCK_GH_VIEW_10_SUBCOUNT='2' \
    MOCK_GH_VIEW_10_OPENSUBS='11 12' \
    MOCK_GH_VIEW_11_BLOCKED='0' \
    MOCK_GH_VIEW_11_LABELS='in-progress' \
    MOCK_GH_VIEW_12_BLOCKED='0' \
    MOCK_GH_VIEW_12_LABELS='ready-for-agent' \
        PATH="$mock_dir:$PATH" \
        bash "$SCRIPT_DIR/scripts/agent-triage.sh" > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    [ "$(cat "$test_dir/stdout")" = "12" ] || { echo "  FAIL: expected stdout '12', got '$(cat "$test_dir/stdout")'"; fail=1; }
    grep -q "api.*issues/12/labels" "$calls_file" || { echo "  FAIL: expected gh api labels claim for 12"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: parent skips in-progress sub-issue"
}

test_parent_all_subs_blocked_skips_to_next() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"
    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    MOCK_GH_LIST_RESULT='10 5' \
    MOCK_GH_VIEW_10_BLOCKED='0' \
    MOCK_GH_VIEW_10_SUBCOUNT='2' \
    MOCK_GH_VIEW_10_OPENSUBS='11 12' \
    MOCK_GH_VIEW_11_BLOCKED='1' \
    MOCK_GH_VIEW_12_BLOCKED='1' \
    MOCK_GH_VIEW_5_BLOCKED='0' \
    MOCK_GH_VIEW_5_SUBCOUNT='0' \
        PATH="$mock_dir:$PATH" \
        bash "$SCRIPT_DIR/scripts/agent-triage.sh" > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    [ "$(cat "$test_dir/stdout")" = "5" ] || { echo "  FAIL: expected stdout '5', got '$(cat "$test_dir/stdout")'"; fail=1; }
    grep -q "api.*issues/5/labels" "$calls_file" || { echo "  FAIL: expected gh api labels claim for 5"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: parent with all subs blocked skips to next candidate"
}

test_parent_with_no_claimable_subs_skips_to_next() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"
    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    MOCK_GH_LIST_RESULT='10 5' \
    MOCK_GH_VIEW_10_BLOCKED='0' \
    MOCK_GH_VIEW_10_SUBCOUNT='2' \
    MOCK_GH_VIEW_10_OPENSUBS='11 12' \
    MOCK_GH_VIEW_11_BLOCKED='0' \
    MOCK_GH_VIEW_11_LABELS='in-progress' \
    MOCK_GH_VIEW_12_BLOCKED='0' \
    MOCK_GH_VIEW_12_LABELS='in-progress' \
    MOCK_GH_VIEW_5_BLOCKED='0' \
    MOCK_GH_VIEW_5_SUBCOUNT='0' \
        PATH="$mock_dir:$PATH" \
        bash "$SCRIPT_DIR/scripts/agent-triage.sh" > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    [ "$(cat "$test_dir/stdout")" = "5" ] || { echo "  FAIL: expected stdout '5', got '$(cat "$test_dir/stdout")'"; fail=1; }
    grep -q "api.*issues/5/labels" "$calls_file" || { echo "  FAIL: expected gh api labels claim for 5"; fail=1; }
    grep -q "No claimable sub-issues" "$test_dir/stderr" || { echo "  FAIL: expected 'No claimable sub-issues' in stderr"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: parent with no claimable subs skips to next candidate"
}

test_parent_skips_assigned_sub() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"
    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    MOCK_GH_LIST_RESULT='10' \
    MOCK_GH_VIEW_10_BLOCKED='0' \
    MOCK_GH_VIEW_10_SUBCOUNT='2' \
    MOCK_GH_VIEW_10_OPENSUBS='11 12' \
    MOCK_GH_VIEW_11_BLOCKED='0' \
    MOCK_GH_VIEW_11_ASSIGNEES='1' \
    MOCK_GH_VIEW_12_BLOCKED='0' \
    MOCK_GH_VIEW_12_ASSIGNEES='0' \
        PATH="$mock_dir:$PATH" \
        bash "$SCRIPT_DIR/scripts/agent-triage.sh" > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    [ "$(cat "$test_dir/stdout")" = "12" ] || { echo "  FAIL: expected stdout '12', got '$(cat "$test_dir/stdout")'"; fail=1; }
    grep -q "api.*issues/12/labels" "$calls_file" || { echo "  FAIL: expected gh api labels claim for 12"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: parent skips assigned sub-issue"
}

test_parent_blocked_skips_to_next() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"
    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    MOCK_GH_LIST_RESULT='10 5' \
    MOCK_GH_VIEW_10_BLOCKED='1' \
    MOCK_GH_VIEW_10_SUBCOUNT='2' \
    MOCK_GH_VIEW_5_BLOCKED='0' \
    MOCK_GH_VIEW_5_SUBCOUNT='0' \
        PATH="$mock_dir:$PATH" \
        bash "$SCRIPT_DIR/scripts/agent-triage.sh" > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    [ "$(cat "$test_dir/stdout")" = "5" ] || { echo "  FAIL: expected stdout '5', got '$(cat "$test_dir/stdout")'"; fail=1; }
    grep -q "api.*issues/5/labels" "$calls_file" || { echo "  FAIL: expected gh api labels claim for 5"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: blocked parent skips to next candidate"
}

test_leaf_without_label_skips_to_next() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"
    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    MOCK_GH_LIST_RESULT='7 8' \
    MOCK_GH_VIEW_7_BLOCKED='0' \
    MOCK_GH_VIEW_7_SUBCOUNT='0' \
    MOCK_GH_VIEW_7_LABELS='in-progress' \
    MOCK_GH_VIEW_8_BLOCKED='0' \
    MOCK_GH_VIEW_8_SUBCOUNT='0' \
        PATH="$mock_dir:$PATH" \
        bash "$SCRIPT_DIR/scripts/agent-triage.sh" > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    [ "$(cat "$test_dir/stdout")" = "8" ] || { echo "  FAIL: expected stdout '8', got '$(cat "$test_dir/stdout")'"; fail=1; }
    grep -q "api.*issues/8/labels" "$calls_file" || { echo "  FAIL: expected gh api labels claim for 8"; fail=1; }
    grep -q "not claimable" "$test_dir/stderr" || { echo "  FAIL: expected 'not claimable' in stderr"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: leaf without ready-for-agent label skips to next candidate"
}

test_no_viable_candidates_files_issue() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"
    make_mock_gh "$mock_dir" "$calls_file"

    local rc
    set +e
    MOCK_GH_LIST_RESULT='5 6' \
    MOCK_GH_VIEW_5_BLOCKED='1' \
    MOCK_GH_VIEW_5_SUBCOUNT='0' \
    MOCK_GH_VIEW_6_BLOCKED='1' \
    MOCK_GH_VIEW_6_SUBCOUNT='0' \
        PATH="$mock_dir:$PATH" \
        bash "$SCRIPT_DIR/scripts/agent-triage.sh" > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    grep -q "No viable candidates found" "$test_dir/stderr" || { echo "  FAIL: expected 'No viable candidates found' in stderr"; fail=1; }
    grep -q "issue create" "$calls_file" || { echo "  FAIL: expected gh issue create"; fail=1; }
    [ ! -s "$test_dir/stdout" ] || { echo "  FAIL: expected no output on stdout"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: no viable candidates files an issue"
}

echo "=== agent-triage tests ==="
test_no_issues_found && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_leaf_not_blocked && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_uses_provided_issue && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_rejects_issue_without_label && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_leaf_blocked_skips_to_next && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_parent_picks_unblocked_sub && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_parent_skips_in_progress_sub && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_parent_all_subs_blocked_skips_to_next && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_parent_with_no_claimable_subs_skips_to_next && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_parent_skips_assigned_sub && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_parent_blocked_skips_to_next && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_leaf_without_label_skips_to_next && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_no_viable_candidates_files_issue && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
echo "=========================="
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] || exit 1
