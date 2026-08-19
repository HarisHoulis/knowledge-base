---
domain: python-backend
subdomain: python-packaging
concept: dependency-isolation-smoke-test
title: sqlite-utils 4.2.1: Fixing Missing Dependency and Adding Isolated CLI Smoke Test
sources:
  - title: "sqlite-utils 4.2.1"
    url: "https://simonwillison.net/2026/Aug/13/sqlite-utils-2/"
    date: "2026-08-13T23:53:47+00:00"
---

# sqlite-utils 4.2.1: Fixing Missing Dependency and Adding Isolated CLI Smoke Test

sqlite-utils 4.2.1 fixes a crashing bug introduced in version 4.2. The bug was caused by importing `Self` from `typing_extensions` without declaring `typing-extensions` as a runtime dependency. The package was only present in the dev dependency group, so direct invocation via `uvx sqlite-utils` failed because dev dependencies are not installed in that context.

- The crash was due to an undeclared runtime dependency on `typing-extensions`.
- The dependency was only available in the dev group, so `uvx sqlite-utils` broke.
- A smoke test using `uv run --isolated --no-default-groups sqlite-utils --help` now ensures the CLI works without dev dependencies.