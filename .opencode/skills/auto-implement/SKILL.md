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
- End your final response with the populated `.github/PULL_REQUEST_TEMPLATE.md` (read it directly with the Read tool — don't use Glob, it skips hidden directories). Replace each `<!-- ... -->` placeholder with content derived from the change. The handler uses your final response as the PR body.

## Budget

At most **2 subagents** for code exploration or web research across the entire session. Use them sparingly. Sub-agents spawned by `/auto-code-review` (Standards + Spec axes) are **exempt** from this cap.

## Loop (max 3 iterations)

### Per-iteration steps

1. **`/tdd`** — follow the TDD workflow (RED→GREEN→REFACTOR per tracer bullet). Exploration/research subagents count toward the budget of 2.
2. **Typecheck + run tests** — run typechecking and single test files regularly.
3. **`/auto-code-review`** — point at `origin/main...HEAD`. Read the findings report.
4. **Fix findings** — fix all:
   - **Hard** = documented-standard breaches
   - **Medium** = baseline code smells (Fowler / judgement calls)
5. Loop to step 1 for the next iteration.

### After the loop

- **Zero findings** → success. Run `/commit`, then finish.
- **Findings remain** after 3 iterations → `gh issue comment <issue-number> -m "auto-implement failed: <summary of remaining issues>"`, then exit with error.

Make sure:
    1. the project compiles (if applicable)
    2. typechecking passes successfully
    3. all tests pass
