---
domain: python-backend
subdomain: python-packaging
concept: dependency-isolation-smoke-test
title: sqlite-utils 4.2.1
sources:
  - title: "sqlite-utils 4.2.1"
    url: "https://simonwillison.net/2026/Aug/13/sqlite-utils-2/"
    date: "2026-08-13"
---

# sqlite-utils 4.2.1

sqlite-utils 4.2.1 fixes a crashing bug introduced in 4.2. The bug was caused by importing `Self` from `typing_extensions` without declaring the `typing-extensions` package as a direct dependency. It was only available transitively via the dev dependency group, so direct invocations like `uvx sqlite-utils` would fail because those dev dependencies are not installed. The fix ensures the proper dependency is declared. Additionally, the author figured out a smoke test command to verify the CLI works without dev dependencies: `uv run --isolated --no-default-groups sqlite-utils --help`. This command uses `--no-default-groups` to skip the default `dev` group and `--isolated` to ignore any local `.venv/` folder, ensuring the smoke test runs against only the project's declared dependencies.

- sqlite-utils 4.2.1 fixes a crash caused by an undeclared `typing-extensions` dependency.
- The bug occurred because `typing_extensions.Self` was imported but the package was only present via the dev dependency group.
- Direct usage via `uvx sqlite-utils` did not include dev dependencies, leading to the failure.
- A new smoke test command `uv run --isolated --no-default-groups sqlite-utils --help` validates the CLI without dev dependencies.
- The fix serves as a reminder to explicitly declare runtime dependencies even if they are transitively available in development environments.