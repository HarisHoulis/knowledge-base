---
domain: ai-workflows
subdomain: llm-architecture
concept: inkling-model
title: The New American AI Model Designed to be Customized
sources:
  - title: "The New American AI Model Designed to be Customized"
    url: "https://blog.bytebytego.com/p/the-new-american-ai-model-designed"
    author: "ByteByteGo"
    date: "Tue, 18 Aug 2026 15:30:36 GMT"
---

# The New American AI Model Designed to be Customized

Thinking Machines released Inkling, a large language model with a Mixture of Experts (MoE) architecture, on July 15, 2026. The model has 975 billion total parameters but only about 41 billion are active for any token, achieved by routing each token through 6 out of 256 experts per layer plus 2 shared experts [1][2]. The routing uses a bias-based load-balancing method from DeepSeek to prevent routing collapse without conflicting gradients [1][8][9]. This sparsity makes the model feasible to run: the full-precision checkpoint requires 2 TB of GPU memory, while a quantized version fits in about 600 GB [2].

- Inkling is an Apache 2.0-licensed MoE model with 66 layers, 256 experts per layer, and 6 routed experts active per token, plus 2 shared experts [1][2].
- The router uses sigmoid scores and a separate bias mechanism for load balancing, avoiding routing collapse without degrading text quality [1][9].
- A context window of 1 million tokens is handled by alternating sliding-window and full-attention layers at a 5:1 ratio (55 local, 11 global) [1][7].
- The model uses an older position encoding method instead of RoPE, a deliberate choice for lengths unseen during training.
- Thinking Machines emphasizes customization: the weights are openly downloadable and the company also offers Tinker, a fine-tuning service [4].