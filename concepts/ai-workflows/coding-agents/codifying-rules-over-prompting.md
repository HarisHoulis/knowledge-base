---
domain: ai-workflows
subdomain: coding-agents
concept: codifying-rules-over-prompting
title: Stop Prompting: Codify Agent Rules with Linters
sources:
  - title: "Stop Prompting — Greg Pstrucha, Sentry"
    url: "https://www.youtube.com/watch?v=E3KbFLAGD6A"
    author: "AI Engineer"
    date: "2026-10-09"
---

# Stop Prompting: Codify Agent Rules with Linters

Greg Pstrucha, an AI engineer at Sentry, argues that developers should stop repeatedly prompting coding agents and instead codify the rules agents must follow directly into the codebase. He opens with a relatable frustration: agents produce overly defensive code, useless tests, and unnecessary endpoints, and when you correct them, context compression can wipe out the fix within minutes, forcing you to re-introduce the same corrections again and again.

His core thesis is that deterministic checks—tests, strong typing, and especially linters—should encode the standards and code quality you expect. Historically, writing a real linter was expensive and its benefit had to be weighed against how often the problem occurred, since human developers have memory and only need to be told once or twice. In the agent era, this calculus flips: code-writing systems have no memory and repeat the same mistakes, while writing a new linter is now cheap and easy because you can delegate it to an agent.

Pstrucha recommends a concrete practice: take your past transcripts, GitHub reviews, bot reviews, and colleague feedback, and ask an agent to codify which recurring problems can be caught by deterministic linter rules. He does this regularly on a schedule to surface new rules he hasn't considered. He also warns that strong typing alone is insufficient if you don't disallow typing patterns that eliminate unwanted edge cases, since any state the application can display will force the agent to create it.

- Stop re-prompting agents for the same mistakes; codify rules deterministically in the codebase instead.
- Prioritize tests, strong typing, and linters as deterministic checks, with linters as the main focus.
- Agents lack memory and repeat mistakes, while linters are now cheap to write via agents—flipping the old cost-benefit calculus.
- Mine past transcripts, GitHub reviews, and bot reviews to discover recurring issues worth turning into linter rules.
- Strong typing is not enough unless you disallow typing patterns that permit unwanted edge cases.