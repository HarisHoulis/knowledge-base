---
domain: ai-workflows
subdomain: search-embeddings
concept: hallucinate-then-embed
title: Don't classify. Hallucinate!
sources:
  - title: "Don't classify. Hallucinate!"
    url: "https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/"
    date: "2026-08-14T21:54:35+00:00"
---

# Don't classify. Hallucinate!

The article describes a technique by Doug Turnbull for improving search classification with LLMs. Instead of forcing a model to classify a query into a fixed set of predefined tags, you ask the model to generate novel, never-before-seen classifications that best fit the query. The prompt includes examples of the structural shape of valid tags, such as 'Furniture / Living Room Furniture / Coffee Tables & End Tables / Coffee Tables', to guide the model's output.

- Let the LLM propose new tag paths rather than constraining it to an existing vocabulary.
- Providing examples of tag format helps the model generate plausible and structured candidates.
- Use vector embeddings to match the hallucinated tags to the closest real tags in the existing corpus.
- This approach can better handle diverse search queries and uncover relevant classifications that a fixed taxonomy might miss.