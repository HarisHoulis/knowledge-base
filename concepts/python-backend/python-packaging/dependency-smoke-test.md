---
domain: python-backend
subdomain: python-packaging
concept: dependency-smoke-test
title: sqlite-utils 4.2.1
sources:
  - title: "sqlite-utils 4.2.1"
    url: "https://simonwillison.net/2026/Aug/13/sqlite-utils-2/"
    date: "2026-08-13T23:53:47+00:00"
---

# sqlite-utils 4.2.1

sqlite-utils 4.2.1 is a patch release that fixes a crashing bug introduced in version 4.2. The bug stemmed from using `from typing_extensions import Self`, but the `typing-extensions` package was not declared as a dependency. It happened to be installed via the dev dependency group, but running the CLI directly with `uvx` did not include those dev dependencies, leading to crashes.

- The crash was caused by an undeclared dependency on `typing-extensions`.
- The fix ensures `typing-extensions` is properly listed as a dependency.
- A smoke test using `uv run --isolated --no-default-groups sqlite-utils --help` verifies the CLI works without dev dependencies.
- The `--no-default-groups` flag skips the default dev group, and `--isolated` ignores any existing `.venv`.