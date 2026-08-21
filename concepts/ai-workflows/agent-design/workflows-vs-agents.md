---
domain: ai-workflows
subdomain: agent-design
concept: workflows-vs-agents
title: How I automate my own job at Hugging Face using agents
sources:
  - title: "How I automate my own job at Hugging Face using agents — Niels Rogge, Hugging Face"
    url: "https://www.youtube.com/watch?v=FLUoowDJg4I"
    author: "AI Engineer"
    date: "2026-08-20T15:30:35+00:00"
---

# How I automate my own job at Hugging Face using agents

Niels Rogge describes automating his role at Hugging Face, where he contacts researchers to move model weights from Google Drive/Dropbox to the Hugging Face Hub. He first built a deterministic workflow that mirrors his manual outreach process, running nightly via cron and GitHub Actions, with tracing for prompt, cost, and latency. He deliberately avoided an agent framework because the guidance at the time was to prefer workflows unless an agent is necessary (AI Engineer, 2026).

- Outreach was automated as a deterministic workflow, not an agent, to match the manual path and keep cost/latency traceable.
- Follow-up was later rebuilt as a fully autonomous agent loop using bash as the main tool.
- Each issue gets its own container, allowing parallel execution and isolation.
- Recipients are not told an agent wrote to them because disclosed bots tend to get closed unread, and the messages match what Rogge would send himself.