---
domain: ai-workflows
subdomain: llm-inference-economics
concept: tokenomics
title: The AI Bill Is Too Damn High: Tokenomics 101
sources:
  - title: "The AI Bill Is Too Damn High: Tokenomics 101 — Eugene Cheah, Featherless AI"
    url: "https://www.youtube.com/watch?v=Ti-BmGU1_mQ"
    author: "AI Engineer"
    date: "2026-10-17"
---

# The AI Bill Is Too Damn High: Tokenomics 101

Eugene Cheah, CEO and founder of Featherless AI, presents a framework for controlling large-scale LLM inference costs, which he calls "tokenomics." He frames the talk around four steps: measurement, sizing, procuring capacity, and process validation. He notes that Featherless serves clients processing up to 2 trillion tokens per day at roughly $0.3 per million tokens on private hardware, and cautions that the advice targets organizations spending more than about $10k per month — smaller spenders should focus on finding compelling use cases instead of optimizing token accounts.

The first and most emphasized step is measurement. Cheah polls the audience and finds only about half know their total token spend, fewer can measure it at the department level, and fewer still at the team or task level. He reports that 30-40% of incoming clients initially used a single shared API key across the whole organization, making attribution impossible. His remedy is to separate keys and allocate them by department and main task so spend can be traced and workloads optimized.

Once spend is attributable, teams can right-size resources: some teams deserve a certain tokens-per-second rate, while background agents running overnight do not need premium "Ultra" plans. Usage analysis also informs planning of dedicated capacity for both open and closed models, and reveals which teams consume the most tokens and whether that consumption is productive.

Cheah distinguishes two workload directions with opposing economics: long-running, multi-pass agent workloads such as coding agents that run overnight with multiple compactions and maximize context use, versus process automation such as call centers, email routing, and meeting notes.

- Measure token spend at total, department, team, and task levels; shared API keys (common in 30-40% of new clients) make attribution impossible.
- Allocate separate API keys by department and main task to enable optimization and capacity planning.
- Right-size resources to workload: background agents don't need premium per-second plans.
- Agent workloads (long multi-pass, context-heavy) and process automation have diametrically opposed economics.
- Below roughly $10k/month spend, prioritize finding compelling use cases over token-cost optimization.