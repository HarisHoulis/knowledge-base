---
domain: ai-workflows
subdomain: coding-agents
concept: ai-assisted-game-feature-development
title: Battledrones v14: Compass Rose, a Four-Player Map Built via AI Coding Agent
sources:
  - title: "battledrones v14: Compass Rose, a four player map"
    url: "https://simonwillison.net/2026/Oct/24/battledrones/"
    author: "Simon Willison"
    date: "2026-10-24"
---

# Battledrones v14: Compass Rose, a Four-Player Map Built via AI Coding Agent

Simon Willison released battledrones v14, adding a four-player online mode to the game, which previously supported only two players. The feature was implemented by Claude Opus 5.5 from a single initial prompt requesting a new map with four-way rotational symmetry, support for up to four AI players, and compatibility with the WebSocket non-audio multiplayer mode so up to four humans could join, with spare slots filled by AI.

The agent created a new map called "Compass Rose" and modified the WebSockets multiplayer network code to support up to four players for that map, with joining via share links or QR codes. The new teams use purple and green robot designs alongside the existing blue and red ones, previewable in an updated model browser.

A replay link demonstrates a four-way AI battle with the "Goliath Armada" mutator enabled, where each side starts with four giant Goliath mech units.

- A single natural-language prompt drove Claude Opus 5.5 to add a four-player map and extend the WebSocket multiplayer code to four players.
- The new "Compass Rose" map uses four-way rotational symmetry and supports mixed human/AI slots.
- New purple and green robot teams were added alongside the existing blue and red designs.
- A replay link shows a four-way AI battle with the "Goliath Armada" mutator.