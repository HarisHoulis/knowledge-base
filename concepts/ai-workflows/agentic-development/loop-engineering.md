---
domain: ai-workflows
subdomain: agentic-development
concept: loop-engineering
title: What is “loop engineering?”
sources:
  - title: "What is “loop engineering?”"
    url: "https://newsletter.pragmaticengineer.com/p/what-is-loop-engineering"
    author: "Gergely Orosz"
    date: "2026-07-14"
---

# What is “loop engineering?”

Loop engineering is a trending approach in AI-assisted development where engineers no longer write individual prompts but design loops that repeatedly prompt agents to achieve a goal. The term gained traction after Anthropic’s Boris Cherny said he writes loops rather than prompts, and Peter Steinberger and Addy Osmani popularized the concept. The article traces the origin to Geoffrey Huntley’s “Ralph Wiggum” technique, a Bash loop that runs Claude Code repeatedly against a prompt file, allowing an agent to iterate toward a goal while persisting progress and restarting with fresh context to avoid context rot (Orosz, 2026).

- Loop engineering replaces direct prompting with systems that prompt agents repeatedly until a goal is achieved.
- The concept originated from Geoffrey Huntley's 'Ralph Wiggum' Bash loop technique for working around context window limits.
- Major agent harnesses (Codex, Hermes, Claude Code) now offer /goal commands that automate the loop as a single persistent objective.
- Common real-world loops include event-triggered fixes (Sentry issues, flaky tests) and scheduled jobs (nightly e2e tests, daily product improvements).
- Critics point to token costs, agent drift, and the possibility that loops are a temporary workaround for tooling gaps; context engineering may be more valuable.