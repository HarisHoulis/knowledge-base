#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PASS=0
FAIL=0

PY=python

test_bare_python_fails() {
    local dir; dir=$(mktemp -d)
    mkdir -p "$dir/scripts"
    cat > "$dir/scripts/bad.sh" <<EOF
#!/usr/bin/env bash
${PY} -m pip install requests
EOF
    local rc
    set +e
    bash "$SCRIPT_DIR/scripts/check-rules.sh" "$dir" > "$dir/output" 2>&1
    rc=$?
    set -e
    rm -rf "$dir"
    [ "$rc" -ne 0 ] || { echo "FAIL: bare-${PY} — expected nonzero, got $rc"; return 1; }
    echo "PASS: bare-${PY} fails the check"
}

test_python3_only_passes() {
    local dir; dir=$(mktemp -d)
    mkdir -p "$dir/scripts"
    cat > "$dir/scripts/ok.sh" <<EOF
#!/usr/bin/env bash
python3 -m pytest
EOF
    local rc
    set +e
    bash "$SCRIPT_DIR/scripts/check-rules.sh" "$dir" > "$dir/output" 2>&1
    rc=$?
    set -e
    rm -rf "$dir"
    [ "$rc" -eq 0 ] || { echo "FAIL: python3 only — expected 0, got $rc"; return 1; }
    echo "PASS: python3 only passes the check"
}

test_dangling_reference_fails() {
    local dir; dir=$(mktemp -d)
    cat > "$dir/AGENTS.md" <<EOF
## External File Loading
@docs/agents/missing.md
## Global Engineering Standards
EOF
    local rc
    set +e
    bash "$SCRIPT_DIR/scripts/check-rules.sh" "$dir" > "$dir/output" 2>&1
    rc=$?
    set -e
    rm -rf "$dir"
    [ "$rc" -ne 0 ] || { echo "FAIL: dangling @reference — expected nonzero, got $rc"; return 1; }
    echo "PASS: dangling @reference fails the check"
}

test_valid_references_pass() {
    local dir; dir=$(mktemp -d)
    mkdir -p "$dir/docs/agents"
    echo "# ok" > "$dir/docs/agents/ok.md"
    cat > "$dir/AGENTS.md" <<EOF
## External File Loading
@docs/agents/ok.md
## Global Engineering Standards
EOF
    local rc
    set +e
    bash "$SCRIPT_DIR/scripts/check-rules.sh" "$dir" > "$dir/output" 2>&1
    rc=$?
    set -e
    rm -rf "$dir"
    [ "$rc" -eq 0 ] || { echo "FAIL: valid @references — expected 0, got $rc"; return 1; }
    echo "PASS: valid @references pass the check"
}

echo "=== check-rules tests ==="
test_bare_python_fails && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_python3_only_passes && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_dangling_reference_fails && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
test_valid_references_pass && PASS=$((PASS+1)) || FAIL=$((FAIL+1))
echo "======================"
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] || exit 1
