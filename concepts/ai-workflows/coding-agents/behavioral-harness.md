---
domain: ai-workflows
subdomain: coding-agents
concept: behavioral-harness
title: Are Harnesses Worth the Cost?
sources:
  - title: "Are Harnesses Worth the Cost?"
    url: "https://martinfowler.com/articles/are-harnesses-worth-the-cost.html"
    author: "Martin Fowler"
---

# Are Harnesses Worth the Cost?

Naresh Jain compares coding agents building the same API service with and without a behavioral harness. A frontier model, GPT-6 Sol, passed every external evaluation either way. But a cost-optimized model, GPT-6 Luna, succeeded in only 3 of 10 unharnessed runs and all 10 with the harness.

While adding the harness increased token usage and runtime for Luna, the harnessed Luna runs achieved the same 10-for-10 reliability as GPT-6 Sol while costing 33% less per run ($0.273 vs $0.406). This experiment suggests a behavioral harness might be a practical way to get dependable results from smaller, cost-optimized models.

- A behavioral harness took a cost-optimized model (GPT-6 Luna) from 3/10 to 10/10 successful runs.
- The frontier model (GPT-6 Sol) passed all evaluations with or without the harness.
- Harnessed Luna runs matched Sol's 10-for-10 reliability at 33% lower cost per run ($0.273 vs $0.406).
- The harness increased token usage and runtime for Luna.