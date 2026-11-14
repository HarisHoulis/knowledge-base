---
domain: ai-workflows
subdomain: agent-observability
concept: production-agent-failure-diagnosis
title: Google Open Sources AQuA to Diagnose Production AI Agent Failures
sources:
  - title: "Google Open Sources Ambient Quality Agent (AQuA) to Diagnose Production AI Agent Failures"
    url: "https://www.infoq.com/news/2026/11/google-ambient-agent-prod/"
    author: "Leela Kumili"
    date: "2026-11-13"
---

# Google Open Sources AQuA to Diagnose Production AI Agent Failures

Google has open-sourced AQuA (Ambient Quality Agent), a reference implementation for analyzing production AI agent sessions. It verifies recurring failure patterns and investigates root causes against snapshots of the deployed source, giving teams a way to trace agent misbehavior back to the code and prompts actually running in production (InfoQ, Leela Kumili).

The reported evaluation replayed 32 sessions. After prompt changes informed by AQuA's analysis, seat selection bypasses dropped from 15 sessions to two, and dietary preference omissions fell from seven to zero. These results illustrate the core value: turning observed production failures into targeted, verifiable fixes rather than guesswork.

- AQuA is an open-source reference implementation for analyzing production AI agent sessions and verifying recurring failure patterns.
- It investigates root causes against snapshots of the deployed source, tying failures to the actual production code and prompts.
- In a 32-session replay, seat selection bypasses fell from 15 sessions to two after prompt changes.
- Dietary preference omissions dropped from seven to zero in the same evaluation.