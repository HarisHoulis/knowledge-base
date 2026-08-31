---
domain: ai-workflows
subdomain: retrieval-augmented-generation
concept: graphrag
title: GraphRAG: How AI Answers Questions Hidden Across Many Documents
sources:
  - title: "GraphRAG: How AI Answers Questions Hidden Across Many Documents"
    url: "https://blog.bytebytego.com/p/graphrag-how-ai-answers-questions"
    author: "ByteByteGo"
    date: "Wed, 19 Aug 2026 15:31:18 GMT"
---

# GraphRAG: How AI Answers Questions Hidden Across Many Documents

GraphRAG addresses the limitations of standard RAG on global, corpus-wide questions by building a knowledge graph from source documents. The indexing pipeline extracts entities, relationships, and claims using language models, merges duplicate entities, and constructs a hierarchical community structure via Leiden clustering. Each community gets a summarized report, which captures collective information before query time. This enables two query modes: local search, which expands from matched entities to nearby text units, reports, and relationships; and global search, which maps and reduces over community reports to produce an answer. The approach is expensive at index time—graph extraction alone accounts for roughly 75% of indexing cost—but it makes whole-collection reasoning tractable (ByteByteGo, 2026).

- Standard RAG fails on global queries because vector similarity only surfaces chunks that resemble the question, not answers distributed across many documents.
- GraphRAG constructs a knowledge graph of entities and relationships, enabling connection-based retrieval and community-level summarization.
- Hierarchical Leiden clustering and community reports provide a precomputed corpus overview, which makes global queries answerable.
- Local search expands from entities to gather context; global search aggregates community reports via map-reduce.
- GraphRAG has high indexing costs (LLM-based extraction is dominant) but can deliver better answer quality for cross-document analytical questions, as seen in LinkedIn's support ticket retrieval improvements.