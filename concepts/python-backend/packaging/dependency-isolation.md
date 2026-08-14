---
domain: python-backend
subdomain: packaging
concept: dependency-isolation
title: sqlite-utils 4.2.1
sources:
  - title: "sqlite-utils 4.2.1"
    url: "https://simonwillison.net/2026/Aug/13/sqlite-utils-2/"
    author: "Simon Willison"
    date: "2026-08-13"
---

# sqlite-utils 4.2.1

sqlite-utils 4.2.1 fixes a crashing bug introduced in 4.2 where the code imported `Self` from `typing_extensions`, but that package was not declared as a dependency. It was only present indirectly through dev dependencies, so direct invocation via `uvx sqlite-utils` would fail. The fix adds the missing dependency and establishes a smoke test to catch similar issues in the future.

- The crash was caused by importing `Self` from `typing_extensions` without declaring it as a direct dependency.
- The dependency was only available via dev dependencies, so `uvx sqlite-utils` failed in clean environments.
- A new smoke test command `uv run --isolated --no-default-groups sqlite-utils --help` checks the CLI works without dev dependencies.
- `--isolated` ignores any existing `.venv/` and `--no-default-groups` skips default dev dependency groups.