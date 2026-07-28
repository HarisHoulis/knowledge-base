---
name: auto-push
description: Ship finished work: commit, push, and open a PR. Use when work is done and ready to ship, when the user wants to commit and push, publish changes, open a pull request, or wrap up a session.
---

# Push

## 1. Commit

Run the `commit` skill.

Completion criterion: commit succeeds.

## 2. Push

`git push`

On non-fast-forward: `git pull --rebase && git push`

Completion criterion: remote confirms the push.

## 3. PR

`gh pr view` to check if a PR exists for this branch.

If none exists, create one:

1. Read `.github/PULL_REQUEST_TEMPLATE.md` directly with the Read tool (don't use Glob — it skips hidden directories). If the file doesn't exist, skip template handling.
2. For each `<!-- ... -->` placeholder in the template, replace it with content derived from `git log` (since the base branch) or the diff.
3. Create the PR with: `gh pr create --title "..." --body "$body"` (do NOT use `--fill`).
4. Verify: `gh pr view --json body` and confirm the body includes the filled-out template (not empty, not a fallback).

**Failure mode**: If the template exists but the PR body does not contain its filled-out structure, mark the step as failed.

Completion criterion: PR exists on the remote with a body derived from the template.