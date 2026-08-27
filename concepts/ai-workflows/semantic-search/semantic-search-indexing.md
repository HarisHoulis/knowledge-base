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

Kent C. Dodds describes implementing semantic search on his website using modern AI tools and Cloudflare's AI platform. He had wanted this feature since 2019, but recent advances in AI agents (like Cursor) made it trivial to build. The system indexes content (blog posts, videos, podcasts) into a vector database by chunking text into overlapping segments, generating embeddings via Cloudflare Workers AI, and storing them in Cloudflare Vectorize. To support incremental indexing, each chunk is hashed and only changed chunks are re-embedded and upserted, saving time and money. For search, the query is embedded, a vector search fetches nearest neighbor chunks, and results are collapsed per document by keeping the best-scoring chunk. The article highlights how Cloudflare's integrated AI stack simplifies building AI-powered applications and how AI agents accelerated the development process.

- Semantic search was implemented using Cloudflare Vectorize as the vector database and Workers AI for generating embeddings.
- Content is chunked into overlapping segments with stable IDs, and each chunk is hashed to skip unchanged chunks during re-indexing.
- Search overfetches chunk-level matches (up to 15) and then collapses them into per-document results by keeping the highest-scoring chunk per document.
- AI coding agents (e.g., Cursor) made it feasible to quickly implement this long-requested feature and close all open issues.