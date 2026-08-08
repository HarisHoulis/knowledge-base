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

if [ "$1" = "issue" ] && [ "$2" = "view" ]; then
    echo "${MOCK_GH_ISSUE_TITLE:-Untitled issue}"
    exit 0
fi

if [ "$1" = "pr" ] && [ "$2" = "list" ]; then
    JQ_EXPR=$(printf '%s' "$*" | sed 's/^.*--jq //')
    echo "${MOCK_GH_PR_LIST:-[]}" | jq -r "$JQ_EXPR"
    exit 0
fi

if [ "$1" = "pr" ] && [ "$2" = "view" ]; then
    case "$*" in
        *"--json headRefName"*) echo "${MOCK_GH_PR_HEAD:-opencode/dispatch-abc123-20260731145348}"; exit 0;;
        *"--json body"*) printf '%s' "${MOCK_GH_PR_BODY:-}"; exit 0;;
    esac
    exit 0
fi

if [ "$1" = "pr" ] && [ "$2" = "edit" ]; then
    if [ -n "${MOCK_GH_EDIT_OUT:-}" ]; then
        while [ $# -gt 0 ]; do
            if [ "$1" = "--body-file" ]; then
                cat "$2" > "$MOCK_GH_EDIT_OUT"
            fi
            shift
        done
    fi
    exit 0
fi

echo "gh: unrecognized invocation: $*" >&2
exit 1
MOCKEOF
    finalize_mock "$mock_dir/gh" "$calls_file"
}

make_mock_git() {
    local mock_dir="$1"
    local calls_file="$2"
    cat > "$mock_dir/git" << 'MOCKEOF'
#!/usr/bin/env bash
echo "git $*" >> "CF"
case "$1" in
    fetch|checkout|push) exit 0;;
esac
echo "git: unrecognized invocation: $*" >&2
exit 1
MOCKEOF
    finalize_mock "$mock_dir/git" "$calls_file"
}

finalize_mock() {
    local mock_file="$1"
    local calls_file="$2"
    sed "s|CF|$calls_file|g" "$mock_file" > "$mock_file.tmp"
    mv "$mock_file.tmp" "$mock_file"
    chmod +x "$mock_file"
}

source "$SCRIPT_DIR/scripts/agent-triage-postprocess.sh"

test_slugify() {
    local fail=0
    local got
    got=$(slugify "Proposes adding BYTEBYTEGO_SUBSTACK_COOKIE to daily-ingest CI env.")
    [ "$got" = "proposes-adding-bytebytego-substack" ] || { echo "  FAIL: long title slug '$got'"; fail=1; }
    got=$(slugify "Add TDD loop to auto-implement (issue #89)")
    [ "$got" = "add-tdd-loop-to-auto-implement-issue-89" ] || { echo "  FAIL: punctuated title slug '$got'"; fail=1; }
    got=$(slugify "Fix: daily-ingest 20-minute timeout!")
    [ "$got" = "fix-daily-ingest-20-minute-timeout" ] || { echo "  FAIL: trailing punct slug '$got'"; fail=1; }
    got=$(slugify "")
    [ "$got" = "" ] || { echo "  FAIL: empty title slug '$got'"; fail=1; }
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: slugify"
}

test_strip_footer() {
    local body got
    body=$'## Summary\n\nAdds the cookie.\n\n## Notes\n\nDone.\n\nTriggered by workflow_dispatch\n\n<a href="https://opencode.ai/s/abc123"><img width="200" /></a>\n[opencode session](https://opencode.ai/s/abc123)&nbsp;&nbsp;|&nbsp;&nbsp;[github run](/HarisHoulis/knowledge-base/actions/runs/1)'
    got=$(printf '%s' "$body" | strip_footer)
    echo "$got" | grep -q "## Summary" || { echo "  FAIL: template header lost"; return 1; }
    echo "$got" | grep -q "^Done\.$" || { echo "  FAIL: template tail lost"; return 1; }
    echo "$got" | grep -q "Triggered by" && { echo "  FAIL: footer marker leaked"; return 1; }
    echo "$got" | grep -q "github run" && { echo "  FAIL: footer link leaked"; return 1; }

    got=$(printf '%s' $'## Summary\n\nPlain body without footer.' | strip_footer)
    echo "$got" | grep -q "Plain body without footer." || { echo "  FAIL: passthrough lost content"; return 1; }
    echo "PASS: strip_footer"
}

