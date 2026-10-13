---
domain: ai-workflows
subdomain: coding-agents
concept: agent-adjacent-file-editing
title: web-edit 0.1a0: A Web UI for Editing Files Without Routing Them Through an LLM
sources:
  - title: "web-edit 0.1a0"
    url: "https://simonwillison.net/2026/Oct/12/web-edit/"
    author: "Simon Willison"
    date: "2026-10-12"
---

# web-edit 0.1a0: A Web UI for Editing Files Without Routing Them Through an LLM

Simon Willison released web-edit 0.1a0, a Python web app that provides a browser UI for viewing and editing files in a folder. The motivation came from working on a project from his phone via Codex Remote: he wanted to edit a credentials file without round-tripping those credentials through the LLM itself. The tool is intended to be run over Tailscale, so an agent can start it and he can then edit files directly from his phone across his Tailscale network.

The app includes an interface for browsing files in a folder, and editing is powered by CodeMirror 6. Willison notes he initially considered Monaco but chose CodeMirror because Monaco still lacks a great mobile experience. The project was built with Codex and GPT-6 Astra Extra High.

- web-edit is a Python web app for viewing and editing files in a folder via a browser UI.
- It was created to edit credentials files from a phone without sending those credentials through the LLM.
- It is designed to run over Tailscale, letting an agent start it and the user edit files from their phone.
- Editing uses CodeMirror 6; Monaco was rejected due to its weaker mobile experience.