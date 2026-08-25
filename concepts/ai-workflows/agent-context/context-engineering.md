---
domain: ai-workflows
subdomain: agent-context
concept: context-engineering
title: Building Agents Is Trivial Now, Context Is the Next Frontier
sources:
  - title: "Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked"
    url: "https://www.youtube.com/watch?v=HvMyYLTfvhg"
    author: "AI Engineer"
    date: "2026-08-21T17:00:30+00:00"
---

# Building Agents Is Trivial Now, Context Is the Next Frontier

Jeff Ng, a founding engineer at Unblocked, argues that building AI agents has become dramatically easier over the past six months. Previously, standing up an agent required a dedicated team and a full quarter to handle systems like state persistence, sandboxing, and observability—what he calls 'taxes' that don't improve agent capabilities. Now, cloud providers (Cloudflare, Vercel, AWS) and frameworks (Flu, Vercel EvE, Mastra) have abstracted away these complexities, allowing developers to focus on the core agent logic. Defining an agent has been reduced to choosing a model, writing system instructions, selecting tools/skills, and specifying a sandbox location (Jeff Ng, Unblocked, 2026).

Ng demonstrates this simplicity with an issue enrichment system he built for Linear: the agent fetches a ticket, classifies it as bug or feature, searches code, and recommends next steps. However, the agent's recommendation in a real case was confidently wrong—it suggested re-enabling async dispatch, which had actually caused an outage and been explicitly disabled. This example illustrates that while the infrastructure for building agents is now trivial, the real challenge lies in providing agents with sufficient context to avoid such errors. Ng concludes that context is the next frontier: the key to making agents not just easy to build but genuinely reliable (Jeff Ng, Unblocked, 2026).

- Agent infrastructure has matured: cloud primitives and frameworks now handle checkpointing, sandboxing, and observability, making agent development far less resource-intensive.
- Defining an agent today is simply choosing a model, system prompt, tools, and sandbox—rather than building a suite of supporting services.
- Even with easy-to-build agents, they still fail by making confident but incorrect recommendations, as shown by the outage-inducing suggestion in the Linear example.
- The next frontier is context: ensuring agents have the right situational understanding to avoid producing plausible yet wrong outcomes.