---
domain: ai-workflows
subdomain: agent-orchestration
concept: declarative-agent-programming
title: Stop Telling Agents How: Declarative Contracts for Agent Systems (OpenProse)
sources:
  - title: "Stop Telling Agents How — Dan Barrett, Raymond Weitekamp & Jose Montes de Oca, OpenProse"
    url: "https://www.youtube.com/watch?v=7T-gldvgfpo"
    author: "AI Engineer"
    date: "2026-10-18"
---

# Stop Telling Agents How: Declarative Contracts for Agent Systems (OpenProse)

Dan Barrett, creator of OpenProse, argues that as prompting, context engineering, and agent orchestration tooling mature, the remaining hard problem is communicating intent: getting what you want from your brain into a capable system. He frames OpenProse as a language and framework built on the belief that language is a creative force—you write a sentence and the device makes it true—so the interesting question becomes what sentence you choose to write now that the machine can execute it.

Barrett traces the evolution of the skill: early token-level prompting gave way to manually assembling context from search results and tool calls (context engineering), then to tools that fill context automatically, and now to self-modifying topologies of orchestrator and sub-agents that would have been unthinkable a year earlier. With context and supporting systems increasingly solved, he positions the next step as naming what you need and letting the supporting system self-organize and run whatever cycles are required to achieve the goal.

The team's answer borrows classical software engineering patterns: write queries compositionally rather than through inheritance, declaratively rather than procedurally, stating the desired outcome as a contract instead of prescribing steps. Telling the agent *how* to do something wastes intelligence and cost, since a more capable model can figure out the method itself. Compositional contracts also let teams combine elements elegantly and manage complexity locally across many parts of a system.

Co-presenters Raymond Weitekamp (PhD, two-time founder, interface designer) and Jose Montes de Oca (early Google Cloud developer) bring engineering and design experience to this approach, with demos following the conceptual framing.

- The enduring problem is communicating intent from human to agent, regardless of model or hardware advances.
- Prescribe outcomes as declarative contracts, not step-by-step procedures—telling agents how wastes model intelligence and cost.
- Borrow classical software patterns: composition over inheritance, declarative over imperative, local complexity management.
- Once you can name what you need, supporting systems can self-organize and run the cycles to achieve it.