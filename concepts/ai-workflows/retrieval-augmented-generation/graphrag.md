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

Standard RAG retrieves relevant text chunks via embedding similarity, which works well for local queries where the answer text resembles the question. However, it fails on global queries that require synthesizing information across many documents, because the answer exists as a distribution across the corpus rather than in a single retrievable location. Microsoft's GraphRAG documentation distinguishes local queries (answer in a small number of text regions) from global queries (require reasoning across large portions or all of a dataset), and tests show larger context windows in standard RAG still leave gaps in comprehensiveness and source quality for global questions (ByteByteGo, 2026).

GraphRAG addresses this by building a knowledge graph from documents. The indexing pipeline extracts entities, relationships, and optional claims from text units using LLMs, merges duplicate entities across the corpus, and runs hierarchical Leiden clustering to detect communities. For each community, an LLM generates a community report containing an overview, key entities, relationships, and claims. These reports are summarized and stored, effectively pre-writing the material needed to answer global questions. The merge step and multiple LLM passes make extraction roughly 75% of total indexing cost (ByteByteGo, 2026).

At query time, GraphRAG supports two main modes. Local search finds entry-point entities by matching the query to entity descriptions, then expands along text units, community reports, neighboring entities, relationships, and covariates, ranking and filtering them into a context window. Global search leaves the entity graph untouched and instead performs map-reduce over shuffled community reports from a chosen hierarchy level, producing rated intermediate answers and then a final answer. The choice of hierarchy level impacts quality and cost: lower levels have more detailed reports but are more expensive. GraphRAG also includes DRIFT search (a hybrid) and a basic vector search mode for simple lookups (ByteByteGo, 2026).

- Standard RAG's similarity-based retrieval fails on global questions that require cross-document synthesis, even with large context windows.
- GraphRAG builds a knowledge graph of entities, relationships, and claims, with pointers back to source text for citation.
- Hierarchical community detection generates pre-written community reports, making whole-collection questions answerable.
- Local search expands from matched entities; global search aggregates community reports via map-reduce.
- GraphRAG has significantly higher indexing cost (~75% for extraction) and is best suited for global Q&A; standard RAG remains simpler and cheaper for local queries.