---
domain: ai-workflows
subdomain: local-llm-reasoning
concept: qwen3-8-27b-overthinking
title: Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things
sources:
  - title: "Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things"
    url: "https://simonwillison.net/2026/Aug/16/qwen-38-27b/"
    author: "Simon Willison"
    date: "2026-08-16"
---

# Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things

Qwen 3.8 27B, an Apache 2 licensed 27B-parameter vision-capable LLM from Alibaba, shows strong benchmark improvements over its predecessor and even the closed-weight Qwen 3.7-Plus. It runs locally on consumer hardware (e.g., 128GB MacBook Pro, NVIDIA DGX Spark) via LM Studio's 17GB Q4_K_M quantized build. However, the model defaults to an 'xhigh' reasoning effort, which causes severe overthinking: generating a pelican SVG took 21 minutes and 22,276 reasoning tokens, while the same prompt with reasoning disabled took just 137 seconds and 3,715 tokens. Even a simple request like 'draw an svg of a circle' triggered elaborate creative spirals, producing a beautiful but unwanted animated circle. The author strongly recommends overriding the default to low or no reasoning for most tasks (Willison, 2026).

- Qwen 3.8 27B is a 17GB local model with vision, long context, tool calling, and strong code generation, but its default xhigh reasoning effort leads to wildly excessive thinking and slow response times.
- Disabling reasoning dramatically improves speed: the pelican SVG dropped from 21 minutes to 2 minutes, and simple prompts no longer spiral into needless complexity.
- Despite the overthinking, the model performs well on practical tasks like bounding-box prediction and coding-agent loops, though it feels slow (15-30 tokens/sec) compared to hosted APIs.
- Multi-Token Prediction (MTP) in llama.cpp provided a ~72% speed boost, suggesting performance optimizations will continue to improve.
- The key takeaway: local open-weights models are now capable enough for real work, but users must manage reasoning effort to balance quality and speed.