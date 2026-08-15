# Plan Execution (Guidelines)

Plan execution rules govern how an agent approaches multi-step tasks before touching files or running terminal commands. They are **guidelines**, reviewed per-diff rather than enforced mechanically.

Before editing files or running terminal commands for multi-step tasks:

1. **State assumptions** — State your assumptions explicitly. If multiple paths exist, list them—do not choose silently.
   - *Rationale:* Unstated assumptions and silent path choices are where work diverges from intent; making them explicit invites correction early.

2. **Plan with success criteria** — Formulate a step-by-step implementation plan with explicit success criteria for each step.
   - *Rationale:* A step without a success criterion is unverifiable; checking each step against its criterion catches drift where it happens.

3. **Verifiable goals** — Transform tasks into verifiable goals (e.g., "Fix bug" → "Write test reproducing it, then make it pass").
   - *Rationale:* A verifiable goal turns an ambiguous ask into a pass/fail test the agent can check itself.

4. **Halt and re-verify on failure** — Execute sequentially. If a step fails or compiles with errors, halt execution, isolate the failure, and re-verify your plan before looping tools.
   - *Rationale:* Plowing through a failing step compounds the error; halting and re-verifying the plan keeps recovery deliberate rather than recursive.
