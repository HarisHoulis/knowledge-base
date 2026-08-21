---
domain: ai-workflows
subdomain: agent-context
concept: context-engineering
title: Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked
sources:
  - title: "Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked"
    url: "https://www.youtube.com/watch?v=HvMyYLTfvhg"
    author: "Jeff Ng"
    date: "2026-08-21T17:00:30+00:00"
---

# Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked

Jeff Ng, a founding engineer at Unblocked, argues that building AI agents has become dramatically easier over the past six months. Previously, shipping an agent required a dedicated team and a quarter of work to build supporting systems like checkpointing and state persistence, sandbox infrastructure, and observability. Those systems are 'taxes'—they don't improve agent capabilities but are necessary for production. Now, cloud providers and frameworks such as Cloudflare, Vercel, and Mastra have turned these into primitives, so defining an agent reduces to selecting a model, writing instructions, exposing tools, and choosing a sandbox location (Ng, 2026).

To illustrate, Ng built a Linear issue enrichment system using Flow and Cloudflare. The agent fetches a ticket, searches code, and proposes next steps. In a real example, the agent incorrectly recommended re-enabling async dispatch—a change that had already caused an outage and was explicitly disabled by a support engineer. This demonstrates that while the mechanics of agent building are now trivial, the real challenge is context: agents need the right code, history, and situational understanding to avoid confidently wrong answers. The next frontier is giving agents meaningful, accurate, and relevant context (Ng, 2026).

- Agent infrastructure has been commoditized by cloud primitives and frameworks, reducing the need for custom in-house systems.
- Defining an agent now requires only a model, system prompt, tools, and sandbox—complexity has shifted to the framework layer.
- Checkpointing, sandboxing, and observability remain essential but are now base-level responsibilities, not differentiators.
- A practical example shows an agent misdiagnosing a production issue, proving that missing context causes confident failures.
- Context engineering is the next bottleneck: gathering and reasoning over the right code, ticket history, and team knowledge is what separates useful agents from dangerous ones.