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

GraphRAG supports two retrieval modes: local search and global search. Local search first matches entities in the query, then expands along text units, community reports, neighboring entities, relationships, and claims. Global search instead uses community reports from a chosen hierarchy level, maps batches of reports to intermediate answers, and reduces them to a final answer. While GraphRAG improves global question answering, it is expensive—graph extraction alone is about 75 percent of indexing cost—and standard RAG remains the better option for local queries and simpler workflows (ByteByteGo, 2026).

- Standard RAG is limited to local queries where the answer text resembles the question; it fails on global queries that require reasoning across a large corpus.
- GraphRAG builds a knowledge graph by extracting entities and relationships from documents, then merges duplicates and generates hierarchical community summaries.
- GraphRAG provides local search (entity-anchored expansion) and global search (community report aggregation) to handle both query types.
- GraphRAG indexing is expensive: LLM-based graph extraction accounts for roughly 75% of total indexing cost, and response quality depends heavily on the chosen community hierarchy level.
- Standard RAG remains the better option for queries answerable from a small number of documents.