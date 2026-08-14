# Design Rules (Guidelines)

Design rules are **guidelines**: choices within a module that are cheap to adjust and local in effect. Unlike architectural constraints, they steer rather than bind; each still carries its rationale.

1. **Composite use-cases** — Orchestrate small single-purpose use-cases; no monoliths.
   - *Rationale:* A monolithic use-case entangles responsibilities and can only be reused wholesale; composed single-purpose pieces stay readable, testable, and reorderable.

2. **Small complexity, small mental overhead** — Write the minimum code for the exact problem; match the surrounding patterns.
   - *Rationale:* Every extra line and novel pattern is a cost paid by every future reader; the smallest correct solution minimises that recurring tax.

3. **High cohesion, low coupling** — Apply cohesion and coupling at the implementation level, not just the architecture level.
   - *Rationale:* Cohesion keeps related behaviour together so a change is local; low coupling keeps a module's changes from leaking into its callers.

4. **Reusable + autonomous components** (Ch. 8) — Question modules that are neither reusable nor autonomous.
   - *Rationale:* A module that is neither reusable nor autonomous is dead weight — it must be understood but serves only one caller (Ch. 8); making it one or the other repays the effort.

5. **Prefer weaker connascence** (Ch. 3) — Prefer static over dynamic coupling; name > type > meaning > position > algorithm.
   - *Rationale:* Stronger connascence (dynamic, position/algorithm) fails at runtime or requires disciplined ordering; weaker connascence fails at compile time, where it is caught early (Ch. 3).

6. **Structural decay alert** — A change that degrades a required characteristic (performance, testability, modularity) is a design violation.
   - *Rationale:* Required characteristics are the contract of the module; a change that erodes one is a defect regardless of the local logic's correctness.
