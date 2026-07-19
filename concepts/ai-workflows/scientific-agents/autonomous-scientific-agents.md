---
domain: ai-workflows
subdomain: scientific-agents
concept: autonomous-scientific-agents
title: Autonomous Agents for Scientific Tasks
sources:
  - title: "Autonomous Agents for Scientific Tasks - Sina Shahandeh, Radicait"
    url: "https://www.youtube.com/watch?v=XLEYtv3cMlw"
    author: "AI Engineer"
    date: "2026-07-18T23:30:06+00:00"
---

# Autonomous Agents for Scientific Tasks

Sina Shahandeh discusses the limitations of current AI coding agents in open-ended scientific tasks, where they often saturate in performance because they lack the ability to generate novel hypotheses—what he calls 'research taste' (Shahandeh, 2026). While agents are proficient at implementing code and running experiments, they struggle to come up with creative ideas for improvement, unlike top human researchers who continuously produce better hypotheses. The talk uses the example of training a GAN to generate PET scans from CT scans for cancer detection, highlighting the need for agents to decompose long-term research into iterative hypothesis-testing loops (Shahandeh, 2026). The core challenge is enabling agents to generate good hypotheses autonomously, rather than just executing predefined optimization steps.

- Coding agents excel at implementation but plateau in open-ended scientific tasks due to lack of hypothesis generation.
- Human researchers outperform agents by continuously producing novel, effective ideas (research taste).
- Scientific tasks require iterative loops of observation, hypothesis, experiment, and learning, not just hill-climbing optimization.
- Example: training a CT-to-PET translation model shows that agents need better mechanisms for idea generation, not just data and code execution.