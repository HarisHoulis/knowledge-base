---
domain: system-design
subdomain: ai-hardware
concept: google-tpu
title: What is Google’s TPU?
sources:
  - title: "EP222: What is Google’s TPU?"
    url: "https://blog.bytebytego.com/p/ep222-what-is-googles-tpu"
    author: "ByteByteGo"
    date: "2026-08-15"
---

# What is Google’s TPU?

Google’s TPU (Tensor Processing Unit) is a custom AI chip designed specifically for the large-scale matrix multiplications that modern deep learning models rely on. Unlike GPUs, which were originally built for graphics, TPUs were built for deep learning from the start. At Cloud Next ’26, Google unveiled the 8th generation of TPUs in two flavors: TPU 8t for training, where raw throughput is key, and TPU 8i for inference, where latency and chip-to-chip speed are prioritized. Both variants share the same Axion CPUs, liquid cooling, and software stack, so code written for one runs on the other. This design allows flexibility across training and deployment workloads while maintaining a unified development environment.

- TPUs are Google’s custom AI accelerators, designed from scratch for deep learning matrix operations.
- GPUs were built for graphics first, while TPUs were purpose-built for deep learning.
- The 8th generation ships as TPU 8t (training-optimized) and TPU 8i (inference-optimized).
- Both TPU variants share Axion CPUs, liquid cooling, and the same software stack for code portability.