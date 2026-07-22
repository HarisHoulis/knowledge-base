---
name: commit
description: Draft and commit changes following Conventional Commits. Use when the user mentions committing, staging, making a commit, or asks you to commit changes.
---

# Commit

## 1. Survey

Run `git status`, `git diff`, `git diff --cached`. If nothing to commit, stop.

Completion criterion: full inventory shown.

## 2. Draft

Map the change to a Conventional Commits type:

- `feat` — new feature
- `fix` — bug fix
- `chore` — maintenance, config, deps, tooling
- `refactor` — internal restructuring
- `docs` — documentation-only
- `style` — formatting, lint
- `perf` — performance
- `test` — tests

Scope is the affected module, one or two words — optional.

Propose `<type>(<scope>): <summary>`. Show the user; accept edits. If the type is obvious (added code = `feat`, typo fix = `docs`), skip the prompt and commit.

Completion criterion: message confirmed (explicitly or by skipping).

## 3. Commit

`git add -A && git commit -m "<message>"`

Completion criterion: commit succeeds.
