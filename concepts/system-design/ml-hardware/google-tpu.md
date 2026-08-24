---
domain: system-design
subdomain: ml-hardware
concept: google-tpu
title: What is Google's TPU?
sources:
  - title: "EP222: What is Google's TPU?"
    url: "https://blog.bytebytego.com/p/ep222-what-is-googles-tpu"
    author: "ByteByteGo"
    date: "Sat, 15 Aug 2026 15:30:49 GMT"
---

# What is Google's TPU?

Google's TPU (Tensor Processing Unit) is a custom AI chip designed from the ground up for the giant matrix multiplications that modern machine learning models depend on. Unlike GPUs, which were originally built for graphics, TPUs were purpose-built for deep learning from day one (ByteByteGo, 2026).

- TPUs are custom AI accelerators built specifically for deep learning workloads, unlike GPUs which originated for graphics.
- The 8th-generation TPU comes in two flavors: TPU 8t for training and TPU 8i for inference.
- TPU 8t prioritizes raw throughput, while TPU 8i prioritizes latency and chip-to-chip speed.
- Both TPU variants share Axion CPUs, liquid cooling, and a common software stack for portability.