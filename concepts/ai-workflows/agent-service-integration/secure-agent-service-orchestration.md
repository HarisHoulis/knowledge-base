---
domain: ai-workflows
subdomain: agent-service-integration
concept: secure-agent-service-orchestration
title: My Agent Ships Across 6 Services Without Seeing a Secret
sources:
  - title: "My Agent Ships Across 6 Services Without Seeing a Secret"
    url: "https://www.youtube.com/watch?v=u2PzSPD-wVI"
    author: "Kent C. Dodds"
    date: "2026-07-23T13:45:07+00:00"
---

# My Agent Ships Across 6 Services Without Seeing a Secret

In this talk, Kent C. Dodds demonstrates how his custom tool Kodi enables an AI agent to operate across multiple services—such as Notion and Dropbox—to complete a real-world publishing task without exposing any secrets. He argues that common approaches like copy-pasting credentials, using MCP servers, or relying on CLIs are either insecure (secrets accessible to other local processes) or token-inefficient. Kodi provides a secure bridge between the agent and external services, exposing only controlled tools rather than raw credentials (Kent C. Dodds, 2026).

- Kodi securely connects AI agents to multiple external services without exposing secrets to the agent or local processes.
- Agents use a search tool to discover available integrations and documentation, then an execute tool to perform actions like updating a kanban board.
- Kodi's built-in memory context enhances search relevance by surfacing related memories automatically.
- The design is token-efficient and works across devices, making it suitable for real-world production workflows.