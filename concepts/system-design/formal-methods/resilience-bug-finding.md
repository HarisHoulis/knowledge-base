---
domain: system-design
subdomain: formal-methods
concept: resilience-bug-finding
title: Finding Resilience Bugs in Systems That Don't Exist
sources:
  - title: "Presentation: How to Find Resilience Bugs in Systems that Don't Exist"
    url: "https://www.infoq.com/presentations/formal-methods-principles/"
    author: "Hillel Wayne"
    date: "2026-10-14"
---

# Finding Resilience Bugs in Systems That Don't Exist

Hillel Wayne presents formal methods principles as practical mental models for uncovering architectural bugs early, before systems are built. Rather than requiring complex mathematical tools, he argues that concepts like property strength, state-space verification, and environment assumptions can help engineers reason about failure modes in distributed systems.

A central technique he highlights is "adversarial non-determinism" — deliberately imagining an adversary that drives a system toward its worst-case interleavings. This framing helps engineers reason about concurrency, edge cases, and distributed failures without needing to construct the full system first.

By applying these principles to hypothetical or not-yet-existing systems, teams can surface critical resilience bugs during design rather than after implementation, when fixes are far more expensive.

- Formal methods principles can be applied as lightweight mental models, not heavyweight math
- Property strength, state-space verification, and environment assumptions are key lenses for finding bugs
- "Adversarial non-determinism" helps reason about concurrency and distributed failure modes
- Applying these techniques to systems that don't yet exist surfaces architectural bugs early