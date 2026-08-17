---
domain: ai-workflows
subdomain: browser-agents
concept: agent-harness
title: Bringing agents onto the world wide web — Paul Klein IV, Browserbase
sources:
  - title: "Bringing agents onto the world wide web — Paul Klein IV, Browserbase"
    url: "https://www.youtube.com/watch?v=GqoNrUz8hEU"
    author: "AI Engineer"
    date: "2026-08-14T15:00:31+00:00"
---

# Bringing agents onto the world wide web — Paul Klein IV, Browserbase

The talk examines why AI agents still struggle to interact with the web despite rapid model improvements. Klein argues that the web was designed for humans, not agents, leading to frequent page changes, token-heavy contexts, and fragile browser states. He reflects on his earlier career maintaining web automation scripts, noting that while agents have improved, they remain far from reliable for real-world tasks.

Klein identifies the core bottleneck as no longer model capability but the absence of the right harness and tools. He highlights that models have progressed significantly thanks to reinforcement learning from computer-use environments, yet agent performance lags because the surrounding scaffolding—browser control, subagents, and multimodal input—is underdeveloped. Investing in harness engineering can unlock more capability from existing models, echoing Karpathy's 2023 prediction about LLM systems comprising code interpreters, browsers, and other LLMs as subagents.

- The web is inherently human-focused, creating challenges like page instability and high token usage for automated agents.
- Model quality has improved enough that it is no longer the primary barrier; the missing piece is the agent harness.
- A well-designed harness (browser, tools, subagents) can extract significantly more utility from modern LLMs.
- Karpathy's 2023 framework for LLM systems remains a useful blueprint for agent development.