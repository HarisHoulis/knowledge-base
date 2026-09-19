---
domain: ai-workflows
subdomain: inference-engineering
concept: inference-engineering-updates
title: What's New in Inference Engineering
sources:
  - title: "What's New in Inference Engineering — Philip Kiely, Baseten"
    url: "https://www.youtube.com/watch?v=75ckHC2LU_0"
    author: "AI Engineer"
    date: "2026-09-19T17:00:27+00:00"
---

# What's New in Inference Engineering

Philip Kiely's talk reviews developments in inference engineering since the publication of his book, framing the field into two emerging contexts: local inference and data-center inference (AI Engineer, 2026). In local inference, the dominant strategy is to get a model working on whatever hardware is available by compressing it through quantization, distillation, pruning, or splitting across GPUs, then reducing the resulting degradation to recover baseline intelligence at batch size one (AI Engineer, 2026). In the data-center world, the focus is on getting a model working on day zero and then making it less slow using KV-aware routing, speculation, and disaggregation (AI Engineer, 2026).

Kiely notes that the boundary between training and inference is blurring, as many inference optimizations now come from dedicated training processes. He describes a cycle in which faster inference produces more data, which is used to train a better model, which enables faster inference again (AI Engineer, 2026).

The practical day-to-day techniques for making models faster cluster around three areas: quantization, KV caching, and speculation (AI Engineer, 2026). The talk promises updates on Turboquant, KV compaction, and Deflash, with a significant focus on speculative decoding, followed by prognostications about the future of inference engineering (AI Engineer, 2026).

- Inference engineering has diverged into local inference, where the goal is to fit compressed models onto available hardware at batch size one, and data-center inference, where the goal is to reduce latency and improve throughput for batch workloads.
- Practical inference speedups commonly focus on three techniques: quantization, KV caching, and speculative decoding.
- Training and inference are increasingly intertwined, with inference optimizations often arising from dedicated training processes and faster inference feeding data back into model training.
- Recent developments highlighted include Turboquant, KV compaction, and Deflash, with substantial attention on speculative decoding.