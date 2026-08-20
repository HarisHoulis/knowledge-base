---
domain: ai-workflows
subdomain: agentic-loops
concept: loop-engineering
title: What is “loop engineering?”
sources:
  - title: "What is “loop engineering?”"
    url: "https://newsletter.pragmaticengineer.com/p/what-is-loop-engineering"
    author: "Gergely Orosz"
    date: "2026-07-14"
---

# What is “loop engineering?”

Loop engineering is an emerging approach in AI-assisted software development where engineers design autonomous loops for AI agents instead of writing individual prompts. The term gained traction after Boris Cherny of Anthropic stated, “I don’t prompt Claude anymore... My job is to write loops,” and Peter Steinberger of OpenClaw similarly advocated loop design. Addy Osmani summarized it as “replacing yourself as the person who prompts the agent” by designing the system that does it instead (Orosz, 2026).

- Loop engineering shifts developers from prompting agents to designing autonomous agent loops, often using a goal or trigger.
- The technique originated as the “Ralph Wiggum” loop, a Bash loop that repeatedly runs an agent against a prompt until a goal is achieved.
- Major coding harnesses like Codex, Claude Code, and Hermes now ship a /goal command that formalizes the loop as a single durable objective.
- Common practical uses include responding to events (triggers) and running scheduled cron-style workflows, such as fixing flaky tests, triaging issues, and opening PRs automatically.
- Adoption is not universal: some developers report agent drift, high token costs, and better outcomes with human-in-the-loop, while others see looping as a temporary hack until tooling matures.