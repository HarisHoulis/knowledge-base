---
domain: ai-workflows
subdomain: model-architecture
concept: mixture-of-experts
title: The New American AI Model Designed to be Customized
sources:
  - title: "The New American AI Model Designed to be Customized"
    url: "https://blog.bytebytego.com/p/the-new-american-ai-model-designed"
    author: "ByteByteGo"
    date: "2026-08-18"
---

# The New American AI Model Designed to be Customized

Thinking Machines released Inkling, its first from-scratch model, on July 15, 2026. The model uses a Mixture-of-Experts (MoE) architecture with 66 layers, each containing 256 experts, but only six routed experts plus two shared experts are active per token. This sparsity separates storage cost from inference cost: the full checkpoint holds 975 billion parameters, yet processing a single token involves only about 41 billion parameters, roughly 4% of the model. The weights are available on Hugging Face under Apache 2.0, allowing anyone to download and retrain the model on their own data [1][2].

To avoid routing collapse—where a few experts dominate and the rest remain underdeveloped—Thinking Machines uses a bias-based balancing method introduced by Wang et al. and also adopted by DeepSeek. Each expert has a bias value that influences selection only, not output weighting, and is updated by a simple counting rule outside backpropagation. This prevents conflicting gradients from degrading text quality while keeping expert usage balanced [1][8][9].

Inkling's attention is designed for a 1-million-token context window with a hybrid approach: 55 sliding-window layers and 11 full-attention layers (a 5:1 ratio). This lets the model process long documents efficiently, as full-attention layers allow long-range information to propagate while the sliding-window layers handle local context at low cost. Additionally, Inkling uses 8 key-value heads to reduce memory during generation [1][2][7].

For position encoding, the model deliberately uses an older technique instead of the current standard RoPE, a choice likely made to handle sequence lengths not seen during training. The article also outlines other design aspects such as multimodal input without separately pretrained encoders and a 'thinking effort' control, though the provided excerpt focuses on the architectural details described here.

- Inkling is Thinking Machines' first from-scratch model, released under Apache 2.0 with weights on Hugging Face.
- MoE architecture: 975B total parameters, ~41B active per token, with 66 layers × 256 experts, selecting 6 routed + 2 shared experts per token.
- Routing collapse is mitigated via a bias-based balancing method that separates selection from weighting, avoiding conflicting gradients.
- A 5:1 mix of sliding-window and full-attention layers enables a 1M-token context window efficiently.
- Inkling uses an older position encoding method rather than RoPE, likely to handle lengths unseen in training.