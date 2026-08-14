---
domain: ai-workflows
subdomain: llm-alignment
concept: rlhf-vs-dpo
title: How LLMs Learn to Be Helpful: RLHF vs DPO
sources:
  - title: "How LLMs Learn to Be Helpful (RLHF vs DPO)"
    url: "https://blog.bytebytego.com/p/how-llms-learn-to-be-helpful-rlhf"
    author: "ByteByteGo"
    date: "Tue, 14 Jul 2026 15:30:53 GMT"
---

# How LLMs Learn to Be Helpful: RLHF vs DPO

Language models are built in three stages: pretraining, supervised fine-tuning (SFT), and preference learning. SFT teaches instruction-following through imitation, but this fails when a prompt has many valid answers with trade-offs. Comparison data - where humans judge which of two responses is better - captures those trade-offs and forms the basis for preference learning. As ByteByteGo (2026) notes, this alignment stage can matter more than model size: a 1.3B parameter aligned model was preferred over the 175B GPT-3.

- Pretraining gives raw capability, SFT enables instruction following, and preference learning teaches trade-offs between multiple good answers.
- RLHF trains a separate reward model and uses PPO to optimize the policy, with a KL penalty to prevent degenerate text; it is powerful but expensive and complex.
- DPO folds the reward signal into a single supervised training step, making alignment simpler and more accessible; Zephyr 7B trained with DPO beat Llama 2 Chat 70B.
- Both RLHF and DPO rely on human preference as a proxy signal, which can lead to sycophancy and quality degradation when optimized too hard (Goodhart's law).
- For tasks with checkable answers, verifiable rewards (e.g., math/unit tests) replace human preference signals, as seen in DeepSeek's GRPO and R1, while subjective qualities still require preference learning.