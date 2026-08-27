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

Standard RAG relies on vector similarity: documents are chunked, embedded, and retrieved by nearest neighbors to the query. This works well for local queries, where the answer resides in a small number of text regions and resembles the query. However, for global queries that require reasoning across an entire corpus, such as identifying recurring failure causes across all postmortems, similarity retrieval returns chunks that merely share vocabulary with the query, missing the underlying pattern. Microsoft's GraphRAG documentation distinguishes these two query types and notes that even expanding context to 64,000 tokens does not close the gap on comprehensiveness, diversity, and source quality for global questions (ByteByteGo, 2026).

GraphRAG addresses this by building a knowledge graph from the corpus. An LLM extracts entities and relationships from text units, merges duplicates across documents, and optionally extracts time-bound claims. The graph is then clustered into a hierarchy using Leiden community detection, and for each community an LLM generates a community report summarizing its key entities, relationships, and claims. These reports are written during indexing, so when a global query arrives, the material needed to answer it already exists as pre-summarized text. This hierarchical structure enables two query modes: local search expands from matched entities along five parallel directions, while global search aggregates over community reports via a map-reduce stage. DRIFT search blends both approaches (ByteByteGo, 2026).

GraphRAG comes with significant tradeoffs. Indexing is expensive, with graph extraction estimated at roughly 75% of total indexing cost due to two LLM passes over the entire corpus. The choice of hierarchy level for global search heavily influences response quality and cost: lower levels provide more detail but require processing many more reports. Standard RAG remains the better option for local queries and when cost and latency are primary concerns (ByteByteGo, 2026).

- Standard RAG fails on global queries because vector similarity retrieves chunks that resemble the query's vocabulary rather than answers distributed across many documents.
- GraphRAG constructs a knowledge graph of entities and relationships, then uses hierarchical Leiden clustering to generate community reports that summarize document clusters.
- Local search expands from entity matches through text units, community reports, neighbors, relationships, and claims; global search aggregates community reports via map-reduce.
- Graph extraction consumes about 75% of indexing cost, making GraphRAG significantly more expensive than standard RAG; standard RAG remains preferable for local queries and cost-sensitive deployments.