---
domain: ai-workflows
subdomain: llm-inference
concept: speculative-decoding
title: How to Make LLMs 3X Faster
sources:
  - title: "How to Make LLMs 3X Faster"
    url: "https://blog.bytebytego.com/p/how-to-make-llms-3x-faster"
    author: "ByteByteGo"
    date: "Wed, 26 Aug 2026 15:30:34 GMT"
---

# How to Make LLMs 3X Faster

The article explains why autoregressive token generation is slow: each forward pass requires reading model weights from GPU memory, and since a single token applies to a tiny vector, compute units remain idle most of the time. Speculative decoding exploits this spare capacity by using a small draft model to propose several candidate tokens, which the large target model then verifies in a single parallel forward pass. This can deliver 2–3x faster generation while producing text that is statistically identical to the target model running alone, thanks to a careful accept/reject rule that preserves the target distribution (ByteByteGo).

Acceptance rate—the fraction of draft tokens kept—varies by workload and sampling temperature. Code, summarization, and retrieval-based tasks show high acceptance, while open-ended creative writing lowers it. The technique also degrades with high concurrency, as the previously idle compute becomes saturated by real requests. The article surveys four draft sources: a separate small model, extra prediction heads, a quantized/cheaper version of the same model, and text reuse from context, each with tradeoffs in complexity, training cost, and VRAM usage (ByteByteGo).

- Token generation is memory-bandwidth-bound: a 70B model moves ~140GB of weights per token, leaving compute utilization at only 20–40%.
- Speculative decoding uses a small draft model to generate candidate tokens and the large model verifies them in one pass, yielding 2–3x speedup.
- The accept/reject rule guarantees output statistically identical to the target model's own distribution.
- Acceptance rate is higher for structured tasks like code and summarization; gains shrink when concurrency saturates the GPU.