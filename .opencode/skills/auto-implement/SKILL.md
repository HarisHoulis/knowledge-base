---
name: auto-implement
description: "Build working code from a spec or set of tickets. Use when the user provides a specification to implement, tickets to build out, or requirements to code up."
---

Implement the work described by the user in the spec or tickets.

Before any code change, switch from origin/main to a new branch.

Run existing tests to establish the starting baseline.

Implement the solution, running typechecking and single test files regularly to catch regressions early.

When the work requires code exploration or searching the web, launch subagents to do that work.

Make sure:
    1. the project compiles (if applicable)
    2. typechecking passes successfully
    3. all tests pass

Commit your work to the current branch.
