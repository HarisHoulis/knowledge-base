---
domain: ai-workflows
subdomain: local-llm-for-coding
concept: local-model-viability
title: Viability of local models for coding
sources:
  - title: "Viability of local models for coding"
    url: "https://martinfowler.com/articles/exploring-gen-ai/local-models-for-coding-factors.html"
    author: "Martin Fowler"
---

# Viability of local models for coding

In [this article](https://martinfowler.com/articles/exploring-gen-ai/local-models-for-coding-factors.html), Martin Fowler shares his hands-on experience running local AI models for coding over four weeks, focusing on agentic use and usability for developers. He tested models on an Apple M3 Max (48GB) and an M5 Pro (64GB), covering a range of factors that influence viability such as RAM, processing power, memory bandwidth, parameter count, reasoning capabilities, tool calling, format, quantization, architecture, context window size, runtime, and harness choice.

Fowler identifies RAM as the core constraint: models between 15-25GB are comfortable on 48GB, while larger models can crash or become unusably slow. Response speeds were impressive compared to a year ago but degrade with longer conversations. Tool calling remains a common failure point for agentic coding, though models often self-correct, and smaller models sometimes perform better with reasoning disabled. Context windows need to be at least 32K-64K, but memory limits often prevent using larger windows.

Overall, Fowler concludes that local models are still messy and not a plug-and-play experience for developers. However, he found the Qwen3.6 35B MoE model to be the best balance of capability, speed, and RAM footprint among those tested, and it is now his go-to local model.

- RAM is the primary bottleneck; models in the 15-25GB range fit comfortably on 48GB systems, but larger models risk crashes.
- Response speed has improved dramatically, but degrades as conversation context grows.
- Tool calling for agentic coding is still unreliable, though models often self-correct from malformed calls.
- Reasoning can be counterproductive for smaller models; turning it off sometimes improves performance.
- Qwen3.6 35B MoE offered the best trade-off between capability, speed, and RAM usage.