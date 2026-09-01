---
domain: ai-workflows
subdomain: llm-inference-optimization
concept: speculative-decoding
title: How to Make LLMs 3X Faster
sources:
  - title: "How to Make LLMs 3X Faster"
    url: "https://blog.bytebytego.com/p/how-to-make-llms-3x-faster"
    author: "ByteByteGo"
    date: "2026-08-26"
---

# How to Make LLMs 3X Faster

Speculative decoding speeds up LLM token generation by exploiting the memory-bandwidth-bound nature of autoregressive decoding. A 70B model must stream ~140 GB of weights from VRAM for every single token, leaving GPU compute units idle most of the time (ByteByteGo, 2026). To use this spare capacity, a small draft model generates several candidate tokens in advance, and the large target model verifies them all in one parallel forward pass using causal masking. This converts one token per pass into several tokens per pass, delivering 2-3x speedups while producing statistically identical output.

- Autoregressive generation requires one forward pass per token, and each pass is dominated by weight transfer, not arithmetic.
- Speculative decoding pairs a large target model with a much smaller draft model; the draft proposes K tokens, and the target verifies them simultaneously in a single pass.
- Tokens are accepted or rejected against the target model's probabilities, with a rejection-replacement rule that preserves the exact output distribution, making it lossless.
- Acceptance rates vary by workload: code, summarization, and structured output accept 80-90% of drafts, while open-ended creative writing accepts far fewer.
- Gains shrink under high concurrency because spare compute disappears; a 70B model speedup drops from ~1.96x at batch size 1 to ~1.21x at batch size 128.