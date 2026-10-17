---
domain: ai-workflows
subdomain: rag-chunking
concept: chunking-strategies
title: 8 Chunking Strategies for RAG-Based Agents
sources:
  - title: "EP229: 8 Chunking strategies for RAG-based agents"
    url: "https://blog.bytebytego.com/p/ep229-8-chunking-strategies-for-rag"
    author: "ByteByteGo"
    date: "2026-10-17"
---

# 8 Chunking Strategies for RAG-Based Agents

This ByteByteGo refresher catalogs eight ways to split documents into chunks for retrieval-augmented generation. Fixed-size chunking cuts text every fixed number of tokens with a small overlap, while recursive chunking splits on paragraphs first and falls back to lines, words, and characters only when a piece is still too big. Document-based chunking respects existing structural breaks like headings, chapters, or HTML tags, so a markdown file becomes one chunk per section (ByteByteGo).

More sophisticated approaches target meaning rather than length. Semantic chunking embeds each sentence, compares similarity to the prior sentence, and starts a new chunk when similarity drops, catching real topic shifts. LLM-based chunking asks a model to rewrite text as standalone propositions, one idea per line, yielding high quality at high cost across a large corpus. Agentic chunking has an AI agent read each document, classify it (code, contract, table), and pick the chunking method per file instead of applying one rule everywhere (ByteByteGo).

Two strategies operate at the embedding level. Late chunking runs the full document through an embedding model, then applies normal split boundaries and mean-pools within each boundary to produce chunk embeddings. Hierarchical chunking breaks documents into layers: sections, paragraphs, then sentences. A reader comment notes a key constraint on late chunking: the whole document must fit the embedding model's context window (8K tokens for the jina-embeddings-v2 models used in the original paper), beyond which you must split into macro-chunks first. The payoff is that reference-heavy text retains meaning, e.g. a chunk like "its revenue grew 3%" keeps track of which company "its" refers to (reader comment).

The same issue also covers Google Translate's neural translation pipeline (language detection, BPE tokenization, target-language tokens, encoder/decoder, beam search), Agent Skills that load reusable playbooks on demand to keep context small, and a PostgreSQL (process-based) versus MySQL (thread-based, pluggable storage engines) comparison (ByteByteGo).

- Eight chunking strategies span simple token windows (fixed-size, recursive) to structure-aware (document-based, hierarchical) and meaning-aware (semantic, LLM-based, agentic) methods.
- Late chunking embeds the full document first, then mean-pools within split boundaries, preserving cross-references like pronoun antecedents that fixed-size splitting loses.
- Late chunking is bounded by the embedding model's context window (8K tokens for jina-embeddings-v2), requiring macro-chunking beyond that limit.
- Agentic chunking lets an agent classify each document and choose a per-file strategy rather than one rule for everything.
- A good reranker may recover much of the benefit of clever chunk boundaries, per a reader's open question.