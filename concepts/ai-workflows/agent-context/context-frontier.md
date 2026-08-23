---
domain: ai-workflows
subdomain: agent-context
concept: context-frontier
title: Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked
sources:
  - title: "Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked"
    url: "https://www.youtube.com/watch?v=HvMyYLTfvhg"
    author: "AI Engineer"
    date: "2026-08-21T17:00:30+00:00"
---

# Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked

In this talk, Jeff Ng argues that the heavy lifting for building AI agents has been commoditized over the past six months. Previously, launching an agent required a dedicated team and a quarter of work to handle state persistence, sandboxed execution, observability, and other infrastructure concerns. Now, cloud providers like Cloudflare, Vercel, and AWS, combined with frameworks such as Flu, Vercel AI SDK, and Maestra, abstract away these "taxes" so developers can focus on core agent logic. Defining an agent is now as simple as choosing a model, writing a system prompt, and specifying tools and sandbox location (Ng, 2026).

Ng illustrates this with an issue enrichment agent for Linear built on Flu and Cloudflare. The agent fetches a Linear ticket, searches the codebase, and proposes next steps. In the demo, the agent confidently recommends re-enabling async dispatch to improve QA pipeline performance. However, that async dispatch had actually caused a recent outage, making the recommendation confidently wrong. This leads to Ng's central thesis: building agents is trivial now, but context is the next frontier. The remaining challenge is not constructing the agent, but ensuring it has the right context to reason correctly and avoid plausible yet incorrect outputs (Ng, 2026).

- Agent infrastructure (state persistence, sandboxing, observability) is now largely handled by cloud primitives and frameworks.
- Defining an agent requires only model selection, system prompt, tools, and sandbox configuration.
- The demo of a Linear issue enrichment agent shows a plausible but incorrect recommendation, highlighting the context problem.
- As building agents becomes easier, providing the right context becomes the primary challenge to ensure reliable outputs.