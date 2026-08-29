---
domain: ai-workflows
subdomain: agent-robotics
concept: agent-hardware-tool
title: Tell the Robot What You Want — Sandhya Subramani, AWS
sources:
  - title: "Tell the Robot What You Want — Sandhya Subramani, AWS"
    url: "https://www.youtube.com/watch?v=S6aSoQ6_u5A"
    author: "AI Engineer"
    date: "2026-08-29T18:30:17+00:00"
---

# Tell the Robot What You Want — Sandhya Subramani, AWS

Sandhya Subramani demonstrates Scout, a Raspberry Pi-based quadruped robot connected via 4G, which can answer unplanned questions like counting people using a front camera—without being explicitly trained for that task. The robot's capabilities emerge from an agent layer placed above its existing movement policies, allowing it to reason about its environment and select appropriate presets (Subramani, 2026). The core idea is that agents can be given hardware tools just like software tools, enabling plain-language control of robots trained for fixed task lists. This is implemented in about five lines using an open-source AWS framework that supports roughly 40 robot models. Scout runs three agents simultaneously—one for environmental awareness, one for Telegram messaging, and a voice agent disabled to avoid on-stage interruptions. Subramani's framing is that the agent decides what to do while the trained policy decides how, and the robot also serves as a data collection rig for future training (Subramani, 2026).

- An agent layer above trained policies lets users control robots with natural language, even for tasks never explicitly trained.
- Hardware tools can be exposed to agents as software tools, enabling selection among preset policies.
- Scout runs three concurrent agents (environment, Telegram, voice) on a Raspberry Pi with 4G connectivity.
- The AWS framework integrates with 40+ robots, requiring only a few lines of code to connect an agent to a robot.
- The robot doubles as a data collection platform, feeding future model training.