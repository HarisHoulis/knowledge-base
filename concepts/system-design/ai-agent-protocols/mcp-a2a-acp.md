---
domain: system-design
subdomain: ai-agent-protocols
concept: mcp-a2a-acp
title: MCP vs A2A vs ACP: How AI Agents Actually Talk to Each Other
sources:
  - title: "MCP vs A2A vs ACP: How AI Agents Actually Talk to Each Other"
    url: "https://blog.bytebytego.com/p/mcp-vs-a2a-vs-acp-how-ai-agents-actually"
    author: "ByteByteGo"
    date: "2026-07-18"
---

# MCP vs A2A vs ACP: How AI Agents Actually Talk to Each Other

The article explains the three primary communication protocols for AI agents: MCP, A2A, and ACP. MCP (Model Context Protocol) is designed for agent-to-tool communication: a host app embeds an MCP client that routes user requests to the appropriate MCP server, which executes the tool call and returns structured output. A2A (Agent-to-Agent) enables direct agent-to-agent collaboration: an agent discovers capable peers via an Agent Card published at a known URL, delegates tasks, and handles mid-task pauses through an input-required state. ACP (Agent Communication Protocol) was a REST-first approach that used an Agent Manifest for discovery, but it has since been merged into A2A. In practice, MCP and A2A are complementary: MCP handles tool access, while A2A handles inter-agent communication. The article also touches on evaluation approaches for LLMs, RAG, coding agents, and multi-agent systems, emphasizing that each added component introduces new failure modes requiring tailored grading strategies.

- MCP is for agent-to-tool communication: host app with embedded MCP client routes to MCP server, which executes tool calls and returns structured responses.
- A2A is for agent-to-agent communication: agents discover each other via Agent Cards, delegate tasks, and handle mid-task input needs via a paused state.
- ACP (REST-first agent protocol) has been merged into A2A; it originally used Agent Manifest for discovery and sync/async communication.
- MCP and A2A are complementary in production: MCP provides tool access, A2A provides agent-to-agent messaging.
- Evals for AI systems (LLMs, RAG, coding agents, multi-agent) must grade each new pipeline component separately, using methods like LLM-as-judge, retrieval checks, and unit tests.