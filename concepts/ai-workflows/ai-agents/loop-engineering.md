---
domain: ai-workflows
subdomain: ai-agents
concept: loop-engineering
title: What is “loop engineering?”
sources:
  - title: "What is “loop engineering?”"
    url: "https://newsletter.pragmaticengineer.com/p/what-is-loop-engineering"
    author: "Gergely Orosz"
    date: "2026-07-14"
---

# What is “loop engineering?”

In “What is loop engineering?” (2026), Gergely Orosz explores the emerging practice of designing automated loops for AI coding agents, rather than writing individual prompts. The article traces the origin to Geoffrey Huntley's “Ralph Wiggum” technique, which uses a Bash loop to repeatedly prompt Claude Code until a project goal is achieved. This method gained popularity as a way to circumvent context-window limits by breaking large tasks into smaller, sequential agent runs with persistent state and compressed logs. Orosz notes that the approach requires senior engineering oversight, as agents still drift and need guidance.

Orosz describes how major AI harnesses (Codex, Hermes, Claude Code) began shipping “/goal” commands in mid-2026, formalizing the Ralph loop into a single durable objective that keeps the agent working across turns until a completion condition is met. Developer examples include cron-style scheduled jobs and event-triggered automations: opening PRs for Sentry issues, fixing flaky tests, triaging outages, and babysitting nightly e2e runs. However, some developers report disappointment due to agent drift and high token costs at API prices.

The article also questions whether loop engineering is a temporary hack while tooling catches up, and suggests that “context engineering” — understanding AI context windows and state management — might be more broadly valuable for developers than building custom loops. (Orosz, “What is loop engineering?”, 2026)

- Loop engineering is a shift from writing prompts to designing autonomous agent loops that work toward a goal.
- The technique originated from Geoffrey Huntley's 'Ralph Wiggum' Bash loop and gained traction as a workaround for context-window limits.
- Major AI coding harnesses now support native /goal commands that implement the loop pattern.
- Common real-world loops are event-triggered automations (e.g., triaging issues) and cron-style scheduled agent tasks (e.g., nightly test fixes).
- Some developers find issues with agent drift and cost; the article suggests context engineering may matter more for most devs.