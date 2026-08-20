---
domain: system-design
subdomain: performance-estimation
concept: napkin-math
title: Pushing Software Engineering Limits with "Napkin Math"
sources:
  - title: "Pushing software engineering limits with "napkin math""
    url: "https://newsletter.pragmaticengineer.com/p/pushing-software-engineering-limits"
    author: "Gergely Orosz"
    date: "2026-07-21"
---

# Pushing Software Engineering Limits with "Napkin Math"

In this article, Gergely Orosz interviews Simon Eskildsen, co-founder of turbopuffer, about his concept of "napkin math": doing quick, back-of-the-envelope calculations to estimate the theoretical limits of computer operations. This practice, which involves memorizing key numbers like memory bandwidth and cloud storage costs, allows engineers to challenge design decisions based on flawed benchmarks (Orosz, 2026). For example, if a database operation is supposed to take 10 milliseconds based on napkin math but a benchmark shows 10 seconds, something is wrong (Orosz, 2026).

Eskildsen's journey began with the International Olympiad for Informatics, where he learned algorithmic thinking and the value of starting over rather than digging holes (Orosz, 2026). These lessons carried into his eight years at Shopify, where he built Toxiproxy, a failure-injection proxy, and learned to write software that ages well; he observed that simple solutions often outlast complex, multi-team RFC-driven designs (Orosz, 2026).

Applying napkin math to search infrastructure, Eskildsen realized existing solutions were far more expensive than necessary, leading to the creation of turbopuffer. The article also covers his decision to raise limited VC funding and his perspective on when raising venture capital makes sense, including funding R&D and growth, rather than ego (Orosz, 2026).

- Napkin math is a superpower: using quick calculations and memorized key numbers to estimate performance limits and challenge benchmarks.
- Long tenure at a company can teach you to write software that ages well; simple solutions often outlast complex ones.
- Competitive programming (IOI) instills algorithmic thinking and perseverance, including knowing when to start over.
- Toxiproxy demonstrates solving real infrastructure problems with tooling that stands the test of time.
- Napkin math can reveal that existing products are far more expensive than necessary, enabling innovation like turbopuffer.