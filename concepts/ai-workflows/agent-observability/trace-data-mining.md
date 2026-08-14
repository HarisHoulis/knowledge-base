---
domain: ai-workflows
subdomain: agent-observability
concept: trace-data-mining
title: Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain
sources:
  - title: "Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain"
    url: "https://www.youtube.com/watch?v=CvRngaQZQ3Y"
    author: "AI Engineer"
    date: "2026-08-12"
---

# Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain

Vivek Trivedy of LangChain argues that continuously improving AI agents is fundamentally a data mining problem. The process begins with shipping an agent into the real world, then collecting a large volume of traces from its operations—including tool calls, API interactions, and CLI usage. These traces form the raw material for identifying both successful and unsuccessful behaviors, which can then guide targeted improvements. Trivedy emphasizes that observability and continual learning are tightly coupled: agents operating in environments produce trace data, and that data is the basis for updating prompts, tools, or orchestration logic.

- Successful agent improvement starts with shipping the agent and collecting comprehensive trace data.
- Trace data enables data mining over gigabytes or terabytes of agent interactions to surface good and bad patterns.
- Observability and continual learning are tightly coupled; traces are the foundation for iterative agent updates.
- Data-driven experiments are essential to validate whether changes to prompts, tools, or orchestration actually improve performance.
- Unlike static code, agent behavior is difficult to reason about manually; trace analysis makes it actionable.