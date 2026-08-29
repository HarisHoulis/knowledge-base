---
domain: ai-workflows
subdomain: semantic-search
concept: semantic-search-indexing-pipeline
title: Building Semantic Search on My Content
sources:
  - title: "Building Semantic Search on My Content"
    url: "https://kentcdodds.com/blog/building-semantic-search-on-my-content"
    date: "2026-02-24"
---

# Building Semantic Search on My Content

The article describes how the author implemented semantic search on his website using modern AI tools. The architecture uses Cloudflare Workers AI for embeddings and Vectorize as the vector database, with GitHub Actions for indexing. The indexing process chunks content into overlapping pieces, builds stable chunk IDs, hashes each chunk, and only re-embeds chunks whose content has changed, making incremental indexing efficient and cost-effective. Search works by embedding the query, retrieving top chunk matches with overfetching, then collapsing chunk results to document-level results by keeping the best-scoring chunk per document. This allows users to search across blog posts, videos, and other content using natural language queries.

- Chunking content with overlap preserves context and fits embedding model limits, improving retrieval precision.
- Stable chunk IDs (docId:chunk:i) and hashing enable incremental indexing by skipping unchanged chunks.
- Overfetching chunk-level matches (safeTopK * 5) and then collapsing to per-document best scores improves result diversity.
- Cloudflare Workers AI and Vectorize provide a simple, agent-friendly platform for building semantic search.
- The implementation is powered by GitHub Actions for automatic re-indexing and uses AI Gateway for embedding calls.