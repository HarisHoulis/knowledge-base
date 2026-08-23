---
domain: system-design
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

Standard RAG retrieval assumes that text answering a question resembles the question. This works for local queries where the answer exists in a specific document, but fails for global queries that require reasoning across many documents. For example, a question like 'Which service owns the payments retry logic' is local, while 'Which failure causes recur most often across all postmortems' is global and cannot be answered by similarity search alone (ByteByteGo).

GraphRAG addresses this by building a knowledge graph from documents. The indexing pipeline extracts entities and relationships using a language model, merges duplicates, optionally extracts claims, and then runs hierarchical Leiden clustering to create communities. For each community, the system generates a community report summarizing the cluster of documents. This report generation happens at index time, so global queries can be answered by summarizing these pre-built reports instead of searching raw text (ByteByteGo).

At query time, GraphRAG offers local search and global search. Local search expands from matched entities through text units, community reports, neighboring entities, relationships, and covariates. Global search maps over shuffled community report batches, produces intermediate rated answers, then reduces them into a final answer. A third mode, DRIFT search, blends both approaches. GraphRAG also includes a basic top-k vector retrieval mode for simple queries (ByteByteGo).

GraphRAG has significant tradeoffs. The extraction and merging stages require multiple LLM passes over the entire corpus, with graph extraction estimated at about 75% of total indexing cost. Standard RAG remains more efficient for local queries and simpler use cases. However, for global questions that require understanding patterns across a corpus, GraphRAG provides a way to make the answer material exist as text ahead of time, supporting comprehensive and well-cited answers (ByteByteGo).

- Standard RAG uses similarity search, which fails for global queries where the answer spans many documents rather than residing in a similar text chunk.
- GraphRAG constructs a knowledge graph with entities, relationships, and claims, then runs hierarchical Leiden clustering to create community reports that summarize the entire corpus.
- Local search expands from matched entities through related graph elements, while global search aggregates across pre-generated community reports to answer whole-collection questions.
- GraphRAG indexing is expensive: graph extraction accounts for about 75% of total indexing cost due to multiple LLM passes, making standard RAG more suitable for local queries and simpler use cases.