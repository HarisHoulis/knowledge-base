---
domain: ai-workflows
subdomain: agent-hardware-integration
concept: agent-hardware-tools
title: Tell the Robot What You Want
sources:
  - title: "Tell the Robot What You Want — Sandhya Subramani, AWS"
    url: "https://www.youtube.com/watch?v=S6aSoQ6_u5A"
    author: "AI Engineer"
    date: "2026-08-29T18:30:17+00:00"
---

# Tell the Robot What You Want

Sandhya Subramani demonstrates Scout, a Raspberry Pi-based robot that answers open-ended questions like how many people it sees, despite never being explicitly trained for such tasks. The robot uses a 4G connection and an agent layer that acts as an intermediary between natural language commands and pre-existing movement policies. This approach effectively turns a fixed-task robot into a flexible system that can be addressed in plain language (Subramani, 2026).

The core idea is to give software agents 'tools' that map to hardware capabilities. By extending this concept, an agent can decide which preset policy to invoke, while the policy handles the low-level execution. Subramani wires this up using an open-source AWS framework supporting around 40 robots, with Scout running three agents simultaneously—one for environmental awareness, one for Telegram communication, and a voice agent that was disabled to avoid stage interruptions. This separation of concerns lets the agent focus on 'what to do' while the trained policy determines 'how' (Subramani, 2026).

The architecture also positions robots as data collection platforms. Because the agent can orchestrate diverse behaviors, it enables the gathering of new training data for future iterations. Subramani suggests that if policies scale like language models, robot capabilities could grow dramatically, leading to more generalizable and adaptable robotic systems (Subramani, 2026).

- Agents can control robots via software tools, enabling natural language commands without retraining.
- An open-source AWS framework supports many robots, requiring only about five lines of code to integrate.
- Multiple agents can run concurrently for different functions (e.g., environment monitoring, messaging, voice).
- The design separates high-level decision-making (agent) from low-level execution (policy).
- Robots become platforms for collecting diverse training data, scaling like large language models.