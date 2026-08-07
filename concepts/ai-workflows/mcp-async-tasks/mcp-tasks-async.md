---
domain: ai-workflows
subdomain: mcp-async-tasks
concept: mcp-tasks-async
title: MCP Tasks (async): Why Aren't Any Agents Supporting Them?
sources:
  - title: "MCP Tasks (async): Why Aren't Any Agents Supporting Them? — Cornelia Davis, Temporal"
    url: "https://www.youtube.com/watch?v=s4r6nk5WsZw"
    author: "AI Engineer"
    date: "2026-08-02T20:00:06+00:00"
---

# MCP Tasks (async): Why Aren't Any Agents Supporting Them?

The presentation also reveals that a new MCP Tasks V2 is coming in July with radical changes, which further explains why agents are not rushing to implement the experimental V1. The talk concludes with live demos and takeaways, emphasizing that asynchronous MCP tools need robust orchestration—an area where Temporal's distributed systems expertise applies (source).

- MCP Tasks allow invoking a long-running MCP tool and receiving a handle instead of an immediate response, enabling async workflows.
- Agent builders are hesitant to support MCP Tasks V1 because it's experimental and known to be superseded by V2 in July.
- Long-running tasks introduce complexity: network failures, crashes, and human availability require durable, stateful execution.
- Human-in-the-loop steps like approve/reject need explicit signaling mechanisms into the running process.
- Real-world use cases (e.g., purchase order processing) show the need for orchestration beyond simple request-response.