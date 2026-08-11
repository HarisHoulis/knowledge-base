---
domain: ai-workflows
subdomain: loop-engineering
concept: loop-engineering
title: What is Loop Engineering?
sources:
  - title: "What is “loop engineering?”"
    url: "https://newsletter.pragmaticengineer.com/p/what-is-loop-engineering"
    author: "Gergely Orosz"
    date: "2026-07-14"
---

# What is Loop Engineering?

Loop engineering is an emerging practice where developers design and run agent loops instead of writing individual prompts. The term gained traction after Boris Cherny of Anthropic stated, 'I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do. My job is to write loops.' Addy Osmani similarly described it as 'replacing yourself as the person who prompts the agent. You design the system that does it instead' (Orosz, 2026). The approach builds on the 'Ralph loop,' a technique named after a Simpsons character, where a Bash loop repeatedly feeds an agent a prompt until a goal is achieved. Geoffrey Huntley, who popularized Ralph loops, noted that senior engineering expertise is still required: 'There is no way this is possible without senior expertise guiding Ralph' (Orosz, 2026).

- Loop engineering replaces one-off prompting with designing persistent agent loops that work toward a goal.
- The 'Ralph loop' — a Bash loop restarting an agent with a fresh context window — is the conceptual origin, driven by context-window limitations.
- By mid-2026, major coding harnesses (Codex, Claude Code, Hermes) shipped /goal and /loop commands that automate the loop, making the technique a primitive.
- Common developer use cases include triggers and cron jobs: opening PRs for new issues, fixing flaky tests, triaging outages, and running nightly end-to-end tests.
- Critics point to high token costs, agent drift, and the possibility that looping was a temporary hack until tooling caught up.