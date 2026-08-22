---
domain: ai-workflows
subdomain: agent-runtime-design
concept: minimal-agent-runtime
title: Agent Frameworks Considered Harmful — Rémi Louf
sources:
  - title: "Agent Frameworks Considered Harmful — Rémi Louf, .txt"
    url: "https://www.youtube.com/watch?v=KHudyx5wW3U"
    author: "AI Engineer"
    date: "2026-08-22T16:30:39+00:00"
---

# Agent Frameworks Considered Harmful — Rémi Louf

In this talk, Rémi Louf, CEO of txt (a 15-person company), recounts his two-week deep dive into building agentic workflows after noticing a step-function improvement in agent capabilities around Opus 4.6. He was motivated by a personal itch: he wanted his morning briefing to be fully automated while he walked, without needing to stay attached to a terminal or constantly steer an agent via a phone. He describes existing tools like TUIs and vibe-based SSH as transitional—they still require human oversight and remote control, which is absurd for routine tasks.

Louf argues that agent frameworks, despite their popularity, are not the best primitive for building autonomous workflows. Instead, he found it far easier to implement agents without code by using YAML files to define prompts and agent behavior. This approach allowed him to version, diff, and review changes in pull requests, and to simply drop a file into a folder where the runtime would pick it up and run it. He also emphasizes the value of using existing scheduling primitives like cron jobs to trigger agents at specific times, such as his market watch every morning while he walks. The resulting system is intentionally minimal and 'dumb,' but it works.

- Frameworks were not helpful; the author spent more time editing prompts in code than building actual logic.
- Using YAML files to define agents enables easy versioning, diffing, and PR review—without writing code.
- A minimal runtime that loads agent definitions from files can make new agents 'magically' appear and run.
- Cron jobs and schedules are sufficient primitives for triggering agents at specific times, such as a morning market watch.
- The goal is to move beyond transitional tools (like TUI and vibe-SSH) to fully autonomous agents that run while you walk.