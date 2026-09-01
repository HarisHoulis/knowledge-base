---
domain: ai-workflows
subdomain: secure-agent-integrations
concept: kodi-secure-service-integration
title: My Agent Ships Across 6 Services Without Seeing a Secret
sources:
  - title: "My Agent Ships Across 6 Services Without Seeing a Secret"
    url: "https://www.youtube.com/watch?v=u2PzSPD-wVI"
    author: "Kent C. Dodds"
    date: "2026-07-23T13:45:07+00:00"
---

# My Agent Ships Across 6 Services Without Seeing a Secret

In this video, Kent C. Dodds demonstrates how his custom project, Kodi, enables an AI agent to securely interact with multiple external services without exposing secrets. Instead of manually copying data between services or relying solely on MCP servers or local CLIs with accessible keys, Kodi provides a server layer with search and execute tool calls. The agent first searches for relevant services and documentation, then executes operations directly, all while keeping secrets safe and minimizing token usage (Dodds, 2026).

Dodds walks through a real example where he asked the agent to update planning documentation and help publish a video. The agent used Kodi to search for available services, found the Notion integration, skipped Remotion because the final edit was already on Dropbox, and staged the video on a Notion kanban board—moving it from 'draft review' toward 'ready to publish' and ultimately 'published'. Kodi also includes a memory mechanism that surfaces relevant memories based on the task and entities, contributing to better search results and context (Dodds, 2026).

The key value is efficiency and security: agents can operate from a phone or computer, token usage is controlled, and secrets are not exposed to local processes. This represents a shift from manual, copy-paste workflows or insecure CLI-based automation to a structured, secure agent-service integration pattern (Dodds, 2026).

- Kodi provides a secure server layer that lets agents search and execute across services without exposing secrets.
- Agents first search available services/packages via Kodi, then execute mutations like updating Notion kanban cards.
- Kodi's built-in memory context improves semantic search by surfacing task-relevant memories and entities.
- The approach is token-efficient and mobile-friendly, unlike local CLI setups with broadly accessible keys.
- Example: agent moved a video through the publishing pipeline by skipping Remotion (edit already on Dropbox) and updating Notion.