---
domain: ai-workflows
subdomain: loop-engineering
concept: loop-engineering
title: What is “loop engineering?”
sources:
  - title: "What is “loop engineering?”"
    url: "https://newsletter.pragmaticengineer.com/p/what-is-loop-engineering"
    author: "Gergely Orosz"
    date: "Tue, 14 Jul 2026"
---

# What is “loop engineering?”

Loop engineering is an emerging practice where engineers design systems that run AI agents in iterative loops, rather than writing individual prompts. The term gained traction after Boris Cherny of Anthropic and Peter Steinberger of OpenClaw described their work as writing loops that prompt AI agents, with Cherny stating, “My job is to write loops.” The approach is abstract to many, but the article gathers developer examples to clarify how it works in practice (Orosz, 2026).

- Loop engineering replaces the role of a human prompter with a designed system that runs agents repeatedly toward a goal.
- The technique originated from Geoffrey Huntley's 'Ralph Wiggum' method, a Bash loop that continuously feeds a prompt to Claude Code with a state tracker.
- By May 2026, major coding harnesses like Codex, Hermes, and Claude Code shipped a /goal command that compresses the Ralph loop into a single persistent objective.
- Common real-world loops include event-driven triggers and cron jobs: opening PRs for Sentry issues, fixing flaky tests, triaging outages, and babysitting nightly E2E tests.
- Some developers report disappointment due to agent drift, high token costs, and the need for human-in-the-loop review; Max Kanat-Alexander suggests loops may be a temporary hack while tooling catches up.