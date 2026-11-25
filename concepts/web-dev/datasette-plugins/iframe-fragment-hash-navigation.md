---
domain: web-dev
subdomain: datasette-plugins
concept: iframe-fragment-hash-navigation
title: datasette-agent 0.7a1: Fragment Hash Navigation in Chat Side Panels
sources:
  - title: "datasette-agent 0.7a1"
    url: "https://simonwillison.net/2026/Nov/24/datasette-agent/"
    author: "Simon Willison"
    date: "2026-11-24"
---

# datasette-agent 0.7a1: Fragment Hash Navigation in Chat Side Panels

datasette-agent 0.7a1 is a small release that improves how chat sessions navigate the iframe side panel they can open. Previously the panel could navigate to different pages; this version adds improved navigation by fragment hashes, allowing deeper integration with other Datasette plugins that update fragment hashes when user interaction changes plugin state.

The author notes the change was made to fix bugs in the more significant datasette-charts 0.2a0 release, tying the agent's panel navigation to chart plugin state changes.

- Chat sessions in Datasette Agent can open an iframe side panel that navigates between pages.
- 0.7a1 adds improved fragment-hash navigation for deeper integration with plugins that update hashes on state changes.
- The change was motivated by fixing bugs in the datasette-charts 0.2a0 release.