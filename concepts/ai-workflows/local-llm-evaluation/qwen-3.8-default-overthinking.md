---
domain: ai-workflows
subdomain: local-llm-evaluation
concept: qwen-3.8-default-overthinking
title: Qwen 3.8 27B is excellent, but defaults to wildly overthinking things
sources:
  - title: "Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things"
    url: "https://simonwillison.net/2026/Aug/16/qwen-38-27b/"
    author: "Simon Willison"
    date: "2026-08-16"
---

# Qwen 3.8 27B is excellent, but defaults to wildly overthinking things

Qwen 3.8 27B is an Apache 2 licensed, 27B parameter vision-capable LLM from Alibaba. According to the article, it shows significant benchmark gains over both Qwen 3.6 27B and the closed-weight Qwen 3.7-Plus (Simon Willison, 2026). The author ran the 17GB Q4_K_M quantization on a 128GB M5 Max MacBook Pro and an NVIDIA DGX Spark, finding that the model defaults to `xhigh` reasoning effort, which leads to excessive reasoning traces and extremely slow generation. For example, generating an SVG of a pelican riding a bicycle took 21 minutes, using 22,276 reasoning tokens to produce 3,223 tokens of output (Simon Willison, 2026). The author strongly recommends dialing reasoning down to low or off for most tasks, as the default is impractical on consumer hardware (Simon Willison, 2026).

- Qwen 3.8 27B defaults to `xhigh` reasoning effort, causing extreme overthinking and very slow output (e.g., 21 minutes for an SVG) (Simon Willison, 2026).
- Despite the overthinking, the model produces excellent results: the best pelican SVG the author has generated locally, accurate bounding boxes for pelicans, and a fully functional HTML tool built from a single prompt (Simon Willison, 2026).
- Turning reasoning off can break tasks that need careful spatial reasoning; a bounding box tool generated without reasoning placed boxes incorrectly (Simon Willison, 2026).
- Local inference speed is slow at ~15-30 tokens/s, but Multi-Token Prediction (draft-mtp) in llama.cpp provided a ~72% speedup over the LM Studio default (Simon Willison, 2026).
- The model's 17GB size demonstrates that open-weight models can handle long context, tool calling, vision, and code generation on high-end consumer hardware (Simon Willison, 2026).