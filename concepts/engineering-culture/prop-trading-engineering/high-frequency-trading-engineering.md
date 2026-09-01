---
domain: engineering-culture
subdomain: prop-trading-engineering
concept: high-frequency-trading-engineering
title: Software Engineering at Optiver: Engineering Culture and Practices at a Proprietary Trading Firm
sources:
  - title: "Software engineering at a proprietary trading company: Optiver"
    url: "https://newsletter.pragmaticengineer.com/p/optiver"
    author: "Gergely Orosz"
    date: "2026-08-11"
---

# Software Engineering at Optiver: Engineering Culture and Practices at a Proprietary Trading Firm

This deep dive from The Pragmatic Engineer explores how software engineering operates at Optiver, a leading proprietary trading firm. Unlike typical tech companies, Optiver has no external customers—its own business is the customer—and nearly every engineering decision is driven by minimizing latency, which is described as "enemy number one." The article explains the evolution of trading from pre-electronic to quantitative trading, and how today the competitive edge is shifting from raw latency to machine learning models and AI-driven decision-making. Optiver's engineering culture emphasizes caution and risk management because a single software bug could be catastrophic, as illustrated by the Knight Capital cautionary tale. The company has moved from fragmented regional systems to global platforms, investing heavily in platform engineering to build for scale and reuse across regions. The report also covers the tech stack, hardware engineering with custom FPGAs, network infrastructure, AI adoption, and hiring culture, highlighting the unique challenges and incentives of working in high-frequency trading.

- Optiver has no external customers; the business itself is the customer, which changes incentives and removes external deadlines.
- Latency is the primary engineering driver, with custom hardware, FPGAs, and low-level kernel work all aimed at shaving nanoseconds.
- The industry has shifted from pure automated trading to quantitative trading, where ML models and AI are becoming key differentiators.
- Optiver is consolidating from fragmented regional systems to global platforms, with a rebuilt CI system designed for scale and multi-region use.
- Engineering culture balances extreme speed with high caution due to the existential risk of bugs, emphasizing knowledge sharing and robust testing.