---
domain: ai-workflows
subdomain: llm-cost-optimization
concept: model-tiering
title: Fable and the End of the Free Lunch
sources:
  - title: "Fable & The End of the Free Lunch"
    url: "https://www.dbreunig.com/2026/08/23/fable-the-end-of-moore-s-law.html"
    author: "Drew Breunig"
    date: "2026-08-23"
---

# Fable and the End of the Free Lunch

Drew Breunig reflects on how the release of Anthropic's Fable model changed his team's approach to LLM usage. Previously, they saw little value in optimizing coding harnesses or context strategies, because each new model would arrive at the same or lower price and conveniently solve most problems. Fable, however, is dramatically more expensive, while other models like Opus, 5.6, K3, and GLM are 'good enough' for the majority of their coding needs. This cost pressure forced them to think deliberately about which tasks warrant the premium model and which can be delegated to cheaper alternatives, marking an end to the era of ignoring cost in model selection.

- Before Fable, new LLM models would arrive at the same price and fix previous shortcomings, so optimizing workflows felt wasteful.
- Fable is extremely capable but also very expensive, creating a real cost trade-off.
- For most coding tasks, older or cheaper models like Opus, 5.6, K3, and GLM are sufficient.
- Teams must now decide which work goes to premium versus budget models, introducing cost-aware model routing.
- This shift signals the end of the 'free lunch' in LLM progress, where better models no longer automatically replace the need for workflow optimization.