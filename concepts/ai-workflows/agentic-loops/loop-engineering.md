---
domain: ai-workflows
subdomain: agentic-loops
concept: loop-engineering
title: What is Loop Engineering?
sources:
  - title: "What is “loop engineering?”"
    url: "https://newsletter.pragmaticengineer.com/p/what-is-loop-engineering"
    author: "Gergely Orosz"
    date: "Tue, 14 Jul 2026 17:01:57 GMT"
---

# What is Loop Engineering?

Loop engineering refers to designing systems that autonomously iterate AI agents toward a goal, replacing manual prompting. The concept gained traction after Anthropic’s Boris Cherny and others stated they 'write loops' instead of prompts. The technique originated from the 'Ralph Wiggum' method, where a Bash loop continuously feeds an agent a prompt until a goal is met. This approach works around context window limitations by breaking tasks into smaller runs with fresh context. By May 2026, major AI coding harnesses like Codex, Claude Code, and Hermes shipped native /goal commands, making loop engineering as simple as a single command. Common developer use cases include triggers (e.g., opening PRs on Sentry issues) and cron jobs (e.g., nightly test babysitting). However, some developers reject looping due to high token costs, agent drift, and the need for human oversight. Distinguished engineer Max Kanat-Alexander suggests loops may have been a temporary hack while tooling caught up. Ultimately, for most software engineers, understanding context windows may be more valuable than deep loop engineering. (Source: Orosz, Gergely. 'What is Loop Engineering?' The Pragmatic Engineer, 14 Jul 2026.)

- Loop engineering replaces manual prompting with automated loops that keep an agent working toward a goal until completion.
- The 'Ralph Wiggum' technique—a simple Bash loop feeding a prompt repeatedly—sparked the loop engineering trend.
- By May 2026, Codex, Claude Code, and Hermes all shipped native /goal commands that implement loop-like behavior.
- Common loop engineering use cases include event-driven triggers (e.g., bug triage, PR creation) and scheduled cron jobs (e.g., flaky test fixes).
- Some developers find loops expensive, prone to drift, and less effective than a human-in-the-loop approach.