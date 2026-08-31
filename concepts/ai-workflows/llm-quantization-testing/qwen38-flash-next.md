---
domain: ai-workflows
subdomain: llm-quantization-testing
concept: qwen38-flash-next
title: Qwen3.8-Flash-Next
sources:
  - title: "Qwen3.8-Flash-Next"
    url: "https://simonwillison.net/2026/Aug/26/qwen38-flash-next/"
    author: "Simon Willison"
    date: "2026-08-26"
---

# Qwen3.8-Flash-Next

Simon Willison's post introduces Qwen3.8-Flash-Next, a large language model with 125B total parameters but only 6B active, which provides a significant performance boost during inference. He tested the model on an NVIDIA DGX Spark using Unsloth's quantized GGUF versions, noting that the 72.5GB UD-IQ1_S and 78.9GB UD-Q2_K_XL variants produced different outputs. His favorite result came from the UD-Q2_K_XL quant with 'xhigh' reasoning effort. The model is tagged with 'pelican-riding-a-bicycle' among other AI-related tags, suggesting it was tested with a quirky prompt.

- Qwen3.8-Flash-Next has 125B total parameters but only 6B active, enabling a significant performance boost.
- Simon Willison evaluated the model on a DGX Spark using Unsloth's quantized GGUF versions (72.5GB UD-IQ1_S and 78.9GB UD-Q2_K_XL).
- The best output observed was from the UD-Q2_K_XL quant with 'xhigh' reasoning effort.
- The test involved generating images of pelicans riding bicycles, as indicated by the 'pelican-riding-a-bicycle' tag.