---
domain: ai-workflows
subdomain: agent-architecture
concept: code-mode-agents
title: Stop Giving Your Agent Tools. Give It a Sandbox
sources:
  - title: "Stop Giving Your Agent Tools. Give It a Sandbox - Mikyo King, Arize AI"
    url: "https://www.youtube.com/watch?v=dAoOYFx7ZYw"
    author: "AI Engineer"
    date: "2026-10-27"
---

# Stop Giving Your Agent Tools. Give It a Sandbox

Mikyo (Michael) King of Arize AI argues that the traditional agent architecture—handing a model a large catalog of tools and letting it invoke them one at a time—does not scale to the emergent, long-horizon behavior people now want from agents. Each tool invocation is pushed into the context window, causing context bloat, tool-call mismatches, multi-turn sprawl, and the need for compaction, all of which raise latency and cost and delay the value the user receives.

His alternative, "Code Mode," replaces the giant tool menu with a programming environment: the agent searches for the specific tool it needs, then executes it inside a sandbox. Because the agent is writing code rather than emitting individual tool calls, it can run tools sequentially or in parallel, chain and combine them, and apply conditions—calling many tools in one go while returning only the results actually needed into the model's context.

King attributes Code Mode's effectiveness to four properties: gradual disclosure of tools (the agent picks and understands only the relevant ones), the ability to compose tools into complex chains, token efficiency (the model crops and searches outputs rather than dumping everything into context), and a fourth benefit he identifies as a primary reason Arize adopted it. He notes that Claude's dynamic workflows are built on this pattern, and frames the shift as dissolving the old boundary between software written for engineers and software for everyone else—coding agents can now generate the software a task requires on the fly.

- Traditional tool-calling agents accumulate context on every invocation, increasing latency, cost, and turn count
- Code Mode gives the agent a sandboxed programming environment where it searches for tools and executes them in code
- Agents can then call many tools at once, in parallel or chained, and return only the needed output to context
- Gradual tool disclosure and token efficiency are core advantages over a large static tool catalog
- Coding agents dissolve the boundary between engineer-built and non-engineer software by generating tools dynamically