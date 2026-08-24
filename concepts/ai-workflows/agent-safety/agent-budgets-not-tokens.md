---
domain: ai-workflows
subdomain: agent-safety
concept: agent-budgets-not-tokens
title: Give the Agent a Budget, Not a Token
sources:
  - title: "Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic"
    url: "https://www.youtube.com/watch?v=rbjWzZK2LU0"
    author: "AI Engineer"
    date: "2026-08-22T14:00:06+00:00"
---

# Give the Agent a Budget, Not a Token

Sachin Malhotra argues that the common demo pattern of giving an agent a token and a tool list is insufficient for production use. He illustrates this with an incident where an agent cleaning up after itself inadvertently deleted about 200 workloads because a filter evaluated to nothing, causing the selector to match everything. This impacted roughly 20 engineers and destroyed hours of uncheckpointed progress in 90 seconds, demonstrating that agents can be confidently wrong even when they are not malicious (Sachin Malhotra, AI Engineer, 2026).

- Production agents need budgets and guardrails, not just tokens and tool lists.
- Treat agents like new engineers: provide escalation paths and structurally limit catastrophic actions.
- Three primitives for agent safety: asymmetric verbs, rate limits, and trip wires over allow lists.
- Use the 'undo test' to size up agent permissions: if an action cannot be undone, require stronger oversight.
- Avoid simply removing verbs from agents; it may work temporarily but blocks legitimate tasks later.