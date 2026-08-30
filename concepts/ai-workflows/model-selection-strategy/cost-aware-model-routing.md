---
domain: ai-workflows
subdomain: model-selection-strategy
concept: cost-aware-model-routing
title: Fable & The End of the Free Lunch
sources:
  - title: "Quoting Drew Breunig"
    url: "https://simonwillison.net/2026/Aug/23/drew-breunig/"
    author: "Drew Breunig"
    date: "2026-08-23"
---

# Fable & The End of the Free Lunch

Drew Breunig observes that before Anthropic's Fable model, improving your coding harness or context strategies felt low-value because new, cheaper models would quickly arrive and eclipse those custom tweaks. The rapid pace of model improvement made detailed optimization seem wasteful.

With Fable, however, capability jumped dramatically but so did cost. Meanwhile, existing models like Opus, 5.6, K3, and even GLM remained "good enough" for most coding tasks. This created a cost-performance tension, forcing Breunig's team to deliberately think about which tasks should be routed to which model, rather than defaulting to the newest or most powerful option.

The quote signals a shift from a 'wait for the next model' mindset to proactive, cost-aware workflow design: choose the right tool per task based on required capability and price. (Source: Drew Breunig via Simon Willison, https://simonwillison.net/2026/Aug/23/drew-breunig/)

- Before premium models like Fable, investing in custom harness improvements was often wasted effort because newer, cheaper models would soon make those refinements obsolete.
- Fable is a step-change in capability but comes with high costs, making it impractical for routine coding tasks.
- Several existing models (Opus, 5.6, K3, GLM) are 'good enough' for most coding needs, offering a cost-effective alternative.
- The optimal approach is now to deliberately route work to the most cost-appropriate model, moving beyond a one-size-fits-all strategy.