---
name: auto-implement
description: "Build working code from a spec or set of tickets. Use when the user provides a specification to implement, tickets to build out, or requirements to code up."
---

Implement the work described by the user in the spec or tickets.

## CI Mode (headless)

This skill runs in headless CI. Rules:

- Never prompt the user or wait for input — all operations must be autonomous.
- Git auth uses GITHUB_TOKEN (injected by the GitHub Action). Do not rely on SSH or interactive auth.
- Work on the current branch. The opencode GitHub action handler created it and will push it and open the PR after you finish. Do NOT create a new branch and do NOT run `git push`.
- If a handoff file exists in `.handoffs/` (from a prior run), read it to resume the work.
- All commits must use Conventional Commits messages.
- **Workflow changes are proposed, never pushed.** The run token lacks `workflows` permission, so commits touching `.github/workflows/` are blocked by the CI pre-commit hook. If your work requires changing a workflow file, run `bash scripts/suggest-workflow-change.sh <issue-number>`: it writes a Workflow Proposal (unified diff) to `docs/workflow-proposals/` and reverts the workflow files. Commit the proposal with the rest of your work, flag it in the PR body under the template's "Workflow changes" section, and do NOT claim it is applied. For a proposal-only issue, do not write `Closes #N` in the PR body.
- Your final response must be exactly the populated `.github/PULL_REQUEST_TEMPLATE.md` (read it directly with the Read tool — don't use Glob, it skips hidden directories). Replace each `<!-- ... -->` placeholder with content derived from the change, and output nothing else — no commentary, no preamble, no trailing prose. The handler uses your final response as the PR body.

## Budget

At most **2 subagents** for code exploration or web research across the entire session. Use them sparingly. Sub-agents spawned by `/auto-code-review` (Standards + Spec axes) are **exempt** from this cap.

## Pre-flight (mandatory, before any code)

Before writing any code, on the current branch, name the contract in a machine-extractable block for the PR body, with these fixed labels:

- **Seam:** the named seam this ticket implements at (from the ticket's Seam / the spec's State & Seams).
- **Bounds:** the bounding box this work stays inside (the ticket's allow-list).
- **Assumptions:** every design decision the ticket left implicit that you had to fill.
- **Gaps:** anything the ticket or spec doesn't cover that you needed to resolve.

If you cannot name the seam or state the bounds, **stop — do not silently infer**. Headless CI has no HITL channel, so the escalation path is the AFK one only: `gh issue comment <issue-number> -m "needs-info: <what's missing>"`, apply the `needs-info` label, then exit with error. Record every escalation.

## Loop (max 3 iterations)

### Per-iteration steps

1. **`/auto-tdd`** — follow the TDD workflow (RED→GREEN→REFACTOR per tracer bullet). Exploration/research subagents count toward the budget of 2.
2. **Typecheck + run tests** — run typechecking and single test files regularly.
3. **`/auto-code-review`** — point at `origin/main...HEAD`. Read the findings report.
4. **Fix findings** — fix all:
   - **Hard** = documented-standard breaches
   - **Medium** = baseline code smells (Fowler / judgement calls)
5. Loop to step 1 for the next iteration.

### After the loop

- **Zero findings** → success. Run `/auto-commit`, then finish.
- **Findings remain** after 3 iterations → `gh issue comment <issue-number> -m "auto-implement failed: <summary of remaining issues>"`, then exit with error.

Make sure:
    1. the project compiles (if applicable)
    2. typechecking passes successfully
    3. all tests pass
