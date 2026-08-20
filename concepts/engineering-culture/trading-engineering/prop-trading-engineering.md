---
domain: engineering-culture
subdomain: trading-engineering
concept: prop-trading-engineering
title: Software engineering at a proprietary trading company: Optiver
sources:
  - title: "Software engineering at a proprietary trading company: Optiver"
    url: "https://newsletter.pragmaticengineer.com/p/optiver"
    author: "Gergely Orosz"
    date: "2026-08-11"
---

# Software engineering at a proprietary trading company: Optiver

The Pragmatic Engineer's deep dive into Optiver reveals how software engineering operates in a proprietary trading firm, where the business itself is the only customer. Unlike typical startups or Big Tech, there are no external deadlines, but a single bug could wipe out the company, as the cautionary tale of Knight Capital's $440M loss illustrates. Engineering decisions are dominated by minimizing latency—the 'enemy number one'—which drives custom hardware, FPGA development, and kernel-level optimization. However, the article notes that ultra-low latency is no longer a sufficient competitive moat; today, machine learning models and quantitative strategies are becoming the key differentiators (Orosz, 2026).

Optiver's engineering organization has transitioned from regional 'unblock yourself' systems to global platforms since around 2020, with a strong push toward platform engineering. The tech stack spans three layers, and the company builds its own hardware, including custom chips in partnership with AMD. Network infrastructure includes dedicated fiber, microwave links, and co-located data centers. The engineering culture emphasizes a cautious attitude toward risk while moving fast, with a strong focus on testing, monitoring, and knowledge sharing. AI adoption is accelerating, and the company invests more in building better models than in lowering latency. The article also highlights that AI labs like Anthropic and OpenAI recruit from prop shops due to their expertise in custom hardware and infrastructure (Orosz, 2026).

- Optiver operates with no external customers, which changes incentives: the business itself is the customer, and engineering success directly impacts profitability.
- Latency is the top engineering priority, but the industry has shifted from competing purely on speed to differentiating via machine learning models and quantitative strategies.
- The engineering org evolved from fragmented regional systems to global platforms, with a growing emphasis on platform engineering and standardized CI/CD.
- Trading firms like Optiver build custom hardware, including FPGAs and silicon, and maintain advanced network infrastructure like microwave links to shave off nanoseconds.
- AI is a major focus, both for trading models and internal engineering tooling; prop-shop engineers are sought after by AI labs for their infrastructure and high-performance computing expertise.