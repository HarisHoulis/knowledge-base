# Agentic Execution (Guidelines)

Agentic execution rules govern how an agent runs ticket work: what it may read, how much it may change, and what context it carries. They are **guidelines**, reviewed per-diff rather than enforced mechanically.

1. **Ticket fidelity** — Honor the ticket's bounding box as a hard ceiling. Read only the allowed dependencies; create/modify only within the allow-list.
   - *Rationale:* The ticket's allow-list is the agreed scope; touching anything outside it produces unrequested, unreviewable change.

2. **Size cap** — Keep ~200 lines soft / ~400 hard per ticket. If a vertical slice exceeds it, split it further vertically.
   - *Rationale:* A ticket above the cap outgrows what one fresh context can hold and review cleanly; splitting keeps each slice self-contained.

3. **Fresh context** — One ticket per fresh context. Attach only self-sufficient inputs (ticket, `CONTEXT.md`, relevant ADRs, the parent spec's State & Seams); clear context between tickets.
   - *Rationale:* Carrying one ticket's state into the next leaks decisions and dependencies that make the later ticket's work wrong.

4. **No speculative generality** — Delete unrequested abstraction. Surgical diffs only; touch nothing the ticket doesn't ask for.
   - *Rationale:* Abstraction added for needs the ticket doesn't have is dead weight every future reader must pay for; surgical diffs keep review honest.
