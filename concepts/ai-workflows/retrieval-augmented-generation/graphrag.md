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

Standard RAG slices documents into chunks, embeds them, and retrieves by vector similarity. This works for local queries where the answer text resembles the question, but fails on global queries where the answer emerges only after surveying the whole corpus (ByteByteGo, 2026). Microsoft's GraphRAG documentation distinguishes local from global queries; a global query like 'which failure causes recur most often' cannot be answered by nearest-neighbor search because the answer is a distribution across documents, not a single text region.

GraphRAG constructs a knowledge graph by extracting entities and relationships with an LLM, merging duplicate entities, and optionally extracting claims. It then runs hierarchical Leiden clustering to partition the graph into communities at multiple levels, and generates a community report for each community. These reports summarize clusters and enable whole-collection reasoning during retrieval. The merge step and two LLM passes make indexing expensive; extraction is about 75% of indexing cost.

Query modes are local and global. Local search starts from entities matching the query and expands to neighbor entities, relationships, text units, community reports, and claims. Global search maps over community reports, generates rated intermediate answers, then reduces them into a final answer. DRIFT search blends both. GraphRAG also includes basic vector search for simple lookups.

- Standard RAG relies on similarity between query and answer text, which fails on global queries where answers are distributed across many documents.
- GraphRAG builds a knowledge graph with entities and relationships extracted by an LLM, merged into a coherent structure.
- Hierarchical Leiden clustering partitions the graph into communities, each with an LLM-generated report that acts as a pre-computed summary for global reasoning.
- Local search expands from query-matched entities; global search aggregates community reports via map-reduce; DRIFT search combines both.
- GraphRAG's indexing cost is significantly higher than standard RAG, with extraction consuming roughly 75% of the budget.