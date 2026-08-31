---
domain: system-design
subdomain: hardware-acceleration
concept: google-tpu
title: What is Google's TPU?
sources:
  - title: "EP222: What is Google’s TPU?"
    url: "https://blog.bytebytego.com/p/ep222-what-is-googles-tpu"
    author: "ByteByteGo"
    date: "Sat, 15 Aug 2026 15:30:49 GMT"
---

# What is Google's TPU?

According to ByteByteGo (2026), Google's TPU is a custom AI accelerator designed from scratch for the large matrix multiplications that modern machine learning models rely on. Unlike GPUs, which were originally built for graphics, TPUs were built specifically for deep learning from day one. At Cloud Next '26, Google announced its 8th-generation TPU, which for the first time ships in two flavors: TPU 8t for training workloads where raw throughput is the priority, and TPU 8i for inference workloads where latency and chip-to-chip speed matter most.

- TPUs are custom AI chips built specifically for the matrix multiplications underlying modern deep learning models, unlike GPUs which were originally designed for graphics.
- Google's 8th-generation TPU comes in two variants: TPU 8t for training (optimized for raw throughput) and TPU 8i for inference (optimized for latency and chip-to-chip speed).
- Both TPU variants share the same Axion CPUs, liquid cooling, and software stack, allowing code written for one to run on the other.
- The article serves as a study guide for understanding the similarities and differences between the two TPU variants based on published Google articles.