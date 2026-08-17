---
domain: ai-workflows
subdomain: agent-observability
concept: trace-driven-agent-improvement
title: Improving Agents is a Data Mining Problem
sources:
  - title: "Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain"
    url: "https://www.youtube.com/watch?v=CvRngaQZQ3Y"
    author: "AI Engineer"
    date: "2026-08-12T19:00:01+00:00"
---

# Improving Agents is a Data Mining Problem

In this talk, Vivek Trivedy from LangChain argues that continuously improving AI agents is fundamentally a data mining problem. The proposed recipe is straightforward: ship agents into real-world environments, collect vast amounts of trace data from their operations, mine that data to surface patterns, and run data-driven experiments to validate improvements. He emphasizes that agents generate rich trace data—tool calls, output messages, API interactions, CLI usage—and that this data is the raw material for continual learning.

Trivedy highlights a tight coupling between observability and continual learning. Observability provides the trace data that makes improvement possible; without traces, there is no basis for understanding agent behavior or iterating on it. He also notes that agents are far harder for humans to reason about than traditional code, because behavior is shaped by prompts, tools, skills, hooks, and orchestration, and it varies across domains. Consequently, trace mining becomes essential for identifying both successful and problematic interactions.

The talk concludes by describing how LangChain applies this approach in practice: centralizing trace data into projects, using agents to read other agents' traces, and asking targeted questions to find good and bad interactions. This data-driven methodology enables teams to make informed changes to prompts, tools, or orchestration logic and verify their impact through experiments.

- Ship agents first and collect trace data from real-world operation to enable improvement.
- Trace data includes tool calls, messages, API calls, and CLI usage—store all of it.
- Data mining over traces helps surface good and bad interactions, guiding iteration.
- Observability and continual learning are tightly coupled: traces are the foundation for both.
- Agent behavior is hard to reason about statically, so trace-based experiments are essential for improvements.