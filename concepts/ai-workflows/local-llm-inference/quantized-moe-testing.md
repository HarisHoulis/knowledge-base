---
domain: ai-workflows
subdomain: local-llm-inference
concept: quantized-moe-testing
title: Qwen3.8-Flash-Next: Quantized MoE Model on DGX Spark
sources:
  - title: "Qwen3.8-Flash-Next"
    url: "https://simonwillison.net/2026/Aug/26/qwen38-flash-next/"
    author: "Simon Willison"
    date: "2026-08-26"
  - title: "unsloth/Qwen3.8-Flash-Next-GGUF"
    url: "https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF"
    author: "Unsloth"
---

# Qwen3.8-Flash-Next: Quantized MoE Model on DGX Spark

Qwen3.8-Flash-Next is a massive language model with 125B total parameters but only 6B active, which yields a significant performance boost due to its mixture-of-experts (MoE) architecture (Simon Willison, 2026). This design allows the model to activate only a fraction of its parameters per token, making it more efficient for inference.

Willison tested the model on an NVIDIA DGX Spark using Unsloth-quantized GGUF files, specifically the 72.5GB UD-IQ1_S and the 78.9GB UD-Q2_K_XL variants (Willison, 2026). He generated pelican images via a markdown-to-SVG renderer, and his favorite output came from the UD-Q2_K_XL quant with 'xhigh' reasoning effort enabled (Willison, 2026). The post also links to a Hacker News discussion.

Overall, the post demonstrates how quantization enables running frontier-scale MoE models on local hardware, with quality varying across quant levels and reasoning effort settings.

- Qwen3.8-Flash-Next has 125B total parameters but only 6B active, offering a significant performance boost via MoE.
- Unsloth quantized GGUF versions allow local execution on a DGX Spark.
- Two quant variants tested: UD-IQ1_S (72.5GB) and UD-Q2_K_XL (78.9GB).
- Best result came from UD-Q2_K_XL with xhigh reasoning effort.