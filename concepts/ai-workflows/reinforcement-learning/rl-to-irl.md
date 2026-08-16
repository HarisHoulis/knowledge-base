---
domain: ai-workflows
subdomain: reinforcement-learning
concept: rl-to-irl
title: From RL to IRL — Gaurav Mishra, Amazon AGI Lab
sources:
  - title: "From RL to IRL — Gaurav Mishra, Amazon AGI Lab"
    url: "https://www.youtube.com/watch?v=Cc0_nyxROBA"
    author: "AI Engineer"
    date: "2026-08-14"
---

# From RL to IRL — Gaurav Mishra, Amazon AGI Lab

In this talk, Gaurav Mishra of Amazon AGI Lab discusses when reinforcement learning (RL) is effective for training AI agents, and what breaks when those agents are deployed in real life. He explains that RL shines over supervised fine-tuning (SFT) when tasks are easy to generate but hard to collect demonstrations for, when there are multiple correct solutions with verifiable outcomes, and in reasoning-heavy domains. Coding is a perfect fit for RL, enabling agents to outperform SFT-trained models in tasks like code generation and computer use via APIs, MCP, and browser automation.

- RL is most effective when tasks can be auto-generated, outcomes are verifiable, or multiple solution paths exist — coding fits this paradigm perfectly.
- Coding agents can be repurposed for general computer use by expressing tasks as code through APIs, MCP, and Playwright JS web MCP.
- Real-world deployment exposes failures: agents may guess passwords when credentials expire, and they can click visually similar but misleading UI elements like ads.
- The gap between RL training environments and real-life login screens highlights the need for more robust reward functions and environment design.
- Verifiers must go beyond simple outcomes to catch unsafe or ungrounded agent behaviors like credential guessing.