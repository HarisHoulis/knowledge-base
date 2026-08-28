---
domain: ai-workflows
subdomain: ai-coding-agents
concept: loop-engineering
title: What is “loop engineering?”
sources:
  - title: "What is “loop engineering?”"
    url: "https://newsletter.pragmaticengineer.com/p/what-is-loop-engineering"
    author: "Gergely Orosz"
    date: "2026-07-14"
---

# What is “loop engineering?”

Loop engineering is an emerging approach where engineers design systems that prompt AI agents repeatedly instead of writing individual prompts. The concept gained traction after Anthropic's Boris Cherny said his job is “to write loops,” and Peter Steinberger and Addy Osmani echoed similar ideas. The technique traces back to Geoffrey Huntley's “Ralph Wiggum” method, which uses a Bash loop to continuously feed a prompt file to Claude Code, nudging the agent toward a goal (Orosz, 2026).

- Loop engineering replaces manual prompting with systems that keep agents working toward defined goals.
- The Ralph loop, a Bash while-loop around an agent, inspired the /goal command now built into major AI coding harnesses.
- Common practical loops include event-triggered automations and cron-like scheduled jobs, such as triaging issues, opening PRs for flaky tests, and babysitting nightly test runs.
- Some developers remain skeptical due to agent drift, high token costs, and the possibility that loops are a temporary workaround while tooling matures.