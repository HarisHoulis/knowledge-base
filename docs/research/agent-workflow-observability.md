# Agent Workflow Observability

Question: what to capture per implemented ticket, and where, so a human can see *why* an implementer agent produced bad code without guessing.

## Findings

### 1. Signals captured per agent attempt

- Anthropic *Building Effective Agents* — transparency is a core principle: "explicitly show the agent's planning steps"; prefer evaluator-optimizer loops over end-to-end judgement. https://www.anthropic.com/engineering/building-effective-agents
- Anthropic *Managed Agents* — a session is an append-only log of everything that happened, durable and externally interrogable, decoupled from the harness/sandbox. https://www.anthropic.com/engineering/managed-agents
- OpenTelemetry GenAI semantic conventions — standard vocabulary: agent spans for `plan`, `execute_tool`, `invoke_workflow`; `gen_ai.conversation.id`, `error.type`. https://github.com/open-telemetry/semantic-conventions-genai
- AgentEval (ACL 2026, arXiv 2604.23581) — per-attempt evaluation as a DAG of steps, typed quality metrics from an LLM judge, hierarchical failure taxonomy, linked to upstream dependencies for root-cause attribution. Step-level evals caught 2.17x more failures than end-to-end.
- SWE-bench (arXiv 2310.06770) + Verified — pass/fail against hidden tests; documents failure classes (wrong abstraction level, hidden-test mismatch, grading faults) and turn/token costs. https://www.anthropic.com/research/swe-bench-sonnet
- Reflexion (arXiv 2303.11366) — agents keep verbal reflections in an episodic memory buffer per trial.

**Signal set**: plan, assumptions, tool calls, per-step quality labels, reflection, outcome vs tests, error class.

### 2. Lightweight persistence in git + GitHub

| Surface | Strengths | Weaknesses |
|---|---|---|
| Issue comments | Native per-ticket record, human narrative | Weak for machine aggregation |
| Markdown ledger (ADR-style) | Versioned, PR-reviewable, durable | Aggregation needs parsing |
| Structured JSON/YAML in repo | Machine-queryable, diff-able | Merge-conflict-prone |

Emerging precedent: Decision Reasoning Format (assumptions as a first-class field); `kgai` append-only machine-readable decision log for AI coding agents. https://github.com/architecture-decision-record/architecture-decision-record

**No dashboard needed** — one ledger entry per ticket keyed by ticket ID, committed with the PR; issue comment as the human-facing surface.

### 3. Failure taxonomy

- AgentEval's 3-level, 21-subcategory hierarchical failure taxonomy with root-cause attribution (validated across tau-bench/SWE-bench) is the closest published rubric.
- AgentBench (arXiv 2308.03688) attributes failures to long-term reasoning, decision-making, instruction-following.
- ASE 2025 empirical taxonomy of five review-comment types classified by LLM-judge (arXiv 2510.05450).

**No published rubric matches our five categories exactly** (bypassed seam / scope creep / wrong implementation / requirement drift / overcomplexity) — genuinely open design space. AgentEval's structure is the pattern to follow: requirement-side vs agent-side root cause.

### 4. Assumption capture

- Nygard ADRs capture context/forces before decisions. http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions
- Decision Reasoning Format makes assumptions a first-class field.
- ISO/IEC/IEEE 29148 treats assumptions as standard requirement artifacts.
- SWE-bench Verified notes many issues are "impossible to solve without additional context", forcing agent inference.
- Anthropic warns harnesses encode assumptions that go stale.

**No authoritative source mandates "implementer emits an assumptions artifact per ticket"** — open design space, consistent with ADR/DRF + Reflexion-style reflection.

## Design implication

Capture per ticket: plan/assumptions (from implementer) + categorized findings (from code-review), persisted to a durable repo ledger and posted to the issue thread. Attribute each finding to a root-cause class so data can confirm or correct the "vague ACs" hypothesis.
