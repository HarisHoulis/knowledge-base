---
domain: ai-workflows
subdomain: llm-model-selection
concept: model-naming-conventions
title: LLM Performance Dimensions and Model Naming Conventions
sources:
  - title: "Quoting Ted Sanders"
    url: "https://simonwillison.net/2026/Oct/28/ted-sanders/"
    author: "Ted Sanders"
    date: "2026-10-28"
---

# LLM Performance Dimensions and Model Naming Conventions

Ted Sanders explains that LLM performance is multidimensional, with no fixed ordering across tasks like math and humor, yet much of the variation is captured by a single variable: model size. Bigger models tend to be more performant and reliable, cost more per token, and better recall esoteric facts. OpenAI's models are ordered Luna < Terra < Sol < Astra.

Version numbers encode multiple signals at once: release order, relationship to other releases, and magnitude of improvement. A version like 6.1 signals it launched after 5.6, may share training data or personality traits with other 6.1 models (hence not 5.7), and is not a large enough leap to warrant the expectations of a 7.

- LLM performance is multidimensional, but model size explains much of the variation
- Larger models are more reliable, cost more per token, and recall esoteric facts better
- OpenAI model ordering: Luna < Terra < Sol < Astra
- Version numbers encode release order, model family similarity, and magnitude of improvement