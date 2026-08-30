---
domain: ai-workflows
subdomain: embodied-agents
concept: hardware-tool-agent
title: Tell the Robot What You Want — Sandhya Subramani, AWS
sources:
  - title: "Tell the Robot What You Want — Sandhya Subramani, AWS"
    url: "https://www.youtube.com/watch?v=S6aSoQ6_u5A"
    author: "AI Engineer"
    date: "2026-08-29T18:30:17+00:00"
---

# Tell the Robot What You Want — Sandhya Subramani, AWS

Sandhya Subramani demonstrates a four-legged robot named Scout that answers a question it was never explicitly trained for: counting people in view. Scout runs on a Raspberry Pi connected via 4G, and its behavior is driven by an agent layer sitting above existing movement policies, allowing natural-language commands to select among prebuilt robot behaviors (Subramani, 2026). The underlying pattern is to treat hardware as another tool an agent can invoke; the agent decides what to do, while the trained policy decides how to execute it. This setup is wired in about five lines using an open-source AWS framework that supports roughly 40 robot platforms (Subramani, 2026). Scout runs three agents simultaneously—one reasoning about the environment, one communicating over Telegram, and a voice agent disabled during the talk—and also serves as a platform for collecting future training data (Subramani, 2026).

- An agent layer can extend natural-language control to existing robot policies without retraining the underlying model.
- Giving an LLM agent a hardware tool lets it choose among preset movement policies, enabling novel requests.
- The AWS open-source framework integrates with dozens of robots using minimal code.
- Running multiple specialized agents (environment, chat, voice) on one robot is practical and modular.
- The robot doubles as a data-collection rig for scaling embodied AI policies.