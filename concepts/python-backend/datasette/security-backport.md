---
domain: python-backend
subdomain: datasette
concept: security-backport
title: Datasette 0.65.6: Backported Security Fix for Database Route Access
sources:
  - title: "datasette 0.65.6"
    url: "https://simonwillison.net/2026/Nov/15/datasette-2/"
    author: "Simon Willison"
    date: "2026-11-15"
---

# Datasette 0.65.6: Backported Security Fix for Database Route Access

Datasette 0.65.6 is a patch release that backports a minor security fix from the 1.0a43 alpha. The issue involved databases registered via `add_database(db, name=..., route=...)` where the route differed from the database name: actors denied access to the database could still download it from `/<route>.db`.

- Backports a security fix originally shipped in 1.0a43
- Affects databases registered with a route that differs from their name
- Unauthorized actors could download the database via `/<route>.db`