---
domain: ai-workflows
subdomain: llm-cost-optimization
concept: model-tier-routing
title: Quoting Drew Breunig: Fable and the End of the Free Lunch
sources:
  - title: "Quoting Drew Breunig"
    url: "https://simonwillison.net/2026/Aug/23/drew-breunig/"
    author: "Simon Willison"
    date: "2026-08-23"
---

# Quoting Drew Breunig: Fable and the End of the Free Lunch

Drew Breunig reflects on how the arrival of a very expensive, frontier-class model (codenamed Fable) changed his team's economics around AI-assisted coding. Previously, they saw little reason to invest heavily in coding harnesses or context strategies, because each new model release tended to deliver comparable quality at similar or lower prices, automatically solving many engineering inefficiencies. That free lunch ended with Fable: its performance was incredible but its cost was so high that it forced a deliberate reassessment of how to allocate tasks across available models.

Breunig notes that while Fable was exceptional, other models (Opus, 5.6, K3, and GLM) were 'good enough' for the majority of code they needed. This sparked a critical workflow shift: instead of using a single frontier model for everything, they began explicitly deciding which pieces of work should go to expensive high-end models and which could be safely handled by cheaper, adequate alternatives. The quote underscores a broader AI-workflow lesson: as model capabilities cluster and prices diverge, optimal engineering strategy becomes less about waiting for the next leap and more about routing work to the right model tier based on cost and required quality.

- Before expensive frontier models, improving harnesses or context strategies had low perceived ROI because new models would soon erase many inefficiencies.
- The arrival of Fable, though incredibly capable, was expensive enough to break the assumption of a free lunch.
- Cheaper models (Opus, 5.6, K3, GLM) proved 'good enough' for most coding tasks, enabling cost-aware task allocation.
- High model costs make deliberate workload routing across model tiers a necessary part of AI-assisted development.