---
domain: python-backend
subdomain: datasette
concept: datasette-1-0a40-release
title: Datasette 1.0a40: background tasks for plugins and httpx2 migration
sources:
  - title: "datasette 1.0a40"
    url: "https://simonwillison.net/2026/Sep/16/datasette/"
    author: "Simon Willison"
    date: "2026-09-16"
---

# Datasette 1.0a40: background tasks for plugins and httpx2 migration

Datasette 1.0a40 is an alpha release that carries the same security fix shipped in 0.65.5, alongside new features and bug fixes (Simon Willison, "datasette 1.0a40"). Plugins can now launch and manage background tasks through the new `datasette.add_background_task()` method, a contribution credited to Alex Garcia.

The release also migrates Datasette to httpx2, which affects features such as the internal `datasette.client.get()` method. In addition, the author reports a large batch of bug fixes, many produced by a recent effort to triage issues in preparation for a 1.0 stable release.

The post is a short release note rather than an in-depth article; it points readers to the internals documentation and the changelog for details.

- Plugins can launch and manage background tasks via the new `datasette.add_background_task()` method (contributed by Alex Garcia).
- Datasette has been migrated to httpx2, used by features like the internal `datasette.client.get()` method.
- 1.0a40 includes the same security fix as 0.65.5.
- Many bug fixes landed, driven by issue-triage work aimed at a 1.0 stable release.