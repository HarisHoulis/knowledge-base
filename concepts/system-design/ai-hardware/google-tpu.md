---
domain: system-design
subdomain: ai-hardware
concept: google-tpu
title: What is Google's TPU?
sources:
  - title: "EP222: What is Google’s TPU?"
    url: "https://blog.bytebytego.com/p/ep222-what-is-googles-tpu"
    author: "ByteByteGo"
    date: "Sat, 15 Aug 2026 15:30:49 GMT"
---

# What is Google's TPU?

According to ByteByteGo's article [1], a TPU is Google's custom AI chip, designed from scratch for the giant matrix multiplications central to modern models. Unlike GPUs, which were built for graphics first, TPUs were purpose-built for deep learning from day one. At Cloud Next '26, Google unveiled its 8th-generation TPU in two flavors: TPU 8t for training and TPU 8i for inference.

TPU 8t is optimized for raw throughput, while TPU 8i is optimized for latency and chip-to-chip speed. Despite these different focuses, both variants share the same Axion CPUs, liquid cooling, and software stack, so code written for one runs on the other. The article characterizes this as a study guide based on published Google materials [1].

- TPUs are custom AI accelerators designed specifically for deep learning, while GPUs were originally built for graphics.
- The 8th-generation TPU comes in two variants: TPU 8t for training and TPU 8i for inference.
- TPU 8t emphasizes raw throughput; TPU 8i emphasizes latency and chip-to-chip speed.
- Both variants share Axion CPUs, liquid cooling, and the same software stack, ensuring code portability.