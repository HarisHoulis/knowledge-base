---
domain: engineering-culture
subdomain: proprietary-trading-engineering
concept: prop-trading-engineering
title: Software engineering at a proprietary trading company: Optiver
sources:
  - title: "Software engineering at a proprietary trading company: Optiver"
    url: "https://newsletter.pragmaticengineer.com/p/optiver"
    author: "Gergely Orosz"
    date: "2026-08-11"
---

# Software engineering at a proprietary trading company: Optiver

This deep dive by Gergely Orosz (Pragmatic Engineer, 2026) explores software engineering at Optiver, a proprietary trading firm. Unlike typical tech companies, Optiver has no external customers; its own trading business is the customer. This creates distinct incentives: high emphasis on personal motivation and speed, balanced by an extreme caution to avoid costly bugs like the Knight Capital incident. The article highlights that latency is the historical "enemy number one," but today ultra-low latency is no longer a competitive moat—AI models and trading strategies have become differentiators (Orosz, 2026).

The engineering organization has shifted from regional silos (1986–2020) to global platforms (2020–present), aiming to reduce fragmentation and duplication. With ~950 engineers, the company emphasizes a "build and own" culture and is rebuilding its CI system for cross-regional scalability. The tech stack spans custom hardware, FPGAs, and kernel-level work to minimize latency, while network infrastructure includes co-located data centers and microwave links. Notably, AI infrastructure providers like NVIDIA actively court trading firms due to their heavy GPU spending, and AI labs increasingly recruit from prop shops for their expertise in operating data centers and building high-performance custom hardware (Orosz, 2026).

- No external customers means different engineering incentives: internal motivation is highly valued, but risk avoidance is critical due to the catastrophic potential of bugs.
- Latency minimization has driven custom hardware and kernel-level engineering, but competitive advantage is shifting toward AI models and quantitative trading strategies.
- Optiver moved from regional, fragmented engineering to global platforms to reduce duplication and standardize infrastructure, with platform engineering now a major focus.
- The company's 'build and own' culture spans the full stack, from hardware (FPGAs, custom chips) to software (CI/CD, data layers), and includes sub-nanosecond trading systems.
- AI labs are recruiting from prop shops like Optiver due to their deep infrastructure expertise and custom high-performance hardware skills.