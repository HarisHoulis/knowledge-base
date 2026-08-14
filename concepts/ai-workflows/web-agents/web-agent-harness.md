---
domain: ai-workflows
subdomain: web-agents
concept: web-agent-harness
title: Bringing agents onto the world wide web
sources:
  - title: "Bringing agents onto the world wide web — Paul Klein IV, Browserbase"
    url: "https://www.youtube.com/watch?v=GqoNrUz8hEU"
    author: "AI Engineer"
    date: "2026-08-14T15:00:31+00:00"
---

# Bringing agents onto the world wide web

In this talk, Paul Klein IV of Browserbase examines why web agents and computer-use tools have underdelivered despite rapid model improvements. He argues that the web was built for humans, not agents, leading to persistent issues like dynamic page structures, high token consumption, broken browser sessions, and anti-bot blockers. These infrastructural problems remain a major barrier for automation, even as models have become more capable (Paul Klein IV, 2026).

Klein contends that models are no longer the primary bottleneck. Recent advances in long-context handling and computer use, driven by reinforcement learning on human trajectories, have created a 'capabilities overhang'—models can do far more than current systems let them. The missing piece is the agent harness: the scaffolding, tools, and environments surrounding the LLM that enable it to reliably act on the web. He emphasizes that investing in harness engineering can unlock model potential, much as it has for coding agents (Paul Klein IV, 2026).

He cites Karpathy's November 2023 tweet describing an LLM as the kernel of a growing system, with peripherals like a code interpreter, browser, and subagents. This vision has since become a practical roadmap. For web agents to succeed, developers must build robust browser harnesses that handle page dynamics, context efficiency, and interaction reliability. The talk concludes by framing harness development as the key opportunity for the AI engineering community (Paul Klein IV, 2026).

- The web's human-centric design makes agent automation difficult due to dynamic pages, high token counts, and blockers.
- Model capabilities have advanced significantly, but agents still lack the right harness and tools to translate those capabilities into real-world actions.
- Investing in harness engineering can extract more performance from existing models, as demonstrated in coding use cases.
- Karpathy's concept of the LLM as a kernel with peripherals (code interpreter, browser, subagents) is a guiding framework for building web agents.
- Building browser-specific harnesses is a high-leverage opportunity for developers to push web agents forward.