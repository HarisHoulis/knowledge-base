## Agent skills

### Issue tracker

Issues live in this repo's GitHub Issues, managed via the `gh` CLI. See `docs/agents/issue-tracker.md`.

### Domain docs

Single-context layout — root `CONTEXT.md` + ADRs in `docs/adr/`. See `docs/agents/domain.md`.

### Testing

1. Injectable callables for deterministic unit tests; integration tests gated by marker and excluded from default runs. See `docs/agents testing.md`. 
2. Do not run integration tests automatically. Stop and notify the user which command to run.
