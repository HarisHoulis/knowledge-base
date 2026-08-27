---
domain: system-design
subdomain: ai-hardware
concept: tpu
title: What is Google's TPU?
sources:
  - title: "EP222: What is Google’s TPU?"
    url: "https://blog.bytebytego.com/p/ep222-what-is-googles-tpu"
    author: "ByteByteGo"
    date: "2026-08-15"
---

# What is Google's TPU?

Google's TPU is a custom AI chip designed from scratch for the large matrix multiplications that modern ML models rely on, whereas GPUs were originally built for graphics (ByteByteGo, 2026). At Cloud Next '26, Google unveiled its 8th generation, which for the first time ships in two flavors: TPU 8t for training, where raw throughput wins, and TPU 8i for inference, where latency and chip-to-chip speed matter most. Both share the same Axion CPUs, liquid cooling, and software stack, so code written for one runs on the other.

The key distinction between the two variants reflects different workloads: training favors raw compute throughput, while inference prioritizes low latency and fast chip-to-chip communication. The article frames this as a study guide for understanding what is same and what is different between the TPU variants, helping engineers reason about AI hardware choices.

- TPUs are purpose-built for deep learning matrix math, unlike graphics-first GPUs.
- The 8th generation TPU splits into TPU 8t for training and TPU 8i for inference.
- Training and inference have different priorities: throughput vs. latency and chip-to-chip speed.
- Both TPU variants share Axion CPUs, liquid cooling, and a common software stack for portability.