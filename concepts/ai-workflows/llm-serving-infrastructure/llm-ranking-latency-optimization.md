---
domain: ai-workflows
subdomain: llm-serving-infrastructure
concept: llm-ranking-latency-optimization
title: Scaling LLM-Based Ranking Systems for Latency-Critical Search & Recommendation Workloads
sources:
  - title: "Presentation: Scaling LLM-Based Ranking Systems for Latency-Critical Search & Recommendation Workloads"
    url: "https://www.infoq.com/presentations/scale-llm-ranking-systems-linkedin/"
    author: "Sundara Raman Ramachandran"
    date: "2026-11-17"
---

# Scaling LLM-Based Ranking Systems for Latency-Critical Search & Recommendation Workloads

Sundara Raman Ramachandran describes how LinkedIn productionizes LLM-based ranking under strict P99 latency SLAs for search and recommendation workloads. The core approach is model distillation, shrinking a 7B-parameter model down to roughly 400M parameters while preserving ranking quality.

A second major lever is context compression: job contexts are compressed into single-token embeddings, which yields a 10x throughput improvement. This reduces the input length the model must process per request, directly cutting inference cost and latency.

Beyond the model itself, the talk emphasizes eliminating hidden system bottlenecks. Specific engineering fixes include custom flash attention masks, workarounds for the Python GIL, use of gc.freeze, and non-blocking CUDA memory copies. These systems-level optimizations are presented as essential to meeting tight P99 targets in a latency-critical serving environment.

- Distilled a 7B model down to ~400M parameters to meet P99 latency SLAs
- Compressed job contexts into single-token embeddings for a 10x throughput leap
- Addressed hidden bottlenecks: custom flash attention masks, Python GIL workarounds, gc.freeze, and non-blocking CUDA memory copies
- Productionizing LLM ranking requires both model-level and systems-level optimization