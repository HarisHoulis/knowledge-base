---
domain: python-backend
subdomain: datasette-plugins
concept: datasette-auth-github-1-0
title: datasette-auth-github 1.0: Fixing Session Cookie Expiry
sources:
  - title: "datasette-auth-github 1.0"
    url: "https://simonwillison.net/2026/Sep/19/datasette-auth-github/"
    date: "2026-09-19"
  - title: "datasette-auth-github 1.0 release"
    url: "https://github.com/simonw/datasette-auth-github/releases/tag/1.0"
    date: "2026-09-19"
---

# datasette-auth-github 1.0: Fixing Session Cookie Expiry

Simon Willison released version 1.0 of datasette-auth-github, a GitHub login plugin for Datasette, after fixing a bug that caused authenticated sessions to expire quickly (source: datasette-auth-github 1.0). While running the plugin on the agent.datasette.io demo site, he noticed authenticated sessions weren't lasting long; the cause was that the plugin set cookies without a `Max-Age` parameter, so they expired at the end of a browser session — something that happens frequently in Mobile Safari regardless of app usage (source: datasette-auth-github 1.0).

The fix landed in issue #80 (source: datasette-auth-github 1.0). Because the plugin has existed for a long time and is tested against both Datasette 0.65.x and Datasette 1.0ax, Willison promoted it to a 1.0 release, noting a broader effort to get better at promoting stable plugins to 1.0 (source: datasette-auth-github 1.0).

- datasette-auth-github 1.0 fixes cookies being set without a `Max-Age` parameter, which caused sessions to end with the browser session
- The bug was discovered through use of the plugin on the agent.datasette.io demo site
- The fix is tracked in issue #80
- The plugin is tested against Datasette 0.65.x and Datasette 1.0a, motivating the 1.0 version bump