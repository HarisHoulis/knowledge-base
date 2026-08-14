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

The article, authored by Martin Fowler, investigates whether instructing LLM-powered coding agents to follow Test-Driven Development (TDD) yields tangible benefits or simply adds ritualistic behavior. Fowler references experiments conducted by colleague Birgitta Böckeler, who set out to test the common industry assertion that TDD improves agent-generated code.

The experiments explored how agent behavior and output quality change when TDD is explicitly required. Preliminary findings suggest that TDD can provide structure and verification checkpoints, but its value depends on the context and how rigorously the agent adheres to the cycle. Fowler frames the discussion around whether TDD in the agent loop is 'theater' (looking good without real impact) or 'actual value' (measurably improving outcomes), encouraging practitioners to critically evaluate their use of TDD with AI agents.

- Many practitioners advocate telling LLM agents to use TDD, but empirical evidence is needed to validate this practice.
- Birgitta Böckeler conducted experiments to test whether TDD truly makes a difference in agent-based software development.
- The article questions whether TDD in the agent loop is performative theater or provides measurable value.
- The value of TDD likely depends on how it is implemented and the specific context of the agent's task.