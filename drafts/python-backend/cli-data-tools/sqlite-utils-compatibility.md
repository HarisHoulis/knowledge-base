---
domain: python-backend
subdomain: cli-data-tools
concept: sqlite-utils-compatibility
title: github-to-sqlite 2.9.1: sqlite-utils 4.x compatibility fix
sources:
  - title: "github-to-sqlite 2.9.1"
    url: "https://simonwillison.net/2026/Sep/11/github-to-sqlite/"
    author: "Simon Willison"
    date: "2026-09-11"
---

# github-to-sqlite 2.9.1: sqlite-utils 4.x compatibility fix

Version 2.9.1 of github-to-sqlite is a patch release whose sole change is a fix for compatibility with sqlite-utils 4.x, tracked as issue #85 in the dogsheep/github-to-sqlite repository. No other changes, features, or behavioral notes accompany the release.

The release is dated 11th September 2026 and is a maintenance update driven by an upstream dependency change, pointing users toward the sqlite-utils v4.2 changelog entry for context on what shifted.

- github-to-sqlite 2.9.1 contains a single change: compatibility with sqlite-utils 4.x.
- The fix is referenced by issue #85 on the dogsheep/github-to-sqlite GitHub repository.
- Users should consult the sqlite-utils v4.2 changelog for details on the upstream change.