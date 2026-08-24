---
domain: ai-workflows
subdomain: model-architecture
concept: inkling-architecture
title: Inkling: A Customizable Sparse Mixture-of-Experts AI Model
sources:
  - title: "The New American AI Model Designed to be Customized"
    url: "https://blog.bytebytego.com/p/the-new-american-ai-model-designed"
    author: "ByteByteGo"
    date: "Tue, 18 Aug 2026 15:30:36 GMT"
---

# Inkling: A Customizable Sparse Mixture-of-Experts AI Model

Thinking Machines released Inkling, its first model trained from scratch, designed to be customized by users. The article details five architectural choices: sparse Mixture of Experts, hybrid attention, an older position-encoding method, direct multimodal input, and a tunable 'thinking effort' setting. Inkling has 66 layers, each with 256 experts; only 6 routed and 2 shared experts activate per token, giving 975B total parameters but ~41B active parameters per token (ByteByteGo, 2026).

- Inkling uses sparse Mixture of Experts with 256 experts per layer, activating 6 routed and 2 shared experts per token, reducing compute to about 4% of total parameters.
- The router applies sigmoid scores and a separate bias updated outside backpropagation to prevent routing collapse without conflicting training gradients.
- Attention is hybrid: 55 sliding-window layers and 11 full-attention layers support a 1M-token context at near-linear cost.
- The model uses an older position-encoding method instead of RoPE, and accepts images/audio without a separately pretrained encoder.
- Weights are available on Hugging Face under Apache 2.0, and the architecture largely follows DeepSeek's MoE approach.