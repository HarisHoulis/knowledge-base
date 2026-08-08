---
domain: ai-workflows
subdomain: llm-memory-optimization
concept: kv-cache-optimization
title: Why An LLM's Memory Gets Expensive and How to Fix It
sources:
  - title: "Why An LLM's Memory Gets Expensive and How to Fix It"
    url: "https://blog.bytebytego.com/p/why-an-llms-memory-gets-expensive"
    author: "ByteByteGo"
    date: "2026-08-04"
---

# Why An LLM's Memory Gets Expensive and How to Fix It

The article explains that the rising cost of long-context LLM inference stems from the KV cache, a block of working memory that stores key and value vectors for every token in the input. While this cache avoids recomputing vectors on each step, it grows linearly with context length and batch size—for a 70B model at 128K tokens, it can consume roughly 40GB of GPU memory. The real bottleneck appears during decoding, where every generated token requires reading the entire cache from memory, making the process memory-bound rather than compute-bound. Thus, long-context generation is expensive not just because the cache is large, but because it must be swept through on every token (ByteByteGo).

- The KV cache is a separate memory block that grows linearly with context length and batch size, reaching ~40GB for a 70B model at 128K tokens.
- Decoding reads the entire cache for every generated token, making long-context inference memory-bound and bandwidth-limited.
- Architectural changes like grouped-query attention and latent attention reduce per-token cache footprint, but require training-time commitment.
- Quantization and eviction apply to existing models: 8-bit quantization is nearly lossless, while 4-bit and aggressive eviction risk accuracy and retrieval quality.
- Paged attention and prefix caching improve serving efficiency by reducing fragmentation and sharing cached prefixes, with up to 90% cost and latency savings.