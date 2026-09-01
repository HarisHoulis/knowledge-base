---
domain: ai-workflows
subdomain: llm-evaluation
concept: qwen38-flash-next
title: Qwen3.8-Flash-Next
sources:
  - title: "Qwen3.8-Flash-Next"
    url: "https://simonwillison.net/2026/Aug/26/qwen38-flash-next/"
    author: "Simon Willison"
    date: "2026-08-26"
---

# Qwen3.8-Flash-Next

Qwen3.8-Flash-Next is a large language model with 125B total parameters but only 6B active, resulting in significant performance boosts during inference. Simon Willison tested it on a DGX Spark using Unsloth quantized GGUF models, specifically the 72.5GB UD-IQ1_S and 78.9GB UD-Q2_K_XL versions. His experiments included generating images of pelicans, with the UD-Q2_K_XL model at 'xhigh' reasoning effort producing his favorite result. The post highlights the model's efficiency and quality at different quantization levels, and notes that the model is part of the AI-in-China ecosystem.

- Qwen3.8-Flash-Next has 125B total parameters but only 6B active, boosting performance.
- Willison tested Unsloth quantized GGUF models on a DGX Spark.
- The 78.9GB UD-Q2_K_XL with xhigh reasoning effort produced the best pelican images.
- The model supports efficient local inference with quantized formats.