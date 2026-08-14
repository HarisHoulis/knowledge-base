#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-$(cd "$(dirname "$0")/.." && pwd)}"
FAIL=0

# 1. Bare-python scan (python-rules #1): flag `python` used as a command token
#    in executable/config text. `\bpython\b` alone is too broad — it would flag
#    the rules' own prose and hyphenated identifiers like `python-version`,
#    `setup-python@v5`, and `requires-python`. Prose docs under `docs/` are
#    excluded: the rules themselves and fenced snippets describe bare `python`
#    without invoking it.
for path in scripts tests .github/workflows AGENTS.md pyproject.toml; do
    [ -e "$ROOT/$path" ] || continue
    matches="$(grep -rnHE '(^|[;&|(]|[[:space:]])python([[:space:])\]|$)' "$ROOT/$path" 2>/dev/null || true)"
    if [ -n "$matches" ]; then
        printf 'bare python: %s\n' "$matches"
        FAIL=1
    fi
done

# 2. AGENTS.md @reference resolution: every @path under the External File
#    Loading block must resolve to an existing file.
if [ -f "$ROOT/AGENTS.md" ]; then
    block="$(sed -n '/^## External File Loading/,/^## Global Engineering Standards/p' "$ROOT/AGENTS.md")"
    refs="$(printf '%s\n' "$block" | grep -oE '@[A-Za-z0-9_./-]+' | tr -d '@' || true)"
    if [ -n "$refs" ]; then
        while IFS= read -r ref; do
            [ -e "$ROOT/$ref" ] || { printf 'missing AGENTS.md reference: %s\n' "$ref"; FAIL=1; }
        done <<< "$refs"
    fi
fi

exit "$FAIL"
