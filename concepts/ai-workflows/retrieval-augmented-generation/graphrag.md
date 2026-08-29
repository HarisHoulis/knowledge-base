---
domain: ai-workflows
subdomain: retrieval-augmented-generation
concept: graphrag
title: GraphRAG: How AI Answers Questions Hidden Across Many Documents
sources:
  - title: "GraphRAG: How AI Answers Questions Hidden Across Many Documents"
    url: "https://blog.bytebytego.com/p/graphrag-how-ai-answers-questions"
    author: "ByteByteGo"
    date: "2026-08-19"
---

# GraphRAG: How AI Answers Questions Hidden Across Many Documents

GraphRAG shifts significant cost to indexing: graph extraction alone is about 75% of total indexing cost, and merging descriptions across thousands of mentions is expensive. It offers multiple query modes (local, global, DRIFT, and basic vector search) to balance thoroughness and latency. Standard RAG remains simpler and cheaper for local queries, and GraphRAG is best suited for questions that require understanding the corpus as a whole (ByteByteGo, 2026).

- Standard RAG fails on global queries because answers are spread across the corpus, not local to any similar chunk.
- GraphRAG builds a knowledge graph with entities and relationships, then creates hierarchical community summaries.
- Local search expands from entity matches; global search aggregates community reports to answer whole-corpus questions.
- GraphRAG's index-time cost is high, especially entity/relationship extraction and merging, but it improves answer quality for global questions.
- For local queries, standard RAG remains a simpler and more cost-effective option.