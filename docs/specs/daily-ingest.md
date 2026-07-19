# Daily Ingest

## Problem Statement

The knowledge base pipeline curates concepts from 9 trusted sources, but it only runs when manually invoked. Without a scheduled Daily Ingest, new content accumulates unprocessed and the KB falls behind the user's reading. The user must either remember to run the pipeline or accept stale entries.

## Solution

A scheduled GitHub Actions workflow runs the pipeline at 06:00 UTC daily, creates a feature branch with any new concept files, and opens a pull request for review. State (processed URL hashes) persists between runs via `actions/cache`. If the pipeline produces no changes, no branch or PR is created. Audit exhaustion continues to create a GitHub issue via the existing escalation mechanism.

## User Stories

1. As a knowledge worker, I want the pipeline to run automatically at 06:00 UTC daily, so that new content is ingested without manual triggers.
2. As a knowledge worker, I want processed-URL state to persist between runs on ephemeral runners, so that already-ingested entries are not re-processed each day.
3. As a reviewer, I want new concepts to land in a pull request rather than being pushed directly to main, so that I can review and merge at my own pace.
4. As a reviewer, I want each daily run to create its own branch (`daily-ingest/YYYY-MM-DD`), so that concurrent unmerged PRs don't collide.
5. As a reviewer, I want the workflow to skip creating a branch or PR entirely when there are no new concepts (clean `git status`), so that I don't see empty pull requests.
6. As a knowledge worker, I want audit escalation (exhausted retries) to create a GitHub issue, so that I can investigate failures without monitoring logs.
7. As an operator, I want to trigger the workflow manually via `workflow_dispatch`, so that I can run an ad-hoc ingest without waiting for the schedule.
8. As a knowledge worker, I want the `--dry-run` flag available via workflow inputs, so that I can preview what a run would produce without writing anything.
9. As a knowledge worker, I want the `--limit=N` flag available via workflow inputs, so that I can cap per-source processing during manual testing.
10. As an operator, I want the workflow to log stdout/stderr to a known location in the Actions UI, so that I can inspect run output.
11. As a developer, I want the git/PR orchestration logic extracted into a shell script, so that it can be tested independently of GitHub Actions.
12. As an operator, I want the workflow to use the existing `GITHUB_TOKEN` for all git and `gh` operations, so that no additional credential management is needed.

## Implementation Decisions

- **Trigger**: `schedule` (cron: `0 6 * * *`, 06:00 UTC) plus `workflow_dispatch` with optional `dry_run` and `limit` inputs.
- **State persistence**: `actions/cache@v4` with a static key (`kb-state-v1`) storing `~/.kb-pipeline/state.json`. Restore at start, save at end (even on failure via `if: always()`).
- **Credentials**: `DEEPSEEK_API_KEY` stored as a GitHub Actions secret. The existing `config.py` reads it from the environment.
- **Wrapper script**: `scripts/daily-ingest.sh` — idempotent shell script that runs `python -m kb_pipeline`, checks `git status --porcelain`, and either creates a branch+PR or exits cleanly. The workflow calls this script.
- **Branch naming**: `daily-ingest/YYYY-MM-DD` derived from the run date. Created only when `git status --porcelain` is non-empty after the pipeline run.
- **PR creation**: Via `gh pr create --fill --base main` on the new branch. The PR body includes the run date and a summary of domains touched (derived from `git diff --stat`).
- **Empty run**: After the pipeline exits, if `git status --porcelain` is empty, the script exits 0 with no further action.
- **Merge strategy**: Squash merge via the PR UI. The workflow does not auto-merge.
- **Escalation**: Unchanged — `_escalate_failure` in `pipeline.py` already calls `gh issue create` with `GITHUB_TOKEN`. Works without modification on GH Actions runners.
- **Python setup**: `actions/setup-python@v5` with pip caching. Dependencies installed via `pip install -e ".[dev]"`.
- **Runner**: `ubuntu-latest`.

## Testing Decisions

- **Seam**: The shell script `scripts/daily-ingest.sh` is the testable unit. It encapsulates all git/PR orchestration logic that previously existed only in the cron wrapper.
- **Test approach**: A test that creates a temporary git repo, runs the script with a controlled "pipeline output" (a fixture set of files), and asserts the correct branch is created, the correct files are committed, and a PR is opened (or skipped when clean). The test mocks `gh` or runs in a context where `gh` is not needed, focusing on the git operations.
- **What makes a good test**: Tests verify the script's behavior at three points — dirty repo after pipeline (branch+PR created), clean repo after pipeline (exit 0, no branch), and pipeline failure (no branch, no PR, non-zero exit forwarded).
- **What NOT to test**: The pipeline itself (already tested in `tests/test_pipeline.py`). The workflow YAML syntax (validated by GH Actions on push). Cache restore/save (Actions infrastructure).
- **Prior art**: The existing integration tests use fixture data and assert behavior without mocking the LLM. The script test follows the same pattern — fixture git repo, assert observable behavior.
- **Modules tested**: `scripts/daily-ingest.sh` (new). No pipeline code is modified.

## Out of Scope

- Multi-user / team sharing
- Web UI for the KB
- Vector DB / semantic search
- Backfill of historical content
- Migration of existing `state.json` from local filesystem (cold start on first GH Actions run is acceptable — it re-processes all entries once)

## Further Notes

- First run on GH Actions will cold-start the cache and re-process all existing RSS entries. This is identical to the first local run behavior.
- If the pipeline cadence ever drops below weekly, the `actions/cache` eviction window (7 days) becomes a risk. At that point, switch to committing `state.json` to the repo (Option 1 in the research doc). The change is limited to the workflow file — no pipeline code changes needed.
- The `scripts/daily-ingest.sh` script should be `set -euo pipefail` for safety and work correctly when run locally (not just in Actions) so the user can invoke it manually for testing.
