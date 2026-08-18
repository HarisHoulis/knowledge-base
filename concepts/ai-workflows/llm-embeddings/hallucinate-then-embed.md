---
domain: ai-workflows
subdomain: llm-embeddings
concept: hallucinate-then-embed
title: Don't classify. Hallucinate!
sources:
  - title: "Don't classify. Hallucinate!"
    url: "https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/"
    author: "Simon Willison"
    date: "2026-08-14"
---

# Don't classify. Hallucinate!

This article describes a technique by Doug Turnbull for improving classification tasks with LLMs. Instead of forcing the model to choose from a fixed set of predefined tags or categories, the approach asks the model to generate novel, hallucinated classifications that fit the query. These free-form outputs are then mapped to the existing vocabulary using vector embeddings, finding the concrete tags that are closest to the imagined ones in semantic space.

The prompt examples illustrate the desired shape of tags, such as hierarchical paths like 'Furniture / Living Room Furniture / Coffee Tables & End Tables / Coffee Tables.' This helps the model produce outputs that are structurally similar to the existing taxonomy. The method leverages the LLM's semantic understanding to bridge novel and existing labels, offering a flexible alternative to rigid classification.

- Let the LLM hallucinate potential tags without being constrained by the existing vocabulary.
- Use vector embeddings to compare hallucinated tags against the actual tag corpus to find the closest matches.
- Provide examples of the tag structure in the prompt to guide the model's output format.
- This approach combines generative AI and embeddings to improve search and classification tasks.