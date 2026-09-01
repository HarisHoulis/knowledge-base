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

Standard RAG retrieval assumes that text answering a question resembles the question itself, which works for local queries like "Which service owns the payments retry logic?" but fails for global queries like "Which failure causes recur most often across all postmortems?" where the answer is distributed across many documents. GraphRAG addresses this by building a knowledge graph from documents, extracting entities and relationships via LLM passes, then clustering the graph into a community hierarchy with generated reports. This allows global questions to be answered by aggregating pre-written community summaries rather than relying on vector similarity alone (ByteByteGo, 2026).

GraphRAG indexing is expensive: LLM-based extraction accounts for roughly 75% of total indexing cost, and the merge step reconciles multiple descriptions for the same entity. However, query-time costs vary by mode. Local search expands from matched entities along five directions (text units, community reports, neighboring entities, relationships, and covariates), while global search maps over shuffled community report batches and reduces them into a final answer. The choice of community hierarchy level significantly affects answer quality and cost (ByteByteGo, 2026).

GraphRAG is not always the better option; standard RAG remains cheaper and appropriate for local queries. Alternative approaches like FastGraphRAG replace LLM extraction with traditional NLP to reduce indexing cost at the expense of noisier graphs. Agentic RAG is mentioned as a related direction, and DRIFT search blends local and global modes by using community reports to generate follow-up queries for local search (ByteByteGo, 2026).

- Standard RAG handles local queries well but struggles with global queries whose answers span many documents.
- GraphRAG builds a knowledge graph with entities and relationships, then uses hierarchical Leiden clustering to create community reports.
- Local search expands from matched entities; global search aggregates across community reports via map-reduce.
- Graph extraction is LLM-heavy, about 75% of indexing cost, making indexing significantly more expensive than standard RAG.
- The choice of community hierarchy level heavily influences answer quality, latency, and token usage.