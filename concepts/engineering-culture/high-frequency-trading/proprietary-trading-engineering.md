---
domain: engineering-culture
subdomain: high-frequency-trading
concept: proprietary-trading-engineering
title: Software engineering at a proprietary trading company: Optiver
sources:
  - title: "Software engineering at a proprietary trading company: Optiver"
    url: "https://newsletter.pragmaticengineer.com/p/optiver"
    author: "Gergely Orosz"
    date: "Tue, 11 Aug 2026 16:17:39 GMT"
---

# Software engineering at a proprietary trading company: Optiver

Optiver is a proprietary trading firm that trades only its own capital, with no external customers. Engineering is uniquely focused on minimizing latency, driving decisions from software architecture to custom hardware manufacturing. The company has ~950 engineers and executes 10M+ trades daily across 100 exchanges. This environment differs from Big Tech in that there are no external deadlines, but a single software bug could be catastrophic, as illustrated by the Knight Capital incident.

The article details how trading has evolved through four eras, with quantitative trading now dominant, where ML models are becoming a key differentiator over raw latency. Optiver's engineering organization emphasizes platform engineering, a 'build and own' culture, and a three-layer tech stack. The company invests heavily in custom hardware, FPGAs, and network infrastructure, including microwave links and co-location. Engineering practices balance speed with caution, with a strong focus on testing, monitoring, and risk management.

Notably, AI is being integrated into workflows, and AI labs like Anthropic and OpenAI are recruiting from prop shops due to their infrastructure and hardware expertise. Optiver's engineering culture values personal motivation and knowledge-sharing, and the company has recently shifted from regional systems to global platforms to reduce fragmentation and duplication.

- Optiver has no external customers; the business itself is the customer, leading to different incentives and a premium on caution to avoid catastrophic losses.
- Latency is the primary engineering driver, but is no longer a competitive moat; ML models and quantitative strategies are increasingly the differentiator.
- Optiver builds custom hardware, including FPGAs and specialized network infrastructure, to achieve sub-nanosecond trading speeds.
- The company is moving from fragmented regional systems to global platforms, with a strong platform engineering team led by Pat Cooney.
- AI is being adopted in engineering workflows, and trading firms are a talent source for AI labs due to their infrastructure and high-performance computing expertise.