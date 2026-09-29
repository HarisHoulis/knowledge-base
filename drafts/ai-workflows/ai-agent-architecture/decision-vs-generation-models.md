---
domain: ai-workflows
subdomain: ai-agent-architecture
concept: decision-vs-generation-models
title: Decision vs. Generation: Jev, MCP, and Claude Code's Context Assembly
sources:
  - title: "EP227: Top 9 Places to Use Jev"
    url: "https://blog.bytebytego.com/p/ep227-top-9-places-to-use-jev"
    author: "ByteByteGo"
    date: "Sat, 26 Sep 2026 14:31:13 GMT"
---

# Decision vs. Generation: Jev, MCP, and Claude Code's Context Assembly

The issue's central claim is that LLMs should be reserved for generation while a faster, smaller model handles the decisions around them. ByteByteGo describes Jev, TypeSafe AI's "System One Model," as 100x faster and cheaper than frontier LLMs, which makes viable nine use cases usually skipped for cost or latency: model routing, guardrails, gating tool-calls, inbox triage, reranking, LLM evals, bulk labeling, real-time decisions, and confidence gating (ByteByteGo, EP227). The stated bottom line is to "use the LLM for generations and use Jev on the decisions around it."

The issue also draws definitional lines between LLM, RAG, AI agent, and agentic AI. An LLM predicts tokens from learned parameters; RAG prepends a retriever that grounds the response without guaranteeing correctness; an AI agent holds a goal and task state, plans, calls tools, observes results, and loops until the goal is met; agentic AI orchestrates one or more agents toward a shared objective through an orchestration layer and shared task state.

MCP and function calling share the same tool-call loop — prompt to LLM, LLM emits a tool call, the runtime executes and returns results — but differ in where the function is implemented. Local function calling executes on the user's machine; MCP functions can live on remote servers reached over the MCP protocol, enabling access to hundreds of thousands of publicly hosted tools.

Finally, the piece describes Claude Code's context assembly: nine layers built before each model call — system prompt, environment info, CLAUDE.md hierarchy, auto memory, path-scoped rules, tool metadata, conversation history, tool results, and compact summaries — only one of which is the user's prompt.

- Use LLMs for generation and fast, cheap small models like Jev for the surrounding decisions: routing, guardrails, tool-call gating, reranking, evals, and confidence gates.
- Jev is claimed to be 100x faster and cheaper than frontier LLMs, opening up use cases skipped for latency or cost.
- MCP and function calling share the same tool-call loop; the difference is local execution (function calling) versus remote servers over the MCP protocol (MCP).
- Claude Code assembles nine context layers per model call; auto memory and path-scoped rules load without being explicitly requested.