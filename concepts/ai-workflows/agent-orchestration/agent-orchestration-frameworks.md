---
domain: ai-workflows
subdomain: agent-orchestration
concept: agent-orchestration-frameworks
title: Six Orchestration Frameworks for AI Agent Systems
sources:
  - title: "EP232: 6 Frequently Used Orchestration Frameworks in an AI system"
    url: "https://blog.bytebytego.com/p/ep232-6-frequently-used-orchestration"
    author: "ByteByteGo"
    date: "2026-11-07"
---

# Six Orchestration Frameworks for AI Agent Systems

Orchestration in an AI system is the layer that manages tasks across agents, handles failures, and coordinates shared memory and context. ByteByteGo surveys six frameworks, each taking a distinct approach: LangGraph models workflows as graphs where nodes are steps and edges define state transitions; CrewAI uses role-based abstraction, assigning agents defined roles and goals that work sequentially or under a manager agent; and Microsoft Agent Framework targets organizational workflows with graphs that add branching, checkpoints, and human-intervention pauses. OpenAI Agents SDK takes an LLM-driven runtime approach where the agent itself decides whether to delegate control to another agent or retain execution. Google ADK uses a hybrid control model where a developer defines the strategy and a root agent splits and distributes tasks to sub-agents. Claude Agent SDK has no separate orchestration layer at all — orchestration lives inside the agent, which gathers context, works with tools, evaluates, and keeps going until no calls remain.

The same issue covers cost optimization for AI systems: prompt caching of stable prefixes like system prompts and tool schemas, model routing that sends simple queries to small models and hard ones to frontier models, batch APIs for asynchronous bulk jobs, semantic caching of queries via embeddings, trimming conversation history to avoid resending full context, and distillation or quantization to shrink models.

Two supporting walkthroughs round out the refresher. A SQL query's lifecycle runs through parse-and-validate (producing a logical query tree), rewrite and transform, plan optimization, plan execution (filtering, joining, sorting, typically bottom-up), cache/storage access, and row return. A Claude Code request trace shows the agent loop: the interface wraps the prompt with repo and file context, the loop proposes an action, the permission system checks it, the approved action becomes a tool call dispatched to the execution environment, the result returns to the loop, and the turn is persisted and streamed to the user — repeated until the model stops asking for tools.

- Orchestration frameworks differ mainly in control model: graph-based (LangGraph, Microsoft Agent Framework), role-based (CrewAI), LLM-driven delegation (OpenAI Agents SDK), hybrid root-agent splitting (Google ADK), and no separate layer (Claude Agent SDK).
- Cost optimization levers include prompt caching, model routing, batch APIs, semantic caching, context trimming, and model distillation/quantization.
- A SQL query flows through parse/validate, rewrite, plan optimization, execution, cache/storage access, and row return.
- Claude Code's request path is a loop: context-wrapped prompt, proposed action, permission check, tool call, execution result, state persistence — repeated until no more tool calls.