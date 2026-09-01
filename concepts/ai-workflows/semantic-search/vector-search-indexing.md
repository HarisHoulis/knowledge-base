---
domain: ai-workflows
subdomain: semantic-search
concept: vector-search-indexing
title: Building Semantic Search on my Content
sources:
  - title: "Building Semantic Search on my Content"
    url: "https://kentcdodds.com/blog/building-semantic-search-on-my-content"
    author: "Kent C. Dodds"
    date: "2026-02-24"
---

# Building Semantic Search on my Content

Kent C. Dodds describes how he implemented semantic search on his website using Cloudflare Workers AI and Vectorize. He explains the indexing pipeline, which chunks source content, builds stable chunk IDs, hashes each chunk, and uses a manifest to skip unchanged chunks during incremental indexing. Only changed chunks are embedded and upserted to the vector database. For search, the query is embedded, a vector search returns top chunk matches, then results are collapsed into document-level matches by keeping the best-scoring chunk per document. He notes that modern AI agents made the implementation fast, and the feature is live on his site with a `/` shortcut to search.

- Chunking with overlap preserves context across boundaries and enables precise retrieval.
- Stable chunk IDs and hash-based manifests allow skipping unchanged embeddings, saving time and cost.
- Search overfetches chunk-level matches (topK * 5, capped at 15) then collapses to document-level results for better diversity.
- Cloudflare Workers AI (via AI Gateway) and Vectorize provide a simple platform for building AI-powered semantic search.