---
domain: ai-workflows
subdomain: continual-learning
concept: scaling-continual-learning
title: Scaling up Continual Learning — Ronak Malde, Trajectory
sources:
  - title: "Scaling up Continual Learning — Ronak Malde, Trajectory"
    url: "https://www.youtube.com/watch?v=zL1kLftVTlo"
    author: "AI Engineer"
    date: "2026-08-12T14:30:11+00:00"
---

# Scaling up Continual Learning — Ronak Malde, Trajectory

Ronak Malde, founder of Trajectory, argues that the AI field is hitting a wall with benchmark-driven scaling. While benchmarks are saturating rapidly, they are becoming more expensive and time-consuming, taking hours or days to evaluate. Meanwhile, real-world inference generates hundreds of trillions of tokens daily, producing rich signal about model failures and successes that remains largely untapped. He advocates for continual learning as the next unlock, where models continuously update from real-world interactions, mirroring human learning.

Malde identifies several problems with current algorithms. First, there is a task distribution mismatch: benchmarks often don't reflect real-world use cases. Second, many methods are not truly on-policy, deviating from online deployment conditions. Third, the current paradigm requires massive infrastructure to replicate environments, adding bias. Finally, rewards are compressed into a single scalar, losing the messy, noisy, per-token signal available in real-world data.

He traces the evolution of training paradigms: SFT solved parallelism but was off-policy with static task distributions; DPO/RLHF brought online task distributions but introduced pairs and sequence-level rewards, losing infrastructure ease; GRPO (current) maximizes on-policy rollouts, enabling powerful models with less catastrophic forgetting, but still relies on off-policy task distributions and has significant parallelism challenges. The path forward, he suggests, is to leverage real-world inference data for continual learning, moving beyond benchmark saturation.

- Benchmark scaling is becoming unsustainable: more time-consuming, expensive, and disconnected from real-world AI usage.
- Real-world inference generates massive data (hundreds of trillions of tokens per day) that should be harnessed for training via continual learning.
- Current algorithms suffer from task distribution mismatch, off-policy sampling, heavy infrastructure demands, and compression of rewards into a single scalar.
- The evolution from SFT to DPO/RLHF to GRPO shows trade-offs: on-policy sampling improved but parallelism and task distribution remain problematic.
- Continual learning is positioned as the next major unlock, enabling models to update continuously from real-world signals.