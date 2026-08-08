---
domain: python-backend
subdomain: security
concept: sql-injection-backport
title: datasette 0.65.3
sources:
  - title: "datasette 0.65.3"
    url: "https://simonwillison.net/2026/Aug/6/datasette-2/#atom-everything"
    date: "2026-08-06"
---

# datasette 0.65.3

datasette 0.65.3 is a patch release that back-ports a SQL Injection security fix originally introduced in version 1.0a38. The fix addresses a vulnerability in earlier versions, ensuring that users on the 0.65.x line receive the same protection without upgrading to the alpha release. This release is particularly relevant for deployments relying on the stable 0.65 series.

- Back-ports SQL Injection security fix from 1.0a38.
- Targets the stable 0.65.x line for users not on the alpha branch.
- No other changes mentioned; focused security patch.
- Released on 6th August 2026.