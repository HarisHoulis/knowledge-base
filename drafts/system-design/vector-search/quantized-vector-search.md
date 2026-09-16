---
domain: system-design
subdomain: vector-search
concept: quantized-vector-search
title: From Memory-Hungry HNSW to Quantized SPANN: The Technical Evolution of Pinterest's Manas Platform
sources:
  - title: "From Memory-Hungry HNSW to Quantized SPANN: The Technical Evolution of Pinterest's Manas Platform"
    url: "https://www.infoq.com/news/2026/09/pinterest-search/"
    author: "Olimpiu Pop"
    date: "2026-09-16"
---

# From Memory-Hungry HNSW to Quantized SPANN: The Technical Evolution of Pinterest's Manas Platform

Pinterest Engineering has enhanced its Manas search platform to handle vast data volumes, improving search and discovery efficiency. The platform's evolution involves moving from memory-intensive HNSW to quantized SPANN, applying Scalar and Product Quantization to significantly reduce memory usage while maintaining high recall rates (Pop, 2026).

To further optimize performance, the Manas platform utilizes SSDs, and Pinterest is transitioning to multi-vector models for more refined relevance matching. This technical evolution addresses the challenges of scaling vector search for large-scale applications (Pop, 2026).

- Pinterest's Manas platform applies Scalar and Product Quantization to cut memory usage while preserving high recall.
- The platform leverages SSDs for optimized performance.
- Pinterest is moving toward multi-vector models to improve relevance matching.
- The evolution from HNSW to quantized SPANN addresses memory constraints in large-scale vector search.