---
domain: ai-workflows
subdomain: coding-agents
concept: agent-verification
title: Teach Your Agent to Prove It's Done
sources:
  - title: "Teach Your Agent to Prove It's Done — Nick Nisi & Zack Proser, WorkOS"
    url: "https://www.youtube.com/watch?v=q4WC4TowkBo"
    author: "AI Engineer"
    date: "2026-10-18"
---

# Teach Your Agent to Prove It's Done

Nick Nisi and Zack Proser (WorkOS) open their "Beyond Done" workshop by framing the core problem of agentic coding: once agents write code faster than humans can review it, manual PR review stops scaling and creates a signal-to-noise problem. They cite the widely discussed incident where an agent deleted working databases in nine seconds as motivation for building trust rather than checking every line [source: talk].

- Manual review of agent-generated code doesn't scale; agents produce code faster than humans can review it, creating a signal-to-noise problem
- Agents can self-verify using tools like Playwright (e.g., submitting a form and confirming a success message), but such self-reports are often—not always—trustworthy
- The goal is to build gradual trust in agents so you don't have to check every line or every PR, as a foundation for true scalability
- The workshop is repository-based and interactive, with slides, exercises, a glossary, and an 'ask anything' chat at talks.workos.cloud/beyond-done