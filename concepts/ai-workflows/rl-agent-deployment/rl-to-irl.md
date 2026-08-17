---
domain: ai-workflows
subdomain: rl-agent-deployment
concept: rl-to-irl
title: From RL to IRL — Gaurav Mishra, Amazon AGI Lab
sources:
  - title: "From RL to IRL — Gaurav Mishra, Amazon AGI Lab"
    url: "https://www.youtube.com/watch?v=Cc0_nyxROBA"
    author: "AI Engineer"
    date: "2026-08-14T16:00:06+00:00"
---

# From RL to IRL — Gaurav Mishra, Amazon AGI Lab

In this talk, Gaurav Mishra of the Amazon AGI Lab examines why reinforcement learning (RL) agents that perform well in training often fail when deployed in real-world environments. He begins with a lightning review of RL: the agent (policy) samples generations, a reward is computed on the entire generation (unlike token-level loss in SFT), and algorithms like PPO and GRPO update the weights. RL becomes the preferred method when tasks are easy to generate but difficult to demonstrate, when multiple correct solutions exist and outcomes are verifiable, and in reasoning-heavy domains where only the outcome is judged. Coding is a perfect fit, which is why RL-trained coding agents have become highly capable.

- RL differs from SFT by computing a reward over the whole generation rather than per-token prediction loss, enabling learning from outcome-based signals.
- RL is most effective when tasks are easy to generate but hard to demonstrate, have multiple valid solutions with verifiable outcomes, or require heavy reasoning.
- A full RL system has three components: task, environment, and verifier—the verifier can range from string equality or unit tests to LLM-based judges with rubrics.
- Coding agents generalize to everyday computer use because emails, chats, and web browsing can be reduced to code via MCP/API calls and browser automation.
- Real-world deployment breaks RL agents: they may hallucinate passwords on login screens, click misleading ads that resemble submit buttons, and fail to recover from unexpected states—revealing gaps between reward optimization and practical safety.