test_find_agent_pr() {
    local test_dir mock_dir calls_file got
    test_dir=$(mktemp -d)
    mock_dir="$test_dir/mocks"
    calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"
    make_mock_gh "$mock_dir" "$calls_file"
    make_mock_git "$mock_dir" "$calls_file"

    got=$(ISSUE_NUMBER=37 \
        MOCK_GH_PR_LIST='[{"number":10,"headRefName":"opencode/schedule-aaa-20260101010101","createdAt":"2026-01-01T01:01:01Z","body":"## Related issues\n\n#37"},{"number":11,"headRefName":"opencode/dispatch-bbb-20260101010102","createdAt":"2026-01-01T01:01:02Z","body":"## Related issues\n\n#99"},{"number":12,"headRefName":"other/feature","createdAt":"2026-01-01T01:01:03Z","body":"## Related issues\n\n#37"}]' \
        PATH="$mock_dir:$PATH" \
        find_agent_pr)
    [ "$got" = "10" ] || { echo "  FAIL: expected newest matching agent PR 10, got '$got'"; rm -rf "$test_dir"; return 1; }

    got=$(ISSUE_NUMBER=37 \
        MOCK_GH_PR_LIST='[{"number":13,"headRefName":"opencode/dispatch-ccc-20260101010104","createdAt":"2026-01-01T01:01:04Z","body":"## Related issues\n\n#370"}]' \
        PATH="$mock_dir:$PATH" \
        find_agent_pr)
    [ -z "$got" ] || { echo "  FAIL: expected empty for #370 with issue 37, got '$got'"; rm -rf "$test_dir"; return 1; }

    got=$(ISSUE_NUMBER=37 \
        MOCK_GH_PR_LIST='[{"number":14,"headRefName":"opencode/dispatch-ddd-20260101010105","createdAt":"2026-01-01T01:01:05Z","body":"## Related issues\n\n#99"}]' \
        PATH="$mock_dir:$PATH" \
        find_agent_pr)
    [ -z "$got" ] || { echo "  FAIL: expected empty for unrelated agent PR, got '$got'"; rm -rf "$test_dir"; return 1; }

    rm -rf "$test_dir"
    echo "PASS: find_agent_pr selects newest agent PR for the issue"
}

test_flow_no_pr() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"
    make_mock_gh "$mock_dir" "$calls_file"
    make_mock_git "$mock_dir" "$calls_file"

    local rc
    set +e
    MOCK_GH_PR_LIST='[]' \
        PATH="$mock_dir:$PATH" \
        bash "$SCRIPT_DIR/scripts/agent-triage-postprocess.sh" 37 > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    grep -q "nothing to clean" "$test_dir/stderr" || { echo "  FAIL: expected 'nothing to clean' in stderr"; fail=1; }
    grep -q "git " "$calls_file" && { echo "  FAIL: git called when no PR found"; fail=1; }
    grep -q "issue view" "$calls_file" && { echo "  FAIL: issue title fetched when no PR found"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: no PR found exits cleanly"
}

