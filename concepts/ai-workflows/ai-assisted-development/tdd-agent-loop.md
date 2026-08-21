---
domain: ai-workflows
subdomain: ai-assisted-development
concept: tdd-agent-loop
title: TDD inside the agent loop - theater or actual value?
sources:
  - title: "TDD inside the agent loop - theater or actual value?"
    url: "https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html"
    author: "Martin Fowler"
---

# TDD inside the agent loop - theater or actual value?

This article investigates whether instructing LLM agents to use Test-Driven Development (TDD) genuinely improves the software they produce, or whether it is merely performative. Thoughtworks colleague Birgitta Böckeler conducted a series of experiments to compare agent behavior with and without explicit TDD instructions. The results indicate that TDD can have value in agent-driven development, but its effectiveness is not universal and may depend on context. The article cautions against treating TDD as a silver bullet for agent workflows, while acknowledging that it can help structure the agent's process and validate outputs in certain scenarios.

- TDD instructions to LLM agents are not always effective; results vary across experiments.
- Birgitta Böckeler's experiments provide empirical evidence on the impact of TDD in agent loops.
- The article questions whether TDD is genuinely valuable or just theater in AI-assisted development.
- Context and task complexity likely influence whether TDD helps or hinders agent performance.