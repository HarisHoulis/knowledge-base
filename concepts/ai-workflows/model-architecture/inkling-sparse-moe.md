---
domain: ai-workflows
subdomain: model-architecture
concept: inkling-sparse-moe
title: The New American AI Model Designed to be Customized
sources:
  - title: "The New American AI Model Designed to be Customized"
    url: "https://blog.bytebytego.com/p/the-new-american-ai-model-designed"
    author: "ByteByteGo"
    date: "Tue, 18 Aug 2026 15:30:36 GMT"
---

# The New American AI Model Designed to be Customized

Thinking Machines released Inkling, their first from-scratch model, on July 15, 2026. Inkling is a sparse Mixture-of-Experts (MoE) transformer with 975 billion total parameters but only about 41 billion active per token, achieved by using 256 experts per layer and activating just 6 routed experts plus 2 shared experts per token [1][2]. The architecture largely follows DeepSeek's approach, including a bias-based routing method that prevents expert collapse without conflicting gradients [1][8][9]. This design allows the model to be efficiently run on 8 NVIDIA B300 or 16 H200 GPUs in full precision, or on 4 B300s with quantization [2].

Inkling supports a one-million-token context window by alternating between sliding-window attention and full attention at a 5:1 ratio—55 sliding-window layers and 11 full-attention layers—so long-range information propagates through the full-attention layers while most layers only process recent tokens [1][7]. The model uses an older positional encoding method rather than the current RoPE standard, and it processes images and audio directly without a separately pretrained encoder [1][2]. A novel 'thinking effort' setting between 0 and 1 adjusts how much the model reasons before answering, and the weights are released under Apache 2.0 on Hugging Face for customization [2]. The company's mission, led by ex-OpenAI CTO Mira Murati, emphasizes extending human will and judgment through customizable AI [3].

- Inkling is a 975B-parameter sparse MoE model with only ~41B active parameters per token, using 256 experts per layer with 6 routed + 2 shared experts.
- It alternates sliding-window and full-attention layers at 5:1 to handle a 1M-token context efficiently.
- Uses an older positional encoding instead of RoPE, and processes images/audio without a pretrained encoder.
- Includes a 'thinking effort' dial (0–1) to control reasoning depth.
- Released open-weight under Apache 2.0, allowing anyone to download and fine-tune.