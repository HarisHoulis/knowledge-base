---
domain: ai-workflows
subdomain: loop-engineering
concept: loop-engineering
title: What is “loop engineering?”
sources:
  - title: "What is “loop engineering?”"
    url: "https://newsletter.pragmaticengineer.com/p/what-is-loop-engineering"
    author: "Gergely Orosz"
    date: "2026-07-14"
---

# What is “loop engineering?”

Loop engineering is an emerging practice in AI-assisted development where engineers design and manage loops that automatically prompt AI agents, rather than writing individual prompts. The term gained prominence after Boris Cherny of Anthropic stated, “My job is to write loops,” and was popularized by the “Ralph loop” technique, a Bash loop that repeatedly feeds a prompt to an AI coding agent until a goal is achieved (Orosz, 2026). This approach abstracts the orchestration of repeated agent runs, allowing developers to set durable objectives and let the agent iterate autonomously.

By mid-2026, major coding harnesses such as Codex, Hermes, and Claude Code had shipped native /goal commands that formalize the Ralph loop into a single persistent objective. These commands automatically keep the agent working until a completion condition is met, managing context, state, and subagents behind the scenes. This shift makes loop engineering accessible to a broader audience, reducing the need for custom scripting (Orosz, 2026).

Real-world applications of loop engineering fall largely into two categories: event-driven triggers and scheduled cron jobs. Examples include automatically opening PRs for new Sentry issues, fixing flaky tests, triaging incidents, and babysitting nightly end-to-end test runs. However, some developers report disappointment, citing agent drift and high token costs. Distinguished engineer Max Kanat-Alexander suggests loops may have been a temporary hack while tooling caught up, and many engineers may find more value in understanding context windows than in deep loop engineering (Orosz, 2026).

- Loop engineering shifts developers from prompting agents to designing systems of loops that prompt agents automatically.
- The Ralph loop—a simple Bash loop re-running an agent with a goal—is the conceptual origin of the practice.
- Major AI harnesses now support /goal commands that natively implement persistent, autonomous loops.
- Common use cases include event-triggered automations and scheduled jobs, such as opening PRs or fixing flaky tests.
- Critics note issues like agent drift, high token costs, and the possibility that loops are a temporary workaround for immature tooling.