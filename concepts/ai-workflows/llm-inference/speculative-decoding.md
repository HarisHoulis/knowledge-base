---
domain: ai-workflows
subdomain: llm-inference
concept: speculative-decoding
title: How to Make LLMs 3X Faster
sources:
  - title: "How to Make LLMs 3X Faster"
    url: "https://blog.bytebytego.com/p/how-to-make-llms-3x-faster"
    author: "ByteByteGo"
    date: "2026-08-26"
---

# How to Make LLMs 3X Faster

Speculative decoding accelerates LLM token generation by exploiting underutilized GPU memory bandwidth. During autoregressive decoding, each forward pass moves roughly 140 GB of weights for a 70B model but computes only one token, leaving compute utilization at 20–40%. A small draft model produces multiple candidate tokens, and the target model verifies them in a single forward pass, converting spare capacity into speedups of 2–3x (ByteByteGo).

- Speculative decoding uses a small draft model to propose K candidate tokens, which the target model verifies in parallel in one forward pass, keeping the longest matching prefix plus one free token.
- The method is lossless: via an adjusted acceptance rule, the output distribution remains statistically identical to the target model running alone, even under sampling.
- Acceptance rates vary by workload: structured tasks like code generation see 80–90% acceptance, while open-ended creative writing and high sampling temperatures reduce acceptance and can negate gains.
- Draft sources include a separate small model, extra prediction heads, a quantized/cheaper version of the same model, or retrieval of repeated text sequences.
- Speedups are highest at low concurrency (e.g., ~1.96x at batch size 1) and diminish as server load grows, since spare compute is consumed by other requests.