---
domain: ai-workflows
subdomain: tdd-agent-loop
concept: tdd-in-agent-loop
title: TDD inside the agent loop - theater or actual value?
sources:
  - title: "TDD inside the agent loop - theater or actual value?"
    url: "https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html"
    author: "Martin Fowler"
---

# TDD inside the agent loop - theater or actual value?

This article by Martin Fowler explores whether test-driven development (TDD) genuinely improves outcomes when used with AI coding agents, or if it is merely ceremonial. The investigation, led by Birgitta Böckeler at Thoughtworks, involved a few experiments to evaluate the practical impact of instructing LLM agents to follow TDD practices. The key question is whether the discipline of writing tests first helps the agent produce better code, reduce bugs, or improve maintainability, or if it just adds overhead without tangible benefits. The article summarizes the experiments and their findings, discussing conditions under which TDD inside the agent loop might be valuable versus when it is not. It also considers how the nature of AI-generated code and the agent's ability to iterate quickly might change the traditional TDD calculus.

- The article investigates whether TDD instructions to AI agents produce measurable benefits or are just for show.
- Experiments were conducted to compare agent behavior with and without TDD requirements.
- Findings suggest TDD can be valuable in certain contexts, but may be unnecessary or even counterproductive in others.
- The value of TDD in the agent loop depends on task complexity, codebase maturity, and how strictly the agent follows the red-green-refactor cycle.