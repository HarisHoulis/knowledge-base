---
domain: ai-workflows
subdomain: agent-evaluation
concept: simulation-based-agent-evaluation
title: Using Dynamic Simulation to Evaluate AI Agents
sources:
  - title: "Podcast: Simulation Can Tell You What Your Agents are Actually Doing: A Conversation with Zhou Yu"
    url: "https://www.infoq.com/podcasts/simulation-agents-actually-doing/"
    author: "Zhou Yu"
    date: "2026-11-23"
---

# Using Dynamic Simulation to Evaluate AI Agents

In this InfoQ podcast, Zhou Yu speaks with Michael Stiefel about why static, reference-based benchmarks fall short for evaluating AI agents, particularly conversational agents whose actions depend on prior responses. Because LLM behavior is non-deterministic, a fixed set of reference answers cannot capture how an agent will actually behave across real interactions.

Yu argues that agents should instead be tested through dynamic simulations that model different personas, goals, and corner cases. Such simulations let evaluators observe what agents are actually doing in context, rather than only checking outputs against a static expected answer.

The core takeaway is that agent evaluation needs to be interactive and scenario-driven, reflecting the branching, response-dependent nature of real agent behavior.

- Static, reference-based benchmarks are insufficient for non-deterministic LLM agents
- Conversational agents' actions depend on prior responses, so evaluation must be dynamic
- Simulations should incorporate varied personas, goals, and corner cases
- Simulation reveals what agents are actually doing rather than only matching expected outputs