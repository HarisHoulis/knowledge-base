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

The article explains how large language models are trained to be helpful through three stages: pretraining, supervised fine-tuning (SFT), and preference learning. Pretraining gives the model broad language capability, SFT teaches it to follow instructions by imitation, but neither captures the trade-offs involved in answering questions that have multiple valid responses (ByteByteGo, 2026). Preference learning uses human comparisons—where a prompt is paired with a preferred and a rejected response—to encode these trade-offs directly, because humans are better at judging between two responses than writing an ideal one from scratch.

- RLHF trains a separate reward model from comparison data, then uses PPO reinforcement learning to optimize the policy, while keeping a frozen reference model to penalize drift.
- DPO folds the reward signal directly into a single training step, adjusting the model to increase the probability of preferred responses and decrease rejected ones, avoiding a separate reward model and RL loop.
- Both methods rely on human preferences as a proxy; over-optimizing against this proxy can lead to Goodhart's law effects, such as sycophancy and longer but not better answers.
- For tasks with checkable answers (e.g., math, code), verifiable rewards from a program can replace human-derived reward models, as demonstrated by DeepSeek's GRPO and R1 model.