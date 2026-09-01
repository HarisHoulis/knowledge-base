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

Standard RAG retrieval embeds document chunks and questions into vectors, then retrieves chunks whose text is semantically closest to the query. This works well for local queries where the answer lives in a small number of text regions and resembles the question. However, for global queries that require synthesizing information across an entire corpus, simple similarity search fails because the answer is not concentrated in any single chunk—it is distributed across many documents, making vocabulary-based retrieval coincidental rather than substantive (ByteByteGo, 2026).

GraphRAG addresses this by constructing a knowledge graph from the corpus. An LLM extracts entities and typed relationships from each text unit, merges duplicate entities across documents, and optionally extracts time-bound claims. The graph is then clustered into a hierarchy using Leiden community detection, and LLM-generated community reports summarize what each cluster collectively says. These pre-written reports provide the material needed to answer corpus-wide questions (ByteByteGo, 2026).

GraphRAG supports multiple query modes. Local search finds entry-point entities from the query and expands to neighboring entities, text units, community reports, relationships, and claims, then ranks and packs them into a fixed context window. Global search ignores the entity graph and instead runs a map-reduce over community reports, where batched reports are summarized with importance ratings and then merged into a final answer. A third DRIFT search blends both approaches, and basic vector search remains available for simple queries (ByteByteGo, 2026).

The cost is substantial: graph extraction alone accounts for roughly 75% of indexing cost due to two LLM passes over the corpus. While standard RAG has simple indexing and lookup, GraphRAG's higher index-time cost buys the ability to answer global questions with comprehensive, diverse, and well-sourced answers. Standard RAG remains the better option for local, fact-based queries (ByteByteGo, 2026).

- Standard RAG fails on global questions because vector similarity cannot capture patterns distributed across many documents.
- GraphRAG builds a knowledge graph of entities, relationships, and claims, then applies hierarchical Leiden clustering and generates community summaries.
- Local search expands from matched entities; global search uses a map-reduce over community reports to answer corpus-wide questions.
- Graph extraction is the dominant cost of GraphRAG indexing, estimated at 75% of total indexing expense.
- Standard RAG is still preferable for local, fact-based queries; GraphRAG is needed for global, whole-collection questions.