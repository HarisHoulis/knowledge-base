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

ByteByteGo's article explains that LLM text generation is inherently sequential because each token depends on the previous one, requiring one forward pass per token. However, these forward passes are memory-bound: for a 70B-parameter model, loading 140 GB of weights per token leaves GPU compute units idle 60-80% of the time during generation. Speculative decoding exploits this idle capacity by using a small draft model to propose multiple candidate tokens, which the large target model then verifies in a single forward pass via the parallel processing capabilities of transformers and causal masking. This yields 2-3x faster generation while producing statistically identical output to the target model running alone (ByteByteGo, 2026).

The accept/reject loop compares each candidate against the target model's predictions. Matching tokens are kept, and the first mismatch yields a free correct token from the target model's own prediction, limiting the downside to one useful token per pass. The acceptance rate depends heavily on workload: structured and repetitive outputs like code or summarization see high acceptance—DeepSeek reported 80-90% for second-token acceptance, producing 1.8x throughput—while open-ended creative writing has lower acceptance. Higher sampling temperature also reduces acceptance (ByteByteGo, 2026).

The article identifies four possible draft sources: a separate small model from the same family, extra prediction heads trained on the target model (as with DeepSeek-V3), a quantized or layer-skipping version of the same model (e.g., QuantSpec with 4-bit weights achieving 1.78x speedup), and retrieval of text spans from the prompt or previous output. The speedup is also contingent on server concurrency: at batch size 1, up to 1.96x is possible, but this drops to 1.21x at batch size 128 as compute units saturate (ByteByteGo, 2026).

- Token generation is memory-bandwidth-bound, not compute-bound, leaving GPU math units idle most of the time.
- Speculative decoding uses a small draft model to propose K candidate tokens, then the target model verifies them all in one parallel forward pass, preserving output distribution via a careful accept/reject rule.
- Speedup depends on acceptance rate, which is higher for structured/repetitive workloads and lower for open-ended generation or high-temperature sampling.
- Four draft sources exist: separate small model, extra prediction heads, a cheaper quantized version, or search over existing text; each has trade-offs in cost and complexity.
- Gains shrink under high concurrency; a 70B model saw 1.96x speedup at batch size 1 but only 1.21x at batch size 128.