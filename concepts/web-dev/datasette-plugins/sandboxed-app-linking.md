---
domain: web-dev
subdomain: datasette-plugins
concept: sandboxed-app-linking
title: datasette-apps 0.4a0: URL Fragment Linking for Sandboxed Apps
sources:
  - title: "datasette-apps 0.4a0"
    url: "https://simonwillison.net/2026/Nov/15/datasette-apps/"
    author: "Simon Willison"
    date: "2026-11-15"
---

# datasette-apps 0.4a0: URL Fragment Linking for Sandboxed Apps

datasette-apps 0.4a0 introduces linking support for Datasette Apps, which are sandboxed HTML and JavaScript applications embedded in Datasette that can run SQL queries against the underlying data—described as similar to Claude Artifacts but with database access. The release lets apps be linked to via `#fragments` in the URL, and apps can read and use those fragments. Supported URL schemes are also reported back to Datasette Agent, so the agent can help write apps that link to one another. The practical effect is composable apps: for example, one app can display details about a specific record while a separate search app links directly to that record's representation in the detail app.

- Datasette Apps are sandboxed HTML/JS apps inside Datasette that can run SQL queries against your data
- 0.4a0 adds `#fragment` URL linking that apps can read and use
- Supported URL schemes are reported to Datasette Agent to help it write cross-linking apps
- Enables separate apps (e.g. search and record-detail) to link to each other