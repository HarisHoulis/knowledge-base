---
domain: ai-workflows
subdomain: agent-observability
concept: trace-driven-agent-improvement
title: Improving Agents is a Data Mining Problem
sources:
  - title: "Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain"
    url: "https://www.youtube.com/watch?v=CvRngaQZQ3Y"
    author: "Vivek Trivedy, LangChain"
    date: "2026-08-12T19:00:01+00:00"
---

# Improving Agents is a Data Mining Problem

The talk argues that improving AI agents is fundamentally a data mining problem. Once an agent is shipped and operating in real environments, every action generates trace data—tool calls, output messages, API calls, and CLI usage. This trace data is essential for understanding agent behavior and enabling continual improvement. The speaker emphasizes a tight coupling between observability and continual learning: traces are the raw material for updating agent definitions, prompts, tools, and orchestration (Vivek Trivedy, LangChain, 2026).

Unlike traditional code, agents are difficult for humans to reason about directly. They involve prompts, tools, skills, hooks, middlewares, and even hierarchical agent swarms. A prompt change in the medical domain can have very different effects than in law. As the field trades determinism for autonomy, new systems are needed to interpret autonomous agent behavior. The speaker describes LangChain's practice of centralizing traces in a tracing project and using LLM agents to mine traces—querying for good/bad interactions, user satisfaction signals, and technical issues (Vivek Trivedy, LangChain, 2026).

The overall recipe is: ship the agent, collect a large volume of traces (potentially gigabytes or terabytes), mine that data using agents, then use curated insights to run data-driven experiments—evaluating whether a new prompt, tool, or orchestration loop genuinely improves performance compared to baseline traces. This closes the loop between production data and development (Vivek Trivedy, LangChain, 2026).

- Agent improvement is a data mining loop: ship, collect traces, mine, experiment.
- Traces include tool calls, messages, API calls, and CLI usage; centralize them in a tracing project.
- Observability and continual learning are tightly coupled—traces are necessary for learning.
- Agents are hard to reason about like code; use agents to read traces and surface patterns and errors.
- Validate changes (prompt, tool, orchestration) via data-driven experiments against historical traces.