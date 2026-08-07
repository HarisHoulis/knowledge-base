---
domain: ai-workflows
subdomain: data-quality
concept: data-quality-compute-multiplier
title: Data Quality Is the Compute Multiplier
sources:
  - title: "Data Quality Is the Compute Multiplier — Ari Morcos, DatologyAI"
    url: "https://www.youtube.com/watch?v=_PdK6x7PQNM"
    author: "AI Engineer"
    date: "2026-07-31T23:00:06+00:00"
---

# Data Quality Is the Compute Multiplier

Ari Morcos, CEO of DatologyAI, argues that data quality is an overlooked compute multiplier in an era of scarce compute. He notes that H100 prices have risen ~40% from lows, reasoning models consume 8x tokens, and token usage is projected to 5x again, leading to API access restrictions and token futures. Improving data quality shifts the performance-vs-compute curve upward, yielding comparable performance with far less compute or better performance with the same compute.

The key is maximizing the marginal information gain per data point. There is no universal golden dataset; data must be relevant to target tasks, diverse to avoid brittleness, and properly mixed across sources. DatologyAI acts as an 'oil refinery' for data, applying four C's: clean, curate, create, and compose. Cleaning involves heuristics like filtering short documents; curation selects relevant data; creation synthesizes new data; composition optimally mixes sources to drive model improvement.

- Compute is increasingly scarce, making data quality a critical lever for improving model performance.
- Data quality multiplies compute: better data yields steeper learning curves, enabling similar performance with less compute or higher performance with the same budget.
- Optimal data must be task-relevant, diverse, and correctly composed from multiple sources.
- DatologyAI's approach: clean, curate, create, and compose existing tokens to maximize signal per token.