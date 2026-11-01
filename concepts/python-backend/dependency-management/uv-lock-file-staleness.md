---
domain: python-backend
subdomain: dependency-management
concept: uv-lock-file-staleness
title: If in Doubt, Delete the uv.lock File
sources:
  - title: "If in doubt, delete the uv.lock file"
    url: "https://simonwillison.net/2026/Nov/1/delete-uv-lock-first/"
    author: "Simon Willison"
    date: "2026-11-01"
---

# If in Doubt, Delete the uv.lock File

Simon Willison documents a recurring Python dependency problem that appeared after switching to Python 3.15: stale `uv.lock` files pinning dependency versions that lack wheels for the new interpreter. His rule of thumb is simple — if in doubt, delete the `uv.lock` file.

Most of his projects are libraries, which deliberately omit a `uv.lock` since locking versions would impose constraints on downstream consumers. However, running commands like `uv run pytest` tends to generate `uv.lock` files as a side effect; these are gitignored and never committed, but they persist locally.

The failure mode is that a leftover lock file can pin a dependency whose build tooling doesn't yet support Python 3.15. His example is `watchfiles==1.1.1`, where the `maturin.build_wheel` call fails because PyO3's maximum supported interpreter version is 3.14. Deleting the lock file and re-running `uv run pytest` typically resolves the issue.

- Stale `uv.lock` files can pin dependencies that lack wheels for newer Python versions like 3.15.
- Libraries should generally not commit `uv.lock` files, since locking versions is rude to downstream consumers.
- Commands like `uv run pytest` leave gitignored `uv.lock` files behind locally, which can cause confusing errors.
- Deleting the lock file and re-running the command usually fixes build failures such as PyO3 rejecting Python 3.15.