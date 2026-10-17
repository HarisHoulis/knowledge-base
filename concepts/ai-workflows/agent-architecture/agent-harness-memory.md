---
domain: ai-workflows
subdomain: agent-architecture
concept: agent-harness-memory
title: Memory-Aware Agent Harnesses for Anti-Money Laundering
sources:
  - title: "Memory-Aware Agent Harnesses for Anti-Money Laundering — Nacho Martinez, Oracle"
    url: "https://www.youtube.com/watch?v=KtBivPzmOM8"
    author: "AI Engineer"
    date: "2026-10-17"
---

# Memory-Aware Agent Harnesses for Anti-Money Laundering

Nacho Martinez (Oracle) frames the agent stack as four layers: the application layer users interact with, the model that performs reasoning, the supporting infrastructure, and the data layer. He argues that practitioners have little influence over the model's internal decisions, so the interesting and customizable part is the harness — the surrounding scaffolding that includes memory, context engineering, and memory design (AI Engineer, 2026-10-17).

His central claim is that autonomous agents cannot solve long-horizon problems on their own because the context window is limited and large language models have no native memory. To let agents work autonomously for tens or hundreds of hours, memory components must be implemented by the developer rather than expected from the model. This is why he recommends focusing effort on the harness rather than chasing ever more advanced models.

To make the workshop concrete, he adapts it to banking: a medium-sized bank with many transactions, some of which are suspicious across five typologies — for example, a million-dollar deposit followed by $50,000 withdrawn from ATMs over three days. The goal is to process or flag these transactions autonomously so bank employees spend less time reviewing them. The workshop itself is delivered via GitHub registration and CodeSpaces environments, with a companion free course on building adaptive AI agents with Andrew Ng and DeepLearning.AI.

- The agent stack spans application, model, infrastructure, and data layers; the data/harness layer is where developers have the most control.
- LLMs lack native memory and have limited context windows, so memory and context engineering must be built into the harness for long-running autonomy.
- Effort is better spent customizing the harness than waiting on more advanced models.
- The anti-money-laundering case study uses a medium-sized bank with five suspicious-transaction typologies to show where autonomous flagging reduces human review load.