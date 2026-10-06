---
domain: ai-workflows
subdomain: llm-inference-optimization
concept: speculative-decoding
title: Is Speculative Decoding Worth It? Profiling vLLM on NVIDIA Blackwell
sources:
  - title: "Is Speculative Decoding Worth It? Profiling vLLM on NVIDIA Blackwell — Akamai"
    url: "https://www.youtube.com/watch?v=XTpyNrEgJQ4"
    author: "AI Engineer"
    date: "2026-10-06T22:30:02+00:00"
---

# Is Speculative Decoding Worth It? Profiling vLLM on NVIDIA Blackwell

LLM inference has two main phases: prefill, where the model reads the query, processes incoming tokens, and creates a KV cache once, and decoding, where the model generates the response autoregressively one token at a time. For a large model such as a 70B Llama model, this can require many model transfers and introduce significant latency [1].

Speculative decoding aims to reduce that cost by using a smaller draft model to speculate multiple tokens—typically three to five per cycle—in a faster, cheaper autoregressive process. The target model then validates the draft predictions in one pass, approving or rejecting them and recalculating rejected tokens. The output remains the same because the accurate target model still validates the tokens [1].

It is not free: speculative decoding requires hosting two models, allocating memory for the second model, and reserving extra KV cache space for both. It is generally worth considering when there is spare GPU capacity; if the workload is highly parallel and the GPUs are already busy fulfilling requests, it may not make sense [1].

Choosing a draft model involves balancing accuracy and speed. The draft model should usually be 10 to 50 times smaller than the target model, use the same tokenizer, and ideally come from the same model family. Structured workloads such as coding, JSON, or SQL queries are more likely to benefit, while creative tasks like writing poetry or brainstorming are less likely to benefit. In the demo, a single NVIDIA Blackwell GPU was used, splitting resources between a base model taking about 16 GB of weights and a draft model taking about 2.5 GB, leaving space for KV caching [1].

- Speculative decoding uses a smaller draft model to propose multiple tokens per cycle, which the target model validates in one pass and recalculates when rejected.
- The overhead includes hosting a second model and allocating KV cache for both models, so it is most attractive when spare GPU capacity is available.
- Draft model selection should balance accuracy and speed; it is typically 10–50x smaller, shares the same tokenizer, and ideally belongs to the same model family.
- Benefits are strongest for structured outputs like code, JSON, and SQL, and weaker for open-ended creative tasks such as poetry or brainstorming.
- The demo split a single Blackwell GPU between a base model (~16 GB weights) and a draft model (~2.5 GB).