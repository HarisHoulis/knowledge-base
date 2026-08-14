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

Birgitta Böckeler from Thoughtworks conducted experiments to evaluate whether instructing LLM agents to use Test-Driven Development (TDD) genuinely improves software generation outcomes. The article critically examines the common industry advocacy for TDD in agentic coding, questioning if it is merely performative or provides tangible benefits. While many developers assume TDD's discipline naturally transfers to AI agents, Böckeler's experiments reveal that the effect is nuanced and not universally positive. The findings suggest that TDD can help structure agent work and catch errors early, but its value depends heavily on the task complexity, test quality, and how strictly the agent adheres to the red-green-refactor cycle. The article also notes potential downsides, such as added cost and time without proportional quality gains in certain scenarios.

- TDD instructions to LLM agents can improve code correctness in some tasks, but the effect is inconsistent across experiments.
- The effectiveness of TDD in agent loops is highly dependent on the quality of tests generated and the agent's ability to iterate meaningfully.
- Blindly advocating TDD for agents may be 'theater' unless empirical validation shows clear value for the specific use case.
- The experimental results highlight the need for careful evaluation rather than following industry hype when using AI agents for software development.