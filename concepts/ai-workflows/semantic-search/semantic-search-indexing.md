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

Kent C. Dodds describes how he implemented semantic search on his website using modern AI tools, specifically Cloudflare Workers AI and Vectorize. The core architecture involves two main code paths: indexing and searching. Indexing starts by chunking source content (e.g., MDX files, transcripts) into overlapping pieces, then building stable chunk IDs and hashing each chunk payload. A manifest stores these hashes so unchanged chunks are skipped during re-embedding, saving cost and time. Only changed chunks are embedded into vectors and upserted to the vector database. For searching, the query is embedded, and the vector database returns nearest neighbors with metadata. Since the same document can appear multiple times, the code collapses chunk-level matches into document-level results by keeping the best-scoring chunk per document.

- Chunking with overlap (targetChars 2500, overlap 250, max 3500) preserves context and fits embedding model limits.
- Stable chunk IDs and content hashing enable incremental indexing by skipping unchanged chunks.
- Search overfetches chunk matches (safeTopK * 5, capped at 20) then collapses them to document-level results using canonical doc IDs.
- Cloudflare Workers AI (via AI Gateway) and Vectorize make building semantic search 'phenomenally easy'.
- The implementation is practical and cost-effective, reusing existing content and automation via GitHub Actions.