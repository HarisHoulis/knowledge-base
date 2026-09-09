---
domain: ai-workflows
subdomain: context-engineering
concept: agent-context
title: Your agents lack context: Here's how to fix "You're absolutely right!"
sources:
  - title: "Your agents lack context: Here's how to fix "You're absolutely right!""
    url: "https://www.youtube.com/watch?v=KcVkq5L-0f0"
    author: "Brandon Waselnuk"
    date: "2026-09-09T14:30:12+00:00"
---

# Your agents lack context: Here's how to fix "You're absolutely right!"

In this talk from AI Engineer, Brandon Waselnuk argues that coding agents are extremely capable but start every session without the organizational context that human developers accumulate over years. While a human engineer learns codebase norms through PRs, meetings, and on-call incidents, each new agent session begins with zero knowledge about how a company works. He advocates treating context as a first-class engineering input: agents need a mechanism to query the right context so their code looks like it was written by someone who has been on the team for years.

Waselnuk warns against common but incomplete solutions, calling them 'local maxima'. The 'curated context' trap is when teams throw markdown files into a context store; it starts working, but the repository quickly becomes stale because no one can be the all-powerful curator forever. He also describes an MCP plateau as another limited approach. The real need is to avoid failure loops where agents answer with a confident 'you're absolutely right!' and waste tokens; instead, agents should be able to ask questions when they hit a wall and retrieve fresh, accurate context automatically.

- AI agents are intelligent but lack team/company context; context engineering closes that gap.
- Context mistakes should be caught as early as possible — 'shift left for context' — to avoid expensive failure loops.
- Static curated context repositories become stale and don't scale with the team.
- Agents need a queryable context mechanism so they can ask and answer context questions autonomously.
- Success looks like AI-generated code that reviewers can merge without repeated 'you're right' correction cycles.