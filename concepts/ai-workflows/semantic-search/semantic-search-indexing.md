---
domain: ai-workflows
subdomain: semantic-search
concept: semantic-search-indexing
title: Building Semantic Search on my Content
sources:
  - title: "Building Semantic Search on my Content"
    url: "https://kentcdodds.com/blog/building-semantic-search-on-my-content"
    date: "2026-02-24"
---

# Building Semantic Search on my Content

The article describes how Kent C. Dodds implemented semantic search on his website using Cloudflare's AI platform, specifically Workers AI and Vectorize. The motivation came from a long-standing wishlist item and the ease of using AI agents to build features. The architecture involves two core paths: indexing content (blog posts, YouTube videos, podcasts, pages) and searching the vector database. Indexing is done via GitHub Actions, chunking source text into overlapping segments, creating stable chunk IDs, and hashing chunk payloads to enable incremental updates that skip unchanged content, thereby saving cost and time. Searching embeds the user's query, queries Vectorize for nearest neighbors, and then collapses chunk-level matches into document-level results, keeping the best-scoring chunk per document to present a clean list of search results. The author highlights how trivial it is to build with Cloudflare's premade components, especially with AI agents doing most of the work.

- Semantic search is implemented by chunking content into overlapping segments, embedding them, and storing in a vector database (Vectorize).
- Stable chunk IDs and SHA-256 hashing enable incremental indexing, skipping unchanged chunks to save money and speed up the process.
- Search queries are embedded and matched against the vector index, then chunk matches are collapsed into document-level results by taking the best-scoring chunk per document.
- Cloudflare Workers AI (with AI Gateway) and Vectorize make the AI-powered app development process 'phenomenally easy'.