---
domain: ai-workflows
subdomain: model-release
concept: qwen38-flash-next
title: Qwen3.8-Flash-Next
sources:
  - title: "Qwen3.8-Flash-Next"
    url: "https://simonwillison.net/2026/Aug/26/qwen38-flash-next/"
    author: "Simon Willison"
    date: "2026-08-26"
---

# Qwen3.8-Flash-Next

Qwen3.8-Flash-Next is a large language model with 125B total parameters but only 6B active, enabling a significant performance boost. Simon Willison tested the model on an NVIDIA DGX Spark using Unsloth quantized GGUF versions, specifically the 72.5GB UD-IQ1_S and 78.9GB UD-Q2_K_XL variants, and shared generated examples like pelican illustrations. His favorite output came from the UD-Q2_K_XL model with xhigh reasoning effort, as highlighted in a Hacker News discussion.

- 125B total parameters but only 6B active for efficient inference.
- Tested on DGX Spark with Unsloth quantized GGUF models.
- 72.5GB UD-IQ1_S and 78.9GB UD-Q2_K_XL variants evaluated.
- Best results from UD-Q2_K_XL with xhigh reasoning effort.
- Examples include pelican-riding-a-bicycle illustrations.