# Agent Triage: Silent Exit When No Claimable Work

## Goal

When the agent-triage workflow finds no issues to implement, it should exit
silently — no GitHub issue opened. Today the "no viable candidates" branch in
`scripts/agent-triage.sh` files a `needs-triage` issue ("Agent Triage: No viable
candidates found", e.g. #118).

## Facts

- The YAML never opens an issue; `agent-triage.yml`'s "Mark failed" step only
  runs on `failure()`. The issue is opened by `scripts/agent-triage.sh:89-99`.
- Two no-work paths exist:
  - No `ready-for-agent` issues at all (agent-triage.sh:34) — already silent.
  - Candidates exist but none claimable (agent-triage.sh:87-101) — opens the issue.
- Only one test asserts the issue-creation behavior:
  `test_no_viable_candidates_files_issue` (tests/test_agent_triage.sh:504).
- Removed behavior misapplied the `needs-triage` label (defined as "agent failed
  to implement") to a non-failure, so removing it makes CONTEXT.md more accurate.
  No docs describe the removed behavior.

## Decisions (grilled)

- Full silence accepted: the daily cron made the "systemic bottleneck" alarm
  noise; the stderr log preserves the trace for auditing runs.
- No CONTEXT.md edit: no new concept introduced; glossary never documented the
  removed behavior.
- Surgical scope: YAML, CONTEXT.md, and `agent-triage-postprocess.sh` unchanged.

## Changes

### 1. `scripts/agent-triage.sh`

Replace the `if [ -z "$SELECTED" ]` branch (lines 87-101) with:

```bash
if [ -z "$SELECTED" ]; then
    echo "[agent-triage] No viable candidates found after scanning all issues." >&2
    exit 0
fi
```

Drops only the `gh issue create` block; keeps the stderr log and `exit 0`.

### 2. `tests/test_agent_triage.sh`

Invert `test_no_viable_candidates_files_issue` (lines 504-531): assert exit 0,
"No viable candidates found" in stderr, empty stdout, and **no** `issue create`
in the mock calls file. Rename to `test_no_viable_candidates_exits_silently`,
update its PASS message (line 530) and registration (line 547).

## Success Criteria

- `bash tests/test_agent_triage.sh` passes with the renamed/inverted test green
  and all other agent-triage unit tests still passing.
- `gh issue create` no longer appears anywhere in `scripts/agent-triage.sh`.
