---
domain: python-backend
subdomain: datasette-deployment
concept: datasette-publish-fly
title: datasette-publish-fly 1.4
sources:
  - title: "datasette-publish-fly 1.4"
    url: "https://simonwillison.net/2026/Sep/11/datasette-publish-fly/"
    date: "2026-09-11"
---

# datasette-publish-fly 1.4

datasette-publish-fly 1.4 is a maintenance release of the Datasette plugin that publishes databases to Fly.io. The release sets `force_https=true` in `fly.toml` (issue #31) and includes a fix for a "Volume could not be found" bug (issue #32) [source: datasette-publish-fly 1.4].

The plugin is now compatible with app-scoped deploy tokens (issue #34), which affects how deployments authenticate against Fly.io [source: datasette-publish-fly 1.4].

- Sets `force_https=true` in `fly.toml` (#31).
- Fixes a "Volume could not be found" bug (#32).
- Adds compatibility with app-scoped deploy tokens (#34).