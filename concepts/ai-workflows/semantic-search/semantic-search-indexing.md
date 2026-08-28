---
domain: ai-workflows
subdomain: semantic-search
concept: semantic-search-indexing
title: Building Semantic Search on my Content
sources:
  - title: "Building Semantic Search on my Content"
    url: "https://kentcdodds.com/blog/building-semantic-search-on-my-content"
    author: "Kent C. Dodds"
    date: "2026-02-24"
---

# Building Semantic Search on my Content

Kent C. Dodds describes how he built semantic search for his site, a feature on his wish list since 2019. He decided to implement it after being impressed by modern AI agents and Cloudflare's AI platform. The architecture uses Cloudflare Workers AI for embeddings and Vectorize as the vector database, making the implementation relatively simple (source: https://kentcdodds.com/blog/building-semantic-search-on-my-content).

The indexing process starts by chunking the full text content into overlapping chunks (target 2500 chars, max 3500, overlap 250) to stay within embedding model limits and preserve context across boundaries. Each chunk gets a stable ID (`docId:chunk:i`) and is hashed; the hash is stored in a manifest. During incremental indexing, unchanged chunks are skipped, and only changed chunks are embedded and upserted into Vectorize, saving money and time (source: https://kentcdodds.com/blog/building-semantic-search-on-my-content).

Search involves embedding the query, overfetching chunk-level matches (`safeTopK * 5`, capped at 20), then collapsing the results to document-level by keeping only the best-scoring chunk per document and sorting by score. This avoids the same document appearing multiple times and provides a clean set of results (source: https://kentcdodds.com/blog/building-semantic-search-on-my-content).

- Semantic search is built by chunking content, embedding chunks, and storing vectors in a vector database.
- Overlapping chunks with stable IDs and hashing enable efficient incremental indexing and reduce embedding costs.
- The search query is embedded and vector similarity search returns chunk matches, which are then collapsed to document-level results.
- Cloudflare Workers AI (with AI Gateway) and Vectorize provide a simple, powerful platform for building AI apps.