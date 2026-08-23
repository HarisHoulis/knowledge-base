---
domain: ai-workflows
subdomain: agent-safety
concept: agent-budgets
title: Give the Agent a Budget, Not a Token
sources:
  - title: "Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic"
    url: "https://www.youtube.com/watch?v=rbjWzZK2LU0"
    author: "AI Engineer"
    date: "2026-08-22T14:00:06+00:00"
---

# Give the Agent a Budget, Not a Token

Sachin Malhotra, an engineer at Anthropic, argues that giving an agent a token and a tool list is insufficient for production use [1]. He illustrates this with a real incident where an agent cleaning up after itself deleted about 200 workloads in 90 seconds, impacting 20 engineers, because a filter dropped out and the selector matched everything. The agent genuinely believed it was tidying up, showing the danger of unbounded power without oversight [1]. Malhotra compares this to onboarding a junior engineer: we don't watch every keystroke, but we create escalation paths and make catastrophic actions structurally unreachable. Agents, however, never sleep and are often confidently wrong, so they need policy-based guardrails [1]. He proposes three primitives: asymmetric verbs, rate limits, and trip wires over allow lists, and suggests using the 'undo test' to evaluate them. The standard fix of narrowing token scope—like simply removing delete access—is compared to taking a verb away from a new hire; it works for a week but doesn't scale. Instead, agents should be given budgets that limit blast radius and enforce reversibility [1].

- Agents with raw token access and tool lists cause production incidents; an innocuous cleanup deleted 200 workloads in 90 seconds.
- Narrowing token scope (removing dangerous verbs) is not a durable solution—it's like taking verbs away from a new hire instead of adding guardrails.
- Use asymmetric verbs, rate limits, and trip wires over allow lists to control agent actions.
- Apply the 'undo test' to evaluate actions: the more irreversible the action, the more safeguards it needs.
- Treat agents like junior engineers: limit blast radius, provide escalation paths, and make catastrophic actions structurally unreachable.