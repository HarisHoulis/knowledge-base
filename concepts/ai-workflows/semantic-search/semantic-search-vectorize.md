---
domain: ai-workflows
subdomain: semantic-search
concept: semantic-search-vectorize
title: Building Semantic Search on my Content
sources:
  - title: "Building Semantic Search on my Content"
    url: "https://kentcdodds.com/blog/building-semantic-search-on-my-content"
    date: "2026-02-24"
---

# Building Semantic Search on my Content

Kent C. Dodds describes how he built semantic search for his website using Cloudflare's AI ecosystem (Workers AI, AI Gateway, and Vectorize). The project, which had been on his wish list since 2019, became trivial to implement with modern AI agents and Cloudflare's tools. He indexes his content (blog posts, YouTube videos, podcasts, etc.) by chunking text into overlapping pieces, generating stable chunk IDs, and hashing each chunk to enable incremental indexing. Only changed chunks are embedded and upserted into the vector database. For search, he embeds the query, fetches nearest chunk matches, and collapses them into document-level results by keeping the best-scoring chunk per document.

- Semantic search is implemented by indexing content into Cloudflare Vectorize, using Workers AI for embeddings, and querying with vector similarity.
- Incremental indexing is achieved by chunking source text, creating stable chunk IDs, and hashing chunk payloads to skip unchanged chunks in subsequent runs.
- The search pipeline overfetches chunk-level matches (topK * 5 capped at 20) to ensure good document coverage after collapsing duplicates.
- The entire implementation is simplified by AI agents that handle most of the coding, making what was once a large project essentially trivial.