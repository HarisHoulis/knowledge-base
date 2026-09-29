---
domain: python-backend
subdomain: datasette-plugins
concept: datasette-explain
title: datasette-explain 0.2.2
sources:
  - title: "datasette-explain 0.2.2"
    url: "https://simonwillison.net/2026/Sep/20/datasette-explain/"
    date: "2026-09-20"
---

# datasette-explain 0.2.2

This is a short release note for version 0.2.2 of datasette-explain, a plugin that surfaces SQLite explain plans inside Datasette (source). The headline change is that explain plans now work on read-only stored-query pages, extending the plugin's coverage beyond its previous scope (source).

The release was motivated by the author upgrading datasette.simonwillison.net to Datasette 1.0a40, which prompted shipping a new version of the explain plugin (source). The post is tagged with sqlite and datasette, placing it in the SQLite/Datasette tooling space rather than a general application domain (source).

- datasette-explain 0.2.2 adds explain plan support for read-only stored-query pages.
- The release was inspired by an upgrade of datasette.simonwillison.net to Datasette 1.0a40.
- The plugin is tagged under sqlite and datasette.