---
domain: ai-workflows
subdomain: semantic-tagging
concept: hallucinate-then-map
title: Don't classify. Hallucinate!
sources:
  - title: "Don't classify. Hallucinate!"
    url: "https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/"
    date: "2026-08-14"
---

# Don't classify. Hallucinate!

This article highlights Doug Turnbull's technique for using LLMs to generate novel tags rather than classifying into a fixed vocabulary. The model is instructed to imagine new, never-before-seen classifications that fit a query, guided by examples of the existing tag shape. This approach avoids the limitations of rigid classification and leverages the model's broad semantic knowledge.

The generated tag (e.g., 'brown coffee table') is then embedded as a vector, and compared against embeddings of the existing tag corpus to find the concrete tags that are closest in meaning. This bridges the gap between the model's creative output and the actual taxonomy, enabling more flexible and accurate tagging for search. The article includes an example prompt with product classification hierarchies to illustrate how to frame the task for the model.

- Instead of forcing LLMs to output from a fixed set of classes, let them hallucinate novel tags that fit the query.
- Use vector embeddings to map the hallucinated tag to the nearest existing tags in the corpus.
- Providing examples of the desired tag format helps the model generate more useful suggestions.
- This technique leverages semantic similarity to bridge creative model output and structured taxonomies.