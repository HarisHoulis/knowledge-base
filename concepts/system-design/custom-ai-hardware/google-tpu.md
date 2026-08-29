---
domain: system-design
subdomain: custom-ai-hardware
concept: google-tpu
title: What is Google's TPU?
sources:
  - title: "EP222: What is Google’s TPU?"
    url: "https://blog.bytebytego.com/p/ep222-what-is-googles-tpu"
    author: "ByteByteGo"
    date: "2026-08-15"
---

# What is Google's TPU?

Google's TPU is a custom AI accelerator designed from scratch for the giant matrix multiplications that modern deep learning models depend on. Unlike GPUs, which were originally built for graphics rendering, TPUs are purpose-built for deep learning workloads (ByteByteGo, 2026). At Cloud Next '26, Google unveiled its 8th generation of TPUs, which for the first time comes in two distinct variants: the TPU 8t for training and the TPU 8i for inference. The 8t is optimized for raw throughput, while the 8i is optimized for latency and chip-to-chip speed (ByteByteGo, 2026).

Both variants share the same Axion CPUs, liquid cooling, and software stack, so code written for one runs on the other. This shared foundation highlights that the key difference lies in the hardware trade-offs for different phases of the ML lifecycle—training demands maximum compute throughput, whereas inference prioritizes fast, efficient response times (ByteByteGo, 2026).

- TPU is Google's custom AI chip built specifically for large-scale matrix multiplications in deep learning.
- The 8th generation TPU comes in two flavors: TPU 8t for training and TPU 8i for inference.
- TPU 8t focuses on raw throughput; TPU 8i focuses on latency and chip-to-chip speed.
- Both versions share the same Axion CPUs, liquid cooling, and software stack for portability.