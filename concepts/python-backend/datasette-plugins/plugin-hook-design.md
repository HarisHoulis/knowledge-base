---
domain: python-backend
subdomain: datasette-plugins
concept: plugin-hook-design
title: datasette-charts 0.4a0: Refining the Chart Plugin Hook
sources:
  - title: "datasette-charts 0.4a0"
    url: "https://simonwillison.net/2026/Nov/27/datasette-charts/"
    author: "Simon Willison"
    date: "2026-11-27"
---

# datasette-charts 0.4a0: Refining the Chart Plugin Hook

datasette-charts 0.4a0 is a release that refines the plugin's own plugin hook, which lets other plugins define new chart types. The author had not previously exercised this hook, so he had Claude Opus 5.5 build an experimental plugin to test it; that exercise surfaced a number of friction points in the design, and this release addresses them to make building additional chart plugins more ergonomic.

The release also introduces a dedicated website at charts.datasette.io, which includes a tutorial for plugin authors and a gallery of all core charts and annotations. Each gallery entry links to an interactive demo running on Datasette Lite.

- datasette-charts exposes a plugin hook allowing other plugins to define new chart types
- An AI-built experimental plugin was used to dogfood the hook and reveal design friction
- 0.4a0 addresses those friction points to make chart plugins more ergonomic
- New charts.datasette.io site offers a plugin-author tutorial and a gallery with Datasette Lite demos