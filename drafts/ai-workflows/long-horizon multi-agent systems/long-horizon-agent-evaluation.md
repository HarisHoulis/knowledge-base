---
domain: ai-workflows
subdomain: long-horizon multi-agent systems
concept: long-horizon-agent-evaluation
title: Long-Horizon Agents Need Experiments, Not Just Prompts — Erina Karati
sources:
  - title: "Long-Horizon Agents Need Experiments, Not Just Prompts — Erina Karati"
    url: "https://www.youtube.com/watch?v=x4e5O9zN0TE"
    author: "AI Engineer"
    date: "2026-09-26"
---

# Long-Horizon Agents Need Experiments, Not Just Prompts — Erina Karati

Erina Karati, a former engineer at Microsoft and Supercell, discusses how to evaluate and improve agents that maintain state over time, using a multi-agent AI village as an example. In Supercell's AI Innovation Lab, she and Arunachalam Manikandan developed the Paradox project, a modular framework for autonomous agents in video games that can move purposefully, interact with objects, react to events, hold conversations, and form memories influenced by emotions and curiosity (Karati, 2026).

The architecture was built for state preservation. Each agent has its own RAG-backed memory space so memories are not mixed; emotions are tracked as a small vector updated after events or conversations; agents maintain trust scores for other agents and the player, essentially a trust matrix; and memories receive importance ratings, with high-importance events stored in a separate cache for better retrieval later (Karati, 2026). Short-term gameplay worked well: a character could plan a sequence, move around, talk, remember recent interactions, and respond in context (Karati, 2026).

Over longer horizons, social coherence weakened. In an example, one agent spreads a rumor about a mango sale; after a series of intervening events, the system may remember the general topic but lose the source, treat a rumor as certainty, present it as fact, or fail to mention a known fact when planning (Karati, 2026). This raised the question of how to improve a multi-agent system for long-term social behavior, not just a single response (Karati, 2026).

Inspired by recent auto-research work, Karati proposes letting the system conduct experiments on itself: define scenarios, run agents, collect traces, evaluate behavior, and change only a small portion of the policy, keeping only successful changes. The goal is to move beyond manually configuring prompts or watching one nice demo (Karati, 2026).

- Long-horizon, stateful agents require evaluation beyond single responses or one-off demos.
- Paradox uses per-agent RAG memory, emotion vectors, trust scores, and importance-based memory caching to preserve state.
- Short-term social behavior worked in the picnic example, but long-horizon interactions lost information provenance and turned rumors into apparent facts.
- Karati proposes automated research loops: define scenarios, run agents, collect traces, evaluate behavior, and retain only policy changes that improve long-term social coherence.