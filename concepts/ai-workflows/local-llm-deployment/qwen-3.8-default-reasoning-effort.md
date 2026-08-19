---
domain: ai-workflows
subdomain: local-llm-deployment
concept: qwen-3.8-default-reasoning-effort
title: Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things
sources:
  - title: "Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things"
    url: "https://simonwillison.net/2026/Aug/16/qwen-38-27b/"
    author: "Simon Willison"
    date: "2026-08-16"
---

# Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things

Qwen 3.8 27B is a strong open-weights, vision-capable LLM that runs locally on a 17GB file, with benchmark results outperforming earlier Qwen versions and even the closed-weight Qwen 3.7-Plus (Simon Willison, 2026). However, its default `reasoning_effort` setting is `xhigh`, which leads to excessive thinking and extremely slow generation. For example, producing an SVG of a pelican riding a bicycle took 21 minutes and 22,276 reasoning tokens, while the same prompt with reasoning turned off took just 137 seconds and produced only 3,715 tokens. Even a simple request for an SVG of a circle triggered a long internal monologue and an elaborate animated result, illustrating how over-thinking dominates the default experience.

- Qwen 3.8 27B defaults to `xhigh` reasoning effort, causing huge token overuse and slow responses.
- Disabling or lowering reasoning effort makes the model drastically faster while still producing good results for many tasks.
- The model excels at vision tasks (e.g., bounding boxes) and can drive coding-agent loops with tools like Pi.
- Local inference speeds are around 15-30 tokens/sec, but multi-token prediction (MTP) can boost performance by ~72%.
- A 17GB model can now handle complex tasks that previously required much larger or proprietary systems.