# ADR 0004: GitHub Actions Scheduled Workflow over Cron / Launchd

The daily pipeline scheduler uses a GitHub Actions workflow (cron trigger) instead of local cron or launchd. State is persisted between runs via `actions/cache` rather than the local filesystem. The workflow creates a per-run feature branch and opens a PR for review instead of pushing directly to main.

Local cron is simpler (zero infra, no cache eviction risk) but requires a persistent machine, local Python environment, and `gh` credentials. GitHub Actions is serverless, pre-authenticated with `GITHUB_TOKEN` (which `_escalate_failure` already relies on), and adds no operational overhead. The trade-off is a 7-day cache eviction window (irrelevant at daily cadence) and a slightly more complex workflow file. If the pipeline cadence ever drops below weekly, Option 1 (commit state.json to the repo) is a trivial fallback.
