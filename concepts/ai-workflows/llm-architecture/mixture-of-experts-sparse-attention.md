---
domain: ai-workflows
subdomain: llm-architecture
concept: mixture-of-experts-sparse-attention
title: The New American AI Model Designed to be Customized
sources:
  - title: "The New American AI Model Designed to be Customized"
    url: "https://blog.bytebytego.com/p/the-new-american-ai-model-designed"
    author: "ByteByteGo"
    date: "Tue, 18 Aug 2026 15:30:36 GMT"
---

# The New American AI Model Designed to be Customized

Thinking Machines released Inkling on July 15, 2026 as its first from-scratch model, with weights on Hugging Face under Apache 2.0 (ByteByteGo, 2026). It is a Mixture-of-Experts transformer with 975B total parameters but only ~41B active per token: each of the 66 layers has 256 experts, of which six are routed per token, plus two shared experts that always run (ByteByteGo, 2026). To avoid routing collapse, Thinking Machines uses a bias-based routing method from Wang/DeepSeek that adjusts expert selection without injecting a competing gradient into the training objective (ByteByteGo, 2026).

Inkling supports a 1M-token context. Most layers use sliding-window attention; the 66 layers split into 55 sliding-window and 11 full-attention layers (5:1), and the model uses 8 key-value heads (ByteByteGo, 2026). For position encoding, Thinking Machines chose an older method rather than RoPE, the current standard, because of the long lengths not seen during training (ByteByteGo, 2026). The model also takes images and audio without a separately pretrained encoder, and exposes a 'thinking effort' setting between 0 and 1 that controls how much reasoning happens before answering (ByteByteGo, 2026).

The company's mission is to extend human will and judgment, and Inkling is designed to be customized: before Inkling, Thinking Machines shipped Tinker, a fine-tuning service, and the open Apache 2.0 weights let anyone retrain on their own data (ByteByteGo, 2026).

- Inkling is a 975B-parameter MoE model with ~41B active parameters per token, using 66 layers, 256 experts per layer, 6 routed experts plus 2 shared experts per token.
- Bias-based routing (from Wang/DeepSeek) prevents routing collapse without adding a conflicting gradient to the training objective.
- Long context is handled by alternating 55 sliding-window layers with 11 full-attention layers, plus 8 key-value heads, for a 1M-token context window.
- Position encoding uses an older method instead of RoPE to better extrapolate to lengths not seen during training.
- Images and audio enter the model directly without a separately pretrained encoder, and a 'thinking effort' control (0 to 1) adjusts reasoning depth.
- Weights are open under Apache 2.0 on Hugging Face, enabling anyone to download and retrain the model on custom data.