---
domain: python-backend
subdomain: package release
concept: dependency-management
title: sqlite-utils 4.2.1
sources:
  - title: "sqlite-utils 4.2.1"
    url: "https://simonwillison.net/2026/Aug/13/sqlite-utils-2/"
    author: "Simon Willison"
    date: "2026-08-13"
---

# sqlite-utils 4.2.1

sqlite-utils 4.2.1 fixes a crashing bug introduced in version 4.2. The bug stemmed from importing `Self` from `typing_extensions` without declaring `typing-extensions` as a dependency. In the project's dev dependency group, `typing-extensions` was present transitively, but when users ran `uvx sqlite-utils` directly, the package was missing, causing the crash (Simon Willison, 2026).

The fix involved properly listing `typing-extensions` as a dependency. Additionally, the release notes describe a new smoke test method using `uv run --isolated --no-default-groups sqlite-utils --help` to ensure the CLI works without dev dependencies. The `--no-default-groups` flag skips the default dev group, while `--isolated` ignores any pre-existing `.venv/` folder, providing a clean check (Simon Willison, 2026).

- sqlite-utils 4.2.1 fixes a crash caused by missing `typing-extensions` dependency.
- The bug was not caught because `typing-extensions` was only available via dev dependencies.
- The new smoke test uses `uv run --isolated --no-default-groups` to validate the CLI without dev dependencies.