---
domain: python-backend
subdomain: datasette-plugins
concept: agent-driven-charting
title: datasette-charts 0.2a0: Chart Generation via Datasette Agent
sources:
  - title: "datasette-charts 0.2a0"
    url: "https://simonwillison.net/2026/Nov/24/datasette-charts/"
    author: "Simon Willison"
    date: "2026-11-24"
---

# datasette-charts 0.2a0: Chart Generation via Datasette Agent

datasette-charts 0.2a0 is an alpha release of a Datasette charting plugin, introduced the day before this release post. The new version adds integration with Datasette Agent, so users can ask the chat interface for a chart and have one generated using the plugin's underlying chart suggestion and generation tools.

The post points to a demo video recorded on agent.datasette.io, where users can sign in with GitHub to try the plugin, and links a Markdown export of the demo chat session. The release is tagged under datasette-agent, datasette, and visualization.

- datasette-charts 0.2a0 integrates with Datasette Agent for chat-driven chart creation
- The agent reuses the plugin's existing chart suggestion and generation tools
- A demo is available at agent.datasette.io via GitHub sign-in