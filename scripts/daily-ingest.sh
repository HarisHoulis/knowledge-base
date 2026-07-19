#!/usr/bin/env bash
set -euo pipefail

DRY_RUN=false
PIPELINE_ARGS=()

while [[ $# -gt 0 ]]; do
    case "$1" in
        --dry-run)
            DRY_RUN=true
            PIPELINE_ARGS+=("--dry-run")
            shift
            ;;
        --limit=*)
            PIPELINE_ARGS+=("$1")
            shift
            ;;
        *)
            echo "[daily-ingest] Unknown option: $1" >&2
            exit 1
            ;;
    esac
done

PYTHON="${PYTHON:-$(command -v python3 || command -v python)}"
GH="${GH:-gh}"

KB_PATH="${KB_PATH:-$(pwd)}"
KB_STATE="${KB_STATE:-$HOME/.kb-pipeline/state.json}"
export KB_PATH KB_STATE

cd "$KB_PATH"

echo "[daily-ingest] KB_PATH=$KB_PATH"
echo "[daily-ingest] KB_STATE=$KB_STATE"
echo "[daily-ingest] DRY_RUN=$DRY_RUN"
echo "[daily-ingest] Starting pipeline..."

rc=0
$PYTHON -m kb_pipeline ${PIPELINE_ARGS[@]+"${PIPELINE_ARGS[@]}"} || rc=$?
if [ "$rc" -ne 0 ]; then
    echo "[daily-ingest] Pipeline failed with exit code $rc" >&2
    exit $rc
fi

if ! git status --porcelain | grep -q .; then
    echo "[daily-ingest] No changes detected. Exiting."
    exit 0
fi

if [ "$DRY_RUN" = true ]; then
    echo "[daily-ingest] Dry run: changes detected but not committing or pushing."
    echo "[daily-ingest] Changed files:"
    git status --porcelain
    exit 0
fi

BRANCH="daily-ingest/$(date +%Y-%m-%d)"
echo "[daily-ingest] Creating branch $BRANCH..."
git checkout -B "$BRANCH"
git add -A

STAT=$(git diff --stat --cached)
git commit -m "feat(ingest): daily ingest $(date +%Y-%m-%d)" -m "$STAT"

echo "[daily-ingest] Pushing branch $BRANCH..."
git push origin "$BRANCH"

echo "[daily-ingest] Creating pull request..."
$GH pr create --fill --base main

echo "[daily-ingest] Done."
