---
domain: ai-workflows
subdomain: model-architecture
concept: sparse-mixture-of-experts
title: The New American AI Model Designed to be Customized
sources:
  - title: "The New American AI Model Designed to be Customized"
    url: "https://blog.bytebytego.com/p/the-new-american-ai-model-designed"
    author: "ByteByteGo"
    date: "Tue, 18 Aug 2026 15:30:36 GMT"
---

# The New American AI Model Designed to be Customized

Inkling is open-sourced under Apache 2.0, allowing anyone to download and fine-tune it. The company's broader mission includes building tools for customization, which aligns with their earlier Tinker service and their focus on extending human will. The model also introduces a 'thinking effort' setting to control reasoning depth. Overall, Inkling demonstrates how sparse attention and MoE can make a trillion-parameter-scale model practical [1][2][3][4].

- Inkling uses sparse MoE: 975B total params but only ~41B active per token, with 6 routed + 2 shared experts per layer.
- Routing employs sigmoid scores and bias-based selection (from DeepSeek) to avoid routing collapse without gradient conflicts.
- Context window of 1M tokens is handled by alternating 55 sliding-window and 11 full-attention layers (5:1 ratio).
- Model is open-source (Apache 2.0) and designed for customization, aligning with Thinking Machines' mission.
- Older position encoding chosen over RoPE, possibly due to training on very long sequences.