---
domain: ai-workflows
subdomain: agent-orchestration
concept: secure-agent-service-integration
title: My Agent Ships Across 6 Services Without Seeing a Secret
sources:
  - title: "My Agent Ships Across 6 Services Without Seeing a Secret"
    url: "https://www.youtube.com/watch?v=u2PzSPD-wVI"
    author: "Kent C. Dodds"
    date: "2026-07-23T13:45:07+00:00"
---

# My Agent Ships Across 6 Services Without Seeing a Secret

Kent C. Dodds demonstrates how his custom tool, Kodi, enables an AI agent to operate across multiple services securely and efficiently. Instead of relying on copy-pasting data or exposing local CLI credentials, Kodi acts as a secure middleware layer that connects the agent to services like Notion, Dropbox, and Remotion. The agent performs tool calls through a Kodi server, which handles authentication and secrets without ever revealing them to the agent or storing them on the local machine. Also, Kodi includes a built-in memory mechanism that surfaces relevant context during searches, improving the agent's accuracy and reducing token usage. The walkthrough shows the agent automatically updating planning documentation and moving a video project from a draft review to ready-to-publish on a Notion kanban board, all through a simple conversational prompt.

- Kodi connects an AI agent to multiple services securely, keeping secrets completely hidden from the agent and local environment.
- The agent uses a search tool to discover available services and relevant memory, then an execute tool to perform actions like updating Notion.
- A conversation ID is returned from the first tool call and used to maintain state across subsequent actions.
- Kodi is token-efficient and can be used from any device, including a phone, making it a practical alternative to manual, CLI-heavy workflows.
- The demonstration shows the agent updating documentation and moving kanban cards across stages without human intervention.