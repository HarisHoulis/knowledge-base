---
domain: ai-workflows
subdomain: semantic-search
concept: hallucinate-tags
title: Don't classify. Hallucinate!
sources:
  - title: "Don't classify. Hallucinate!"
    url: "https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/"
    author: "Simon Willison"
    date: "2026-08-14"
---

# Don't classify. Hallucinate!

In this article, Simon Willison highlights a technique by Doug Turnbull for improving LLM-based tagging systems. Instead of forcing a model to choose from a fixed set of predefined tags, the approach lets the model freely hallucinate novel tag suggestions that fit the input, bypassing the limitations of closed-vocabulary classification. This allows the model to leverage its broad semantic knowledge without being constrained by an incomplete or rigid taxonomy (Simon Willison, 2026).

To reconcile these generated tags with an existing corpus, the method uses vector embeddings: the hallucinated tags are embedded, and then matched to the closest real tags in the embedding space. This creates a flexible bridge between free-form generation and structured classification. The article also suggests providing examples of the desired tag shape in the prompt, which helps the model produce more useful and format-consistent suggestions. Overall, this strategy decouples generation from classification, making the system more robust and adaptable to diverse queries (Willison, 2026).

- Let LLMs hallucinate candidate tags without restricting them to a predefined vocabulary.
- Use vector embeddings to map hallucinated tags to the nearest existing tags in the corpus.
- Including examples of tag structure in the prompt improves the quality of generated suggestions.
- This approach avoids the brittleness of closed-set classification and better handles novel or niche inputs.