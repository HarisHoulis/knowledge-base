---
domain: ai-workflows
subdomain: knowledge-graph-rag
concept: graphrag
title: GraphRAG: How AI Answers Questions Hidden Across Many Documents
sources:
  - title: "GraphRAG: How AI Answers Questions Hidden Across Many Documents"
    url: "https://blog.bytebytego.com/p/graphrag-how-ai-answers-questions"
    author: "ByteByteGo"
    date: "2026-08-19"
---

# GraphRAG: How AI Answers Questions Hidden Across Many Documents

Standard RAG retrieves answers by embedding text chunks and finding vectors similar to the query. This works for local queries, where the answer resembles the question and lives in a few documents, but fails for global queries that require synthesizing patterns across an entire corpus. Microsoft's GraphRAG documentation distinguishes these two types, and tests show that simply enlarging context windows to 64,000 tokens still leaves global questions poorly answered (ByteByteGo, 2026).

- Standard RAG assumes text answering a question resembles the question, limiting it to local queries; global queries need a different mechanism.
- GraphRAG constructs a knowledge graph by extracting entities and relationships from documents, merging duplicates, and preserving citations to source text.
- Hierarchical Leiden clustering partitions the entity graph into communities, and language models generate summary reports for each community, enabling whole-collection understanding.
- Local search expands from matched entities across five parallel directions, while global search aggregates pre-written community reports through map-reduce.
- GraphRAG shifts cost to indexing (about 75% for graph extraction), making it expensive for large corpora; FastGraphRAG reduces cost using traditional NLP but adds noise.