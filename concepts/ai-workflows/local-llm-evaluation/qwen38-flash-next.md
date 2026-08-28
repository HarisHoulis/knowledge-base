---
domain: ai-workflows
subdomain: local-llm-evaluation
concept: qwen38-flash-next
title: Qwen3.8-Flash-Next
sources:
  - title: "Qwen3.8-Flash-Next"
    url: "https://simonwillison.net/2026/Aug/26/qwen38-flash-next/"
    date: "2026-08-26"
---

# Qwen3.8-Flash-Next

Qwen3.8-Flash-Next is a Mixture-of-Experts (MoE) language model with 125B total parameters but only 6B active, providing a significant performance boost. Simon Willison tested the model on a DGX Spark using Unsloth quantized GGUF versions, including the 72.5GB UD-IQ1_S and 78.9GB UD-Q2_K_XL variants. He generated images of pelicans via a markdown-to-SVG rendering tool, with his favorite result coming from the UD-Q2_K_XL quant at 'xhigh' reasoning effort. The post highlights the practicality of running large MoE models locally on NVIDIA DGX Spark hardware with quantized weights.

- Qwen3.8-Flash-Next has 125B total parameters but only 6B active due to MoE architecture, boosting efficiency.
- Tested on a DGX Spark using Unsloth quantized GGUF models (UD-IQ1_S and UD-Q2_K_XL).
- The UD-Q2_K_XL quant at xhigh reasoning effort produced the best pelican images.
- Images were generated via a markdown-to-SVG rendering tool, demonstrating multimodal output from the LLM.