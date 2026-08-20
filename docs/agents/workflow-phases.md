# Workflow Phases (Guidelines)

The agentic development workflow is a six-phase sequence: **Discovery → Spec → Tickets → Execute → Open PR → Verify**. It is a **phase model**, not an orchestrator — a naming layer over the existing skills, with no new machinery or hard gates (ADR-0002). Each phase names the skill that already does the work; the phases document *when* to use it, not how.

| Phase | Name | Skill |
| --- | --- | --- |
| 0 | Discovery | `/grill-with-docs` (+ `explore` subagent for codebase context) |
| 1 | Spec | `/to-spec` — State & Seams + Behaviors + Testing Decisions |
| 2 | Tickets | `/to-tickets` |
| 3 | Execute | `/implement` — test-backed, explicit steps, Pre-flight |
| 4 | Open PR | `/push` |
| 5 | Verify | `/code-review` — feeds the Findings Ledger |

The phases are numbered in authoring order. In **execution**, Verify runs immediately before Open PR — `/code-review` runs on the branch before `/push` opens the PR. `/triage` sits **outside** the model: it is the upstream gate for issues and PRs, not Phase 0. Issues enter the workflow only after triage marks them claimable.

## Boundary decisions

- **Verify-then-merge** — `/code-review` (Verify) runs *before* `/push` (Open PR), even though Open PR is numbered earlier. The review feeds the Findings Ledger and its findings are resolved before the PR ships.
- **Triage is a gate, not a phase** — `/triage` decides whether an issue is claimable; it never produces spec or implementation work.
- **No orchestrator** — the phases invoke existing skills in sequence. Nothing auto-chains them; nothing gates a phase on a prior phase's formal artifact beyond what the skills already require.
