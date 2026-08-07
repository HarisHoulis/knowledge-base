---
domain: ai-workflows
subdomain: subagent orchestration
concept: orchestrator-context-protection
title: The Orchestrator's Tax
sources:
  - title: "The Orchestrator's Tax"
    url: "https://martinfowler.com/articles/orchestrator-tax.html"
    author: "Martin Fowler"
---

# The Orchestrator's Tax

The article discusses the real value of subagents in AI workflows, arguing that their primary benefit is not time saved or parallel execution, but rather the protection of the orchestrator's context window. According to Rahul Garg's insights, every token in the orchestrator's context competes for its attention, so offloading reasoning to subagents keeps the orchestrator's working memory free and focused. The article emphasizes that subagents should be treated as a tool for context management, not merely for task delegation. To do this effectively, the orchestrator must be given explicit ground rules for when and how to delegate, ensuring that delegation is intentional and beneficial rather than haphazard. This perspective shifts the design focus from maximizing subagent throughput to minimizing orchestrator cognitive load, leading to more efficient and reliable multi-agent systems (Fowler, 'The Orchestrator's Tax').

- Subagents are justified by their ability to keep irrelevant tokens out of the orchestrator's context, not by parallel execution.
- Every token in the orchestrator's context competes for attention, so reducing context noise improves overall performance.
- Effective delegation requires explicit ground rules that tell the orchestrator when and how to use subagents.
- Designing subagent workflows should prioritize protecting the orchestrator's working memory over raw speed.