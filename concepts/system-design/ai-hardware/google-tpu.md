---
domain: system-design
subdomain: ai-hardware
concept: google-tpu
title: What is Google's TPU?
sources:
  - title: "EP222: What is Google’s TPU?"
    url: "https://blog.bytebytego.com/p/ep222-what-is-googles-tpu"
    author: "ByteByteGo"
    date: "2026-08-15"
---

# What is Google's TPU?

Google's Tensor Processing Unit (TPU) is a custom AI chip built specifically for the large matrix multiplications that modern machine learning models rely on. Unlike GPUs, which were designed for graphics first, TPUs were designed for deep learning from day one. At Cloud Next '26, Google unveiled its 8th generation TPU in two variants: TPU 8t for training, prioritizing raw throughput, and TPU 8i for inference, prioritizing latency and chip-to-chip speed. Both share the same Axion CPUs, liquid cooling, and software stack, allowing code written for one to run on the other [1].

The article presents a diagram to illustrate the similarities and differences between the two TPU variants, based on published Google articles. This highlights a key system design principle: specialized hardware can be optimized for specific workloads, and maintaining a common software stack enables portability across variants. TPUs are a major component of Google's AI infrastructure, and understanding their architecture helps in designing large-scale AI systems [1].

- TPUs are Google's custom AI chips designed from the ground up for deep learning and matrix multiplications.
- The 8th generation TPU comes in two variants: TPU 8t for training (throughput-optimized) and TPU 8i for inference (latency-optimized).
- Both TPU variants share Axion CPUs, liquid cooling, and a common software stack, enabling code portability.
- TPU architecture choices reflect trade-offs between raw compute throughput and low-latency inference.