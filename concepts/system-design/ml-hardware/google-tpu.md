---
domain: system-design
subdomain: ml-hardware
concept: google-tpu
title: What is Google's TPU?
sources:
  - title: "EP222: What is Google’s TPU?"
    url: "https://blog.bytebytego.com/p/ep222-what-is-googles-tpu"
    author: "ByteByteGo"
    date: "2026-08-15"
---

# What is Google's TPU?

Google's TPU is a custom AI chip designed specifically for the large matrix multiplications central to modern machine learning models. Unlike GPUs, which were originally built for graphics rendering, TPUs were purpose-built for deep learning workloads from the ground up (ByteByteGo, 2026).

- TPUs are custom Google AI chips optimized for matrix multiplications in deep learning.
- The 8th-generation TPU comes in two variants: TPU 8t for training and TPU 8i for inference.
- TPU 8t prioritizes raw throughput, while TPU 8i focuses on latency and chip-to-chip speed.
- Both variants share Axion CPUs, liquid cooling, and the same software stack, ensuring code portability.