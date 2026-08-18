---
domain: python-backend
subdomain: python-packaging
concept: dependency-isolation
title: sqlite-utils 4.2.1: Fixing a Missing Dependency with Isolated Smoke Tests
sources:
  - title: "sqlite-utils 4.2.1"
    url: "https://simonwillison.net/2026/Aug/13/sqlite-utils-2/"
    date: "2026-08-13T23:53:47+00:00"
---

# sqlite-utils 4.2.1: Fixing a Missing Dependency with Isolated Smoke Tests

sqlite-utils 4.2.1 fixes a crashing bug introduced in 4.2. The crash occurred because the code imported `Self` from `typing_extensions`, but `typing-extensions` was not listed as a direct dependency. It was only present through the dev dependency group, so a direct `uvx sqlite-utils` invocation would fail.

- Missing direct dependency caused a crash in sqlite-utils 4.2.
- The fix in 4.2.1 ensures `typing-extensions` is properly declared as a dependency.
- A new smoke test runs `uv run --isolated --no-default-groups sqlite-utils --help` to verify the CLI works without dev dependencies.
- The `--isolated` flag ignores any existing `.venv/` folder during the test.