---
domain: ai-workflows
subdomain: agentic-coding
concept: loop-engineering
title: What is “loop engineering?”
sources:
  - title: "What is “loop engineering?”"
    url: "https://newsletter.pragmaticengineer.com/p/what-is-loop-engineering"
    author: "Gergely Orosz"
    date: "2026-07-14"
---

# What is “loop engineering?”

The article explains that “loop engineering” is a trending approach in AI-assisted development where engineers design systems of agent loops instead of writing individual prompts. It traces the origins to Geoffrey Huntley's “Ralph Wiggum” technique, a Bash loop that repeatedly runs Claude Code with a goal and checks progress, effectively working around context window limitations (Orosz, 2026).

By May 2026, major coding harnesses like Codex, Hermes, and Claude Code shipped a `/goal` command that automates this loop, letting an agent work toward an outcome without manual re-prompting. The article notes that this feels similar to a Ralph loop compressed into a single command (Orosz, 2026).

Common real-world uses include event triggers (e.g., opening PRs when a Sentry issue appears) and scheduled cron jobs (e.g., nightly e2e tests with an agent babysitting and fixing flakes). Developers also use loops for triaging issues, reviewing design plans, and running migrations (Orosz, 2026).

However, some developers are disappointed: loops can drift, are expensive at API token prices, and may have been a temporary hack while tooling caught up. The article suggests that “context engineering” might matter more for most developers than deep loop engineering (Orosz, 2026).

- Loop engineering replaces prompt-writing with designing agent loops that work toward a goal.
- It originated from Geoffrey Huntley's “Ralph Wiggum” Bash loop technique, which broke work into context-window-sized runs.
- Major harnesses now support `/goal`, making loops a one-command primitive.
- Common uses are event triggers and cron jobs, e.g., auto-fixing flaky tests or opening PRs from Sentry issues.
- Caveats include token costs, agent drift, and the possibility that loops were a temporary workaround for missing tooling; context engineering may be more broadly useful.