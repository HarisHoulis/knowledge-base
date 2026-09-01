---
domain: system-design
subdomain: trading-systems
concept: proprietary-trading-engineering
title: Software engineering at a proprietary trading company: Optiver
sources:
  - title: "Software engineering at a proprietary trading company: Optiver"
    url: "https://newsletter.pragmaticengineer.com/p/optiver"
    author: "Gergely Orosz"
    date: "2026-08-11"
---

# Software engineering at a proprietary trading company: Optiver

The Pragmatic Engineer's deep dive into Optiver reveals how software engineering operates at a proprietary trading firm where the business itself is the only customer. Unlike Big Tech or startups, there are no external clients or product deadlines; instead, engineering decisions are driven by the need to outcompete rivals in speed and model accuracy. The article emphasizes that latency is 'enemy number one,' shaping investments in custom hardware, FPGAs, kernel-level work, and even physical infrastructure like microwave links between data centers (Pragmatic Engineer, 2026).

Optiver's engineering organization has shifted from regional, self-service systems to global platforms built for the whole company, a change reflected in the rise of a dedicated platform engineering team. The tech stack spans three layers, and engineering roles are split among engineering, research, and trading, with a 'build and own' culture. Today, ultra-low latency alone is no longer a moat; quantitative trading and AI models are becoming key differentiators, though machine learning complements rather than replaces mathematical modeling (Pragmatic Engineer, 2026).

The report also highlights the high bar for hiring, competitive compensation, and the cautionary tale of Knight Capital, where a single bug caused a $440M loss. This drives a culture that balances speed with rigorous risk management. Optiver is also noted for its large platform engineering team, custom hardware stacks, and growing investment in global CI/CD systems (Pragmatic Engineer, 2026).

- Proprietary trading firms have no external customers; their own business is the customer, leading to different incentives focused on competitive edge and personal motivation.
- Latency minimization drives nearly every major engineering decision, from custom FPGAs and hardware to kernel-level and network infrastructure work.
- The industry has evolved through four eras: pre-electronic, electronification, automated trading, and today's quantitative trading, where AI models are a differentiator alongside latency.
- Optiver is globalizing its engineering platforms, moving from fragmented regional systems to global platforms built for scale and cross-region use.
- Engineering roles are divided into engineering, research, and trading, with a 'build and own' culture and a high premium on caution due to the risk of catastrophic trading bugs.