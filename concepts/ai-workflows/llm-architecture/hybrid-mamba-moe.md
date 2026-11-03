---
domain: ai-workflows
subdomain: llm-architecture
concept: hybrid-mamba-moe
title: How Nvidia's New Nemotron Model Works
sources:
  - title: "How Nvidia's New Nemotron Model Works"
    url: "https://blog.bytebytego.com/p/how-nvidias-new-nemotron-model-works"
    author: "ByteByteGo"
    date: "2026-11-02"
---

# How Nvidia's New Nemotron Model Works

Nvidia's Nemotron is a family of transformer-based LLMs designed around a central trade-off: keeping strong model capacity while cutting computation and memory costs. The article explains the mechanics of text generation—tokenization, embeddings, layer processing, and autoregressive decoding—and why efficiency matters especially for AI agents that make dozens of repeated model calls (e.g., coding agents). The Nemotron Lightning model, with 30 billion total parameters, targets this repeated-execution cost.

The article breaks down where transformers spend resources: attention moves information between tokens via query/key/value matching, while feed-forward networks refine each position's representation. Full attention grows quadratically with prompt length, and KV caching reduces this to linear growth but still consumes memory. Nemotron 3 addresses this by combining Mamba layers—which maintain a fixed-size running state with constant per-token update cost—with attention layers that preserve precise access to distant positions, interleaved in a defined layer sequence.

A mixture-of-experts (MoE) design adds capacity without activating all parameters: Lightning uses 128 routed experts per MoE layer with 6 selected per token, so roughly 30 billion total parameters but only ~3 billion active per token. Grouped-query attention (32 query heads, 2 key-value heads) further reduces stored key-value representations. Training progresses from pretraining on broad crawled and synthetic data toward high-quality material, then supervised fine-tuning (objective computed on assistant tokens), then reinforcement learning via GRPO with an environment that checks math, code, instruction compliance, and output schemas.

Multi-token prediction trains an auxiliary mechanism to predict further ahead, enabling speculative decoding where a draft proposes tokens and the main model verifies them, advancing several positions per pass. NVFP4 quantization (4-bit values with FP8 group scales and tensor-level scaling) plus quantization-aware distillation shrinks a BF16 model from ~66 GB to ~22 GB. Larger variants (Super: 120B total/12B active; Ultra: 550B total/55B active) add LatentMoE, which projects representations into a smaller space for routed expert computation to save memory traffic and communication.

- Nemotron interleaves Mamba layers (fixed-size state, constant per-token cost) with attention layers (precise long-range access) to cut sequence-processing costs.
- MoE with 128 routed experts and 6 selected per token lets a ~30B-parameter model use only ~3B parameters per token, though total parameters still drive memory needs.
- Grouped-query attention (32 query heads, 2 KV heads) reduces stored key-value representations while retaining multiple query paths.
- Training follows pretraining → supervised fine-tuning (loss on assistant tokens) → GRPO reinforcement learning with an evaluation environment for math, code, and schema compliance.
- Multi-token prediction enables speculative decoding, and NVFP4 quantization with quantization-aware distillation shrinks the model from ~66 GB to ~22 GB.