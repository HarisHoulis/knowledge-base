---
domain: ai-workflows
subdomain: gpu-security
concept: gpu-side-channel-leakage
title: Your GPU Neighbor Can Hear Your Model: Timing Side-Channels in Shared GPU Tenancy
sources:
  - title: "Your GPU Neighbor Can Hear Your Model — Branislav Brzak, Stealthium"
    url: "https://www.youtube.com/watch?v=SacJfmp33vM"
    author: "AI Engineer"
    date: "2026-10-12"
---

# Your GPU Neighbor Can Hear Your Model: Timing Side-Channels in Shared GPU Tenancy

Branislav Brzak, a cybersecurity researcher at Stealthium, describes how an attacker sharing a GPU with a victim's LLM can learn sensitive operational details about that model purely by observing time. The attacker needs no root access and no traditional exploits; the only action is measuring the operating time of GPU parts that remain common to tenants. From this side channel, the attacker can determine what model is running, how quickly it responds, and what type of work it is currently doing, without touching the victim's data.

The attack exploits the fact that GPU isolation via Multi-Instance GPU (MIG) is incomplete. MIG gives each segment its own physical compute units, dedicated VRAM, split L2 cache, and isolated bandwidth quotas, so there is no displacement between instances. However, memory barriers (membars) operate at the GPU-wide level: a single instance barrier still affects every L2 partition on the card. Time is the only thing not isolated, so when one tenant is busy, others run slightly slower. The attacker only reads his own memory and measures the time of his own reads, repeating every 5 microseconds; the median latency difference is only about 3 microseconds, but that is enough.

Using this primitive, the researchers achieved 97% accuracy in determining model architecture and depth, and 99.3% accuracy in determining decoding speed. They can also infer load periods, number of tokens, and response length, and distinguish work types such as code, creativity, prose, JSON, or search. They cannot recover the prompts, answers, or content itself—only execution time. The work was validated on real H100s serving real LLMs, with the victim running a Quant 3 8B model on a segment with three compute units and 48 GB VRAM while the attacker used one compute unit and 10 GB VRAM. The timing trace shows a fundamental frequency of 881 Hz corresponding to tokens per second, with harmonics and per-token peaks reflecting layer challenges and inter-layer processing.

- An attacker sharing a MIG-isolated GPU can infer model architecture (97% accuracy), decoding speed (99.3% accuracy), load periods, token counts, and response length purely from timing, without root access or exploits.
- The leak stems from GPU-wide memory barriers that affect every L2 partition, making time the only non-isolated resource; the median latency difference is only ~3 microseconds.
- The attacker only reads and times his own memory, repeating every 5 microseconds, so no victim data is ever touched.
- Prompts, answers, and content remain unrecoverable; only execution-time metadata leaks.
- The primitive builds on prior work ('Behind Bars', USENIX Security) and was demonstrated on real H100s serving real LLMs.