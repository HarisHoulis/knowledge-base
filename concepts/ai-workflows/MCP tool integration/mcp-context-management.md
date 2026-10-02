---
domain: ai-workflows
subdomain: MCP tool integration
concept: mcp-context-management
title: MCP Doesn't Suck. Your Agent Does. — Jan Čurn, Apify
sources:
  - title: "MCP Doesn't Suck. Your Agent Does. — Jan Čurn, Apify"
    url: "https://www.youtube.com/watch?v=pAnLpiAG6Es"
    author: "Jan Čurn / AI Engineer"
    date: "2026-10-02T14:00:05+00:00"
---

# MCP Doesn't Suck. Your Agent Does. — Jan Čurn, Apify

In “MCP Doesn't Suck, Your Agent Does,” Jan Čurn argues that MCP has become the standard for secure agent access to tools and resources since Anthropic introduced it almost two years ago, with roughly 10,000–15,000 servers and adoption by Claude and ChatGPT connectors (Jan Čurn, “MCP Doesn't Suck. Your Agent Does.”). Despite that adoption, he catalogs public criticism claiming MCP is the wrong abstraction, a mistake, mostly useless, or something CLIs/APIs should replace (Jan Čurn, “MCP Doesn't Suck. Your Agent Does.”).

The central technical complaint is context consumption. Early agent implementations registered every tool from every MCP server up front, consuming perhaps a third of the context window before any work began; tool calls and their results then add more context, hurting accuracy and cost (Jan Čurn, “MCP Doesn't Suck. Your Agent Does.”). Čurn says this is not an MCP protocol flaw: the specification does not dictate implementation, so it is the agent builder's job to use MCP effectively (Jan Čurn, “MCP Doesn't Suck. Your Agent Does.”).

He evaluates fixes. Subagents can isolate tasks in separate context windows, but they still incur token costs and do not fully eliminate the risk of sensitive or large results persisting in context (Jan Čurn, “MCP Doesn't Suck. Your Agent Does.”). Progressive tool discovery, introduced by Anthropic and Cursor, is presented as a simple, logical improvement: a tool finder exposes tools only when needed, saving a huge amount of context and making work cheaper and faster (Jan Čurn, “MCP Doesn't Suck. Your Agent Does.”).

The excerpt cuts off before the full conclusion, but the through-line is that MCP's bad reputation often reflects poor agent design rather than the protocol itself (Jan Čurn, “MCP Doesn't Suck. Your Agent Does.”).

- MCP is described as the standard for secure agent access to tools and resources, introduced by Anthropic almost two years ago and used by roughly 10,000–15,000 servers.
- Critics say MCP consumes too much context; early naive implementations preload all tools, so context is spent before work begins.
- Jan Čurn argues context bloat is an implementation problem, not a protocol problem, because the MCP specification does not prescribe implementation details.
- Subagents can isolate context but still pay token costs and retain risks around sensitive or large results.
- Progressive tool discovery, such as Anthropic's/Cursor's tool finder, adds tools gradually only when needed, saving context and improving cost and speed.