---
name: auto-implement
description: "Build working code from a spec or set of tickets. Use when the user provides a specification to implement, tickets to build out, or requirements to code up."
---

Implement the work described by the user in the spec or tickets.

## CI Mode (headless)

This skill runs in headless CI. Rules:

- Never prompt the user or wait for input — all operations must be autonomous.
- Git auth uses GITHUB_TOKEN (injected by the GitHub Action). Do not rely on SSH or interactive auth.
- Branch name format: `agent/<issue-number>-<short-kebab-title>`.
- Before branching: check if the branch already exists on `origin` (from a prior handoff). If yes, switch to it and resume. Otherwise branch from `origin/main`.
- All commits must use Conventional Commits messages.

## Implementation

Run existing tests to establish the starting baseline.

Implement the solution, running typechecking and single test files regularly to catch regressions early.

When the work requires code exploration or searching the web, launch subagents to do that work.

Make sure:
    1. the project compiles (if applicable)
    2. typechecking passes successfully
    3. all tests pass

Commit your work to the current branch.
