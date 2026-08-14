---
domain: ai-workflows
subdomain: ai-agent-loops
concept: loop-engineering
title: What is 'Loop Engineering?'
sources:
  - title: "What is “loop engineering?”"
    url: "https://newsletter.pragmaticengineer.com/p/what-is-loop-engineering"
    author: "Gergely Orosz"
    date: "Tue, 14 Jul 2026 17:01:57 GMT"
---

# What is 'Loop Engineering?'

Loop engineering is an emerging approach to working with AI coding agents where instead of writing individual prompts, engineers design iterative loops that autonomously prompt agents and drive them toward a goal. The term gained traction after Anthropic's Boris Cherny and others revealed they spend their time writing loops rather than prompts. The article traces the concept's origins to Geoffrey Huntley's 'Ralph Wiggum' technique, which used a simple Bash loop to repeatedly feed a prompt file to Claude Code, breaking ambitious projects into smaller agent runs to work around context window limits.

- Loop engineering replaces manual prompting with designing autonomous agent loops, often using a /goal command in coding harnesses like Codex, Hermes, and Claude Code.
- The 'Ralph Wiggum' method, popularized by Geoffrey Huntley, uses repeated agent runs with a persistent goal, updating a master plan and logging progress to overcome context window constraints.
- Common use cases include event triggers, cron jobs, fixing flaky tests, triaging issues, opening PRs, and babysitting nightly test runs.
- Some developers report disappointment with loops due to agent drift, high token costs, and the superior results of human-in-the-loop approaches.
- Distinguished engineer Max Kanat-Alexander suggests looping may be a temporary hack while tooling catches up, and 'context engineering' may be more valuable for most developers.