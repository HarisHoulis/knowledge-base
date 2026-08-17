---
domain: ai-workflows
subdomain: agent-development
concept: tdd-in-agent-loop
title: TDD inside the agent loop - theater or actual value?
sources:
  - title: "TDD inside the agent loop - theater or actual value?"
    url: "https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html"
    author: "Martin Fowler"
---

# TDD inside the agent loop - theater or actual value?

In this article from the Exploring Gen-AI series, Martin Fowler discusses the common practice of instructing LLM agents to use Test-Driven Development (TDD) when generating software. He notes that many in the industry advocate this approach, and that his Thoughtworks colleagues are generally strong proponents of TDD. However, the actual impact of this guidance on agent-generated code remains an open question, prompting curiosity about whether TDD is genuinely useful or merely a performative addition to agent workflows.

To investigate, Birgitta Böckeler conducted a few experiments comparing scenarios with and without TDD prompts in the agent loop. These experiments aim to empirically assess whether TDD changes the quality or correctness of the produced software. By sharing these experiments, the article contributes evidence to the broader discussion on effective practices for AI-assisted software development, helping developers understand if TDD inside the agent loop delivers tangible value or is just theater.

The article serves as a practical exploration of a widely recommended practice, offering data and observations to guide developers in deciding how to structure prompts for LLM agents. It highlights the need for empirical evaluation of AI coding practices rather than relying on conventional wisdom alone.

- TDD is a widely advocated practice for LLM agents in software development.
- Birgitta Böckeler conducted experiments to evaluate the impact of TDD on agent-generated code.
- The article presents these experiments as part of the Exploring Gen-AI series, aiming to determine whether TDD offers tangible value.
- The practice may or may not be beneficial; the experiments provide evidence for the discussion.