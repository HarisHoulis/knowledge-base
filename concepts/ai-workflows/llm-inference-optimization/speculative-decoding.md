---
domain: ai-workflows
subdomain: llm-inference-optimization
concept: speculative-decoding
title: How to Make LLMs 3X Faster
sources:
  - title: "How to Make LLMs 3X Faster"
    url: "https://blog.bytebytego.com/p/how-to-make-llms-3x-faster"
    author: "ByteByteGo"
    date: "Wed, 26 Aug 2026 15:30:34 GMT"
---

# How to Make LLMs 3X Faster

Autoregressive decoding generates text one token at a time, requiring a separate forward pass for each token. For a 70-billion-parameter model, each pass loads roughly 140 GB of weights from GPU memory, but the compute units are idle most of the time, with utilization dropping to 20–40% during token generation. This memory-bandwidth bottleneck leaves significant spare compute capacity that speculative decoding exploits (ByteByteGo, 2026).

Speculative decoding pairs the large target model with a much smaller draft model that proposes K candidate tokens. The target model then verifies all candidates in a single forward pass, using the transformer's ability to process multiple positions in parallel with causal masking. Candidates matching the target model's predictions are kept; at the first mismatch, the target model's own token is used, ensuring the output is statistically identical to running the target model alone. This yields 2–3x faster generation in typical cases (ByteByteGo, 2026).

The speedup depends heavily on acceptance rate, which varies by workload. Structured output like code, summarization, and extraction accepts 80–90% of draft tokens (as reported for DeepSeek-V3), while open-ended creative writing accepts fewer. Higher sampling temperature lowers acceptance, and speedups diminish when acceptance drops below ~50%. Gains also shrink under high concurrency, with a reported decline from 1.96x at batch size 1 to 1.21x at batch size 128. Four draft sources exist: a separate small model, extra prediction heads, a quantized/skipped version of the target, and search over existing text (ByteByteGo, 2026).

- Token generation is memory-bound: loading model weights dominates each forward pass, leaving compute underutilized.
- Speculative decoding uses a small draft model to propose candidate tokens, verified in parallel by the large model in one pass.
- The acceptance/rejection rule guarantees output statistically identical to the target model alone.
- Acceptance rate is workload-dependent; code and structured tasks benefit most, while creative writing offers smaller gains.
- Speedups degrade under high concurrency and with high sampling temperature, so the technique is best for low-batch or compute-spare scenarios.