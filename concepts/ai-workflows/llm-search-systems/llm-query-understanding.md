---
domain: ai-workflows
subdomain: llm-search-systems
concept: llm-query-understanding
title: How Instacart Uses LLMs to Make People Buy More
sources:
  - title: "How Instacart Uses LLMs to Make People Buy More"
    url: "https://blog.bytebytego.com/p/how-instacart-uses-llms-to-make-people"
    author: "ByteByteGo"
    date: "2026-11-16"
---

# How Instacart Uses LLMs to Make People Buy More

Instacart rebuilt its product search query understanding (QU) using LLMs to handle the gap between how shoppers phrase searches (e.g. "bread no gluten") and how the catalog is structured. The QU phase produces three outputs—product categories, alternative queries, and structured tags—that guide both retrieval and ranking. The prior approach relied on noisy behavioral data and separate models (a FastText category classifier, pattern-mined query rewrites), which required heavy maintenance, produced inconsistent interpretations, and struggled with long-tail and ambiguous queries.

To make a general LLM useful, Instacart combined context engineering (RAG-style injection of catalog records and historical patterns), post-processing guardrails that validate outputs against the catalog, and fine-tuning of smaller models on their own examples. For category prediction, the system uses a three-stage pipeline: historical purchase data proposes candidate categories, the LLM re-ranks them using world knowledge (e.g. mapping "vegan roast" to Meat → Meat Alternatives), and an embedding-based guardrail discards pairings whose similarity to the query falls below a threshold.

Query rewriting was split into three distinct tasks—synonym, broader, and substitute rewrites—each with dedicated prompts, reasoning guidance, and semantic filters, since a generic rewrite prompt produced useless variants like "one percent milk." This raised rewrite coverage from ~50% to over 95% with more than 90% precision. For semantic role labeling (extracting product, brand, and attributes), Instacart precomputes tags for head queries into a cache, while an offline "teacher" pipeline with a powerful model and rich context generates validated tags that train a smaller real-time "student" model (fine-tuned Llama-3 8B) to handle unseen queries.

- LLM query understanding produces categories, alternative queries, and structured tags that drive retrieval and ranking
- Category prediction combines historical candidates, LLM re-ranking, and embedding-based guardrails to filter irrelevant matches
- Splitting query rewriting into synonym, broader, and substitute types lifted coverage from ~50% to 95%+ with 90%+ precision
- A teacher-student setup precomputes tags for head queries and fine-tunes a smaller model (Llama-3 8B) for real-time long-tail queries
- Behavioral data alone is noisy training signal; LLM world knowledge plus catalog validation fills the gap