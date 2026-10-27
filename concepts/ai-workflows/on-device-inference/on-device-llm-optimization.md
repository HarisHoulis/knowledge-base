---
domain: ai-workflows
subdomain: on-device-inference
concept: on-device-llm-optimization
title: How Apple Fits an LLM on Your iPhone
sources:
  - title: "How Apple Fits an LLM on Your iPhone"
    url: "https://blog.bytebytego.com/p/how-apple-fits-an-llm-on-your-iphone"
    author: "ByteByteGo"
    date: "2026-10-27"
---

# How Apple Fits an LLM on Your iPhone

Apple runs a 3-billion-parameter language model on-device by attacking both memory capacity and memory bandwidth. At 16-bit precision the weights alone would occupy roughly 6GB, leaving no room for the prompt, intermediate calculations, the OS, and other apps, so the engineering team compresses the weights and reduces the working memory needed during inference.

Storage is cut through quantization, specifically palettization: similar weight values are grouped and referenced via a small lookup table with short per-weight references. An earlier version mixed 2-bit and 4-bit representations (about 3.7 bits per weight, ~1.39GB for 3B weights), spending more bits on sensitive components. A later model uses 2-bit decoder weights and a 4-bit embedding table, enabled by quantization-aware training that simulates quantization restrictions during training.

For runtime memory, Apple optimizes the KV cache, which stores intermediate results so earlier tokens aren't recomputed. Cross-layer KV sharing splits the model into two blocks at a 5:3 depth ratio, with the second block reusing keys and values from the final layer of the first, cutting KV-cache memory by 37.5%. Feature specialization uses LoRA adapters: the base model's weights stay fixed while small rank-16 adapters (16-bit values, tens of MBs) are trained and swapped per feature, avoiding duplicated full models.

Hardware efficiency relies on choosing the right data layouts, splitting large arrays, and minimizing memory copies across the CPU, GPU, and Apple Neural Engine. Apple Intelligence decides per request whether to run on-device or route to Private Cloud Compute, where encrypted requests are decryptable only inside validated nodes, and the server model uses mixture-of-experts and parallel processing. The guiding principle is that model capability should follow the resources available at runtime.

- Palettization with mixed 2-bit/4-bit weights (~3.7 bits/weight) shrinks a 3B model to ~1.39GB; later models use 2-bit decoder weights and 4-bit embeddings via quantization-aware training.
- Cross-layer KV sharing (5:3 depth split) cuts KV-cache memory by 37.5% by having later layers reuse keys and values from an earlier layer.
- LoRA adapters (rank-16, tens of MBs) let multiple features share one base model instead of duplicating it.
- Efficient hardware use requires correct data layouts, array splitting, and minimal memory copies across CPU, GPU, and ANE.
- Apple Intelligence routes simple tasks on-device and complex ones to Private Cloud Compute, where requests are encrypted for validated nodes only.