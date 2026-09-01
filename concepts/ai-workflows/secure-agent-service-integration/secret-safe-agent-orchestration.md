---
domain: ai-workflows
subdomain: secure-agent-service-integration
concept: secret-safe-agent-orchestration
title: My Agent Ships Across 6 Services Without Seeing a Secret
sources:
  - title: "My Agent Ships Across 6 Services Without Seeing a Secret"
    url: "https://www.youtube.com/watch?v=u2PzSPD-wVI"
    author: "Kent C. Dodds"
    date: "2026-07-23T13:45:07+00:00"
---

# My Agent Ships Across 6 Services Without Seeing a Secret

According to Kent C. Dodds in his YouTube video 'My Agent Ships Across 6 Services Without Seeing a Secret' (https://www.youtube.com/watch?v=u2PzSPD-wVI), his custom agent, Kodi, connects to multiple services (e.g., Notion, Dropbox, Remotion) in a secure and token-efficient way. Instead of copy-pasting context or installing CLIs with exposed keys, Kodi acts as a server-side bridge that lets the agent search available services and execute tool calls without ever seeing secrets. The agent first performs a search with Kodi, which uses built-in memory context to surface relevant memories and service integrations. In the example, the agent updates a Notion kanban board, moving a video project from draft review to ready to publish, after skipping Remotion because the final edit was already on Dropbox.

Kodi returns a conversation ID on the first tool call, enabling ongoing context. The system is designed to work on mobile and avoids token explosion by limiting search results and using semantic memory. Dodds contrasts this approach with simply adding MCP servers or installing CLIs, emphasizing that Kodi provides a secure, efficient way for agents to both read context and perform real-world mutations across services.

- Agents can securely integrate with multiple services through a server-side bridge like Kodi, without exposing secrets to the agent.
- Kodi uses a search tool with built-in memory context to surface relevant service integrations and memories, reducing token usage.
- The system supports both reading context and performing mutations, such as moving Notion cards on a kanban board.
- A conversation ID is returned from the first tool call to maintain state across subsequent operations.
- This approach avoids the token explosion and security issues of copy-pasting or using locally authenticated CLIs.