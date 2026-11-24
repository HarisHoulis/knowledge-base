---
domain: ai-workflows
subdomain: coding-agents
concept: anti-slop-software-factory
title: 12 Rules for a Software Factory That Doesn't Ship Slop
sources:
  - title: "12 Rules for a Software Factory That Doesn't Ship Slop — Dex Horthy, Factory"
    url: "https://www.youtube.com/watch?v=-NFMsM2y0Vk"
    author: "AI Engineer"
    date: "2026-11-23"
---

# 12 Rules for a Software Factory That Doesn't Ship Slop

Dex Horthy argues that "software factories" built on coding agents are not a new paradigm but simply good engineering with agents doing the building. He grounds the talk in Slop Code Bench, a benchmark measuring how well agents evolve a codebase over time, where the best model scores only about 16% — evidence that models are poor at maintaining code over the long run. The talk frames the problem as a war on slop, with the enemy being models' inability to sustain code quality across iterations.

Horthy's framework centers on two forces: forward pressure (pushing work through the pipeline) and back pressure (constraints that keep output quality high). From this he derives 12 practices for software factories, including planning before building, aligning visually and letting agents test, fighting slop with lint rules, and using feature flags, evals, and a unified forge. He also distinguishes what you can't simply buy — the practices and discipline that must be built in-house.

The talk culminates in the Anti-Slop Manifesto (slopmanifesto.com) and a defense of code review: even with agents doing the building, reviewing work still matters. The overall message is that agent-driven development succeeds when paired with the same rigor — planning, constraints, testing, and review — that good engineering has always required.

- The best model scores only ~16% on Slop Code Bench, which tests how agents evolve a codebase over time
- Software factories are just good engineering with agents doing the building, not a new paradigm
- Balance forward pressure (shipping work) with back pressure (quality constraints)
- Fight slop with planning, visual alignment, agent testing, lint rules, feature flags, evals, and a unified forge
- Reviewing work still matters even when agents do the building