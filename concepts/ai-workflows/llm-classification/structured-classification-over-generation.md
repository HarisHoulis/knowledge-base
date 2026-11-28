---
domain: ai-workflows
subdomain: llm-classification
concept: structured-classification-over-generation
title: Beyond Generation: Fast, Structured Classification with Jev at Glean
sources:
  - title: "Stop Paying LLM Prices for Yes-or-No Answers — Chinmay Goyal, Glean"
    url: "https://www.youtube.com/watch?v=K5_ST-kMrvY"
    author: "AI Engineer"
    date: "2026-11-27"
---

# Beyond Generation: Fast, Structured Classification with Jev at Glean

Chinmay Goyal of Glean argues that most AI tasks in production are constrained problems—intent classification, ranking among N options, quote validation, routing to models or experts—rather than open-ended generation. Historically these were solved with general-purpose LLMs, paying full token prices and latency for what is essentially a yes-or-no or pick-one answer. Glean adopted Jev, a classification approach that sits between general LLMs and pre-trained classifiers, to avoid generating unnecessary output text.

Glean evaluated general-purpose LLMs, open models like LLaMA, fine-tuning LLaMA on their own compute, and Jev. For query classification, Jev nearly doubled output quality over the base LLaMA model and delivered about 90% of the quality of the fine-tuned LLaMA—without the data collection, cleaning, training compute, or repeated retraining when the taxonomy changes. Changing the solution space only requires a small prompt change, and there is no model placement or inference cost to manage.

For routing requests to the best expert, a Jev test environment with N experts showed significantly higher accuracy and roughly an 8x latency reduction versus a general-purpose LLM. Goyal notes this required significant infrastructure changes, but the latency win justified the added complexity—rare for a team that otherwise favors the simplest possible system. A third use case, internally called Q, generates follow-up suggestions and next-query predictions from 10–15 independent sources before a ranking stage.

Because Glean serves millions of users, every change goes through a multi-phased evaluation: gold-standard test suites for nearly every scenario, weeks of testing on Glean's own ~1,500-person internal instance with active feedback, and then A/B testing with clients.

- Most production AI tasks are constrained classification/ranking problems, not generation—so paying full LLM price and latency is wasteful.
- Jev nearly doubled quality over base LLaMA and reached ~90% of a fine-tuned LLaMA's quality without training data or compute.
- Taxonomy changes need only a prompt tweak, avoiding retraining and model placement/inference cost management.
- Expert routing with Jev showed significantly higher accuracy and ~8x latency reduction, justifying added infrastructure complexity.
- Changes are validated via gold-standard suites, internal dogfooding across ~1,500 employees, then client A/B tests.