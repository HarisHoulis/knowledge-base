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

Autoregressive text generation is inherently sequential: a 500-token response requires 500 forward passes, each reading the entire model's weights from memory. For a 70-billion-parameter model, that means transferring ~140 GB of weights per token, while compute utilization during token generation is only 20-40% because the arithmetic per token is trivial compared to the memory traffic (ByteByteGo, https://blog.bytebytego.com/p/how-to-make-llms-3x-faster).

Speculative decoding converts this spare compute into speed by pairing a small draft model with the large target model. The draft model proposes several candidate tokens, and the target model verifies them in a single forward pass using parallel sequence processing. Through an accept/reject rule, the output remains statistically identical to the target model running alone, while achieving 2-3x faster generation. The downside is bounded because the first token from the target model is always kept even if all candidates fail (ByteByteGo, https://blog.bytebytego.com/p/how-to-make-llms-3x-faster).

The speedup depends heavily on acceptance rate, which varies by workload: structured tasks like code generation and summarization accept 80-90% of draft tokens, while open-ended creative writing accepts far fewer. Draft sources can be a separate small model, extra prediction heads, a quantized version of the target, or even reuse of existing context text. However, gains shrink under high concurrency: one evaluation showed the speedup dropping from 1.96x at batch size 1 to 1.21x at batch size 128, as compute becomes saturated by real requests (ByteByteGo, https://blog.bytebytego.com/p/how-to-make-llms-3x-faster).

- Token generation is sequential and memory-bound: a 70B model reads ~140 GB of weights per token, leaving compute utilization at 20–40%.
- Speculative decoding uses a small draft model to propose candidates, which the target model verifies in a single parallel forward pass, yielding 2–3x speedup.
- The accept/reject rule guarantees output statistically identical to the target model alone, preserving quality losslessly.
- Acceptance rate is higher for repetitive/structured tasks (e.g., code) and lower for open-ended creative text; higher temperature reduces acceptance.
- Speedup degrades at high concurrency (from ~2x at batch 1 down to ~1.2x at batch 128) because spare compute disappears.