test_flow_cleans_and_renames() {
    local test_dir; test_dir=$(mktemp -d)
    local mock_dir="$test_dir/mocks"
    local calls_file="$test_dir/gh_calls"
    local edit_out="$test_dir/edit_body"
    mkdir -p "$mock_dir"
    make_mock_gh "$mock_dir" "$calls_file"
    make_mock_git "$mock_dir" "$calls_file"

    local body
    body=$'## Summary\n\nAdds the cookie.\n\n## Notes\n\nDone.\n\nTriggered by workflow_dispatch\n\n[opencode session](https://opencode.ai/s/abc123)&nbsp;&nbsp;|&nbsp;&nbsp;[github run](/HarisHoulis/knowledge-base/actions/runs/1)'

    local rc
    set +e
    MOCK_GH_ISSUE_TITLE="Proposes adding BYTEBYTEGO_SUBSTACK_COOKIE to daily-ingest CI env." \
    MOCK_GH_PR_LIST='[{"number":84,"headRefName":"opencode/dispatch-abc123-20260731145348","createdAt":"2026-07-31T14:55:43Z","body":"## Related issues\n\n#37"}]' \
    MOCK_GH_PR_HEAD="opencode/dispatch-abc123-20260731145348" \
    MOCK_GH_PR_BODY="$body" \
    MOCK_GH_EDIT_OUT="$edit_out" \
        PATH="$mock_dir:$PATH" \
        bash "$SCRIPT_DIR/scripts/agent-triage-postprocess.sh" 37 > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    local fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    grep -q "gh pr edit 84" "$calls_file" || { echo "  FAIL: expected gh pr edit 84"; fail=1; }
    grep -q "git fetch origin opencode/dispatch-abc123-20260731145348" "$calls_file" || { echo "  FAIL: expected git fetch of old branch"; fail=1; }
    grep -q "git checkout -b issue/37-proposes-adding-bytebytego-substack origin/opencode/dispatch-abc123-20260731145348" "$calls_file" || { echo "  FAIL: expected checkout of new branch"; fail=1; }
    grep -q "git push -u origin issue/37-proposes-adding-bytebytego-substack" "$calls_file" || { echo "  FAIL: expected push of new branch"; fail=1; }
    grep -q "git push origin :opencode/dispatch-abc123-20260731145348" "$calls_file" || { echo "  FAIL: expected delete of old branch"; fail=1; }
    [ -f "$edit_out" ] || { echo "  FAIL: PR body edit file not written"; fail=1; }
    grep -q "## Summary" "$edit_out" || { echo "  FAIL: edited body missing template"; fail=1; }
    grep -q "Triggered by" "$edit_out" && { echo "  FAIL: edited body still has footer"; fail=1; }
    grep -q "github run" "$edit_out" && { echo "  FAIL: edited body still has run link"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: cleans PR body and renames branch"
}

test_flow_skips_unrelated_pr() {
    local test_dir mock_dir calls_file rc fail
    test_dir=$(mktemp -d)
    mock_dir="$test_dir/mocks"
    calls_file="$test_dir/gh_calls"
    mkdir -p "$mock_dir"
    make_mock_gh "$mock_dir" "$calls_file"
    make_mock_git "$mock_dir" "$calls_file"

    set +e
    MOCK_GH_PR_LIST='[{"number":84,"headRefName":"opencode/dispatch-abc123-20260731145348","createdAt":"2026-07-31T14:55:43Z","body":"## Related issues\n\n#99"}]' \
        PATH="$mock_dir:$PATH" \
        bash "$SCRIPT_DIR/scripts/agent-triage-postprocess.sh" 37 > "$test_dir/stdout" 2> "$test_dir/stderr"
    rc=$?
    set -e

    fail=0
    [ "$rc" -eq 0 ] || { echo "  FAIL: expected exit 0, got $rc"; fail=1; }
    grep -q "nothing to clean" "$test_dir/stderr" || { echo "  FAIL: expected 'nothing to clean' in stderr"; fail=1; }
    grep -q "git " "$calls_file" && { echo "  FAIL: git called for unrelated PR"; fail=1; }
    grep -q "gh pr edit" "$calls_file" && { echo "  FAIL: pr edit called for unrelated PR"; fail=1; }
    rm -rf "$test_dir"
    [ "$fail" -eq 0 ] || return 1
    echo "PASS: skips agent PR for a different issue"
}

echo "=== agent-triage post-process tests ==="
test_slugify && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_strip_footer && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_find_agent_pr && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_flow_no_pr && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_flow_skips_unrelated_pr && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_flow_cleans_and_renames && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
echo "================================"
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] || exit 1
