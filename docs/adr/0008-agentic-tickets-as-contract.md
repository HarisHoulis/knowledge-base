# ADR-0008: Agentic tickets are the contract; the spec is the derivation source

We write tickets directly for an autonomous coding agent, not for a human. Each ticket carries behavior-typed Acceptance Criteria at a named Seam, a Bounding Box, and an explicit Never list; the parent spec's State & Seams is the sole structural derivation source and user stories are dropped from the spec template. Chosen because acceptance criteria written as human prose leave room for misinterpretation, and the implementer's silent inference produced wrong seams, out-of-bounds edits, and overcomplicated logic — hardening the ticket format and adding a Pre-flight gate (see `CONTEXT.md` under Agentic Development) closes that gap without complicating the workflow.

## Considered Options

- **Keep user stories + thin ACs** (status quo) — rejected: implementer underperforms; failures only surface at code-review with no feedback loop.
- **Specify implementation directly in tickets** (file paths, code) — rejected: goes stale fast; over-constrains the agent's design space (SlopCodeBench).
- **Behavior-typed ACs + Never list + Pre-flight** (chosen) — the spec names seams and behaviors; the ticket names behaviors, bounds, and verification; the implementer records assumptions it had to fill.

## Consequences

- Specs lose human-readable narrative (User Stories) in favor of agent-facing Behaviors + State & Seams.
- Tickets become the reviewable contract; code-review checks fidelity against the ticket, grounded by the parent spec.
- Findings are persisted to the Findings Ledger, closing the loop between code-review output and future ticket authoring.
