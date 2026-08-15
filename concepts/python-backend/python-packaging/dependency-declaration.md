---
domain: python-backend
subdomain: python-packaging
concept: dependency-declaration
title: sqlite-utils 4.2.1
sources:
  - title: "sqlite-utils 4.2.1"
    url: "https://simonwillison.net/2026/Aug/13/sqlite-utils-2/"
    date: "2026-08-13T23:53:47+00:00"
---

# sqlite-utils 4.2.1

sqlite-utils 4.2.1 is a patch release that fixes a crashing bug introduced in 4.2. The bug was caused by importing `Self` from `typing_extensions` without listing `typing-extensions` as a direct dependency. This package was only present in the development dependency group, so when users ran `uvx sqlite-utils` directly, the import failed and the tool crashed. The fix adds the missing dependency to the project's declared dependencies. To prevent similar regressions, the release also includes a smoke test command: `uv run --isolated --no-default-groups sqlite-utils --help`. This command ensures the CLI works with only the declared dependencies, ignoring any pre-existing virtual environment and dev groups.

- sqlite-utils 4.2 crashed because `typing-extensions` was not a declared dependency but was imported at runtime.
- The bug was masked in development because `typing-extensions` was installed transitively via dev dependencies.
- The fix adds the missing dependency and a smoke test using `uv run --isolated --no-default-groups` to verify clean environment behavior.
- This highlights the importance of explicitly declaring all runtime dependencies, even those that may be present in dev environments.