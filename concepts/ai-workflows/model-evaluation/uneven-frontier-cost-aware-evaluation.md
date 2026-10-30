---
domain: ai-workflows
subdomain: model-evaluation
concept: uneven-frontier-cost-aware-evaluation
title: The Cheaper AI Model That Costs You More
sources:
  - title: "The Cheaper AI Model That Costs You More - Rayan Krishnan, Vals AI"
    url: "https://www.youtube.com/watch?v=rWtbOgl5FTU"
    author: "AI Engineer"
    date: "2026-10-30"
---

# The Cheaper AI Model That Costs You More

Rayan Krishnan of Vals AI argues that aggregate benchmark scores on model cards hide an "uneven frontier" of performance: within a single domain or task set, models show inconsistent results that a single headline number obscures. This fragmentation becomes even more pronounced when benchmarks are broken down by programming language and library, and it ignores the fact that models can be optimized for cost and latency as well as raw performance, so generic model-card benchmarks may not apply to how people actually use models.

He ties this to economics: corporate AI spending is roughly doubling year over year, yet ROI remains hard to pin down—adoption is around 90% while only about 7% report clear ROI. Organizations that can track AI cost and spend are more likely to understand where returns come from, and inability to quantify cost-benefit is itself a major obstacle to adoption.

A concrete example shows why intuition misleads: a second-tier model priced lower per token ($4/$20 vs $10/$50) turned out 14 times more expensive on a tax benchmark because the less capable model burned more tokens attempting the task—while still scoring 3% lower. The takeaway is that frontier intelligence can be both cheaper and better in practice, and teams need diligent, cost-aware evaluation rather than relying on lab-provided intuitions.

- Aggregate model-card scores mask an uneven frontier of inconsistent per-task and per-domain performance.
- Lower per-token pricing can be far more expensive in practice: a cheaper model cost 14x more on a tax benchmark by spending more tokens while scoring 3% lower.
- AI adoption is high (~90%) but reported ROI is low (~7%), and inability to quantify cost-benefit blocks adoption.
- Teams that track AI spend are better positioned to understand where ROI comes from.
- Cost-aware, task-specific evaluation is needed over generic benchmark intuitions.