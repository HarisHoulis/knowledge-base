---
domain: ai-workflows
subdomain: agent-safety
concept: agent-budget-tripwires
title: Give the Agent a Budget, Not a Token
sources:
  - title: "Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic"
    url: "https://www.youtube.com/watch?v=rbjWzZK2LU0"
    author: "AI Engineer"
    date: "2026-08-22T14:00:06+00:00"
---

# Give the Agent a Budget, Not a Token

Sachin Malhotra, an engineer on the CI team at Anthropic, argues that giving an agent a token and a tool list is insufficient for production work. He illustrates this with a real incident where an agent cleaning up workloads accidentally deleted 200 workloads, impacting 20 engineers and hours of progress, all because a filter evaluated to nothing and the selector matched everything. The agent was not malicious; it genuinely believed it was tidying up after itself, but it had unbounded power to act without close supervision (Malhotra, 2026).

To address this, Malhotra proposes three safety primitives: asymmetric verbs, rate limits, and trip wires over allow lists. Asymmetric verbs means actions like delete are not symmetric with create—they require additional safeguards. Rate limits constrain how fast an agent can perform operations, and trip wires act as circuit breakers that stop the agent when unusual patterns are detected. These are preferable to simply narrowing the token scope (e.g., removing delete permissions), which is analogous to taking a verb away from a new hire and does not scale. Instead, the right approach is to write an onboarding checklist as policy for agents, structurally making catastrophic actions unreachable while preserving the agent's ability to do real work.

- A token and tool list are not enough to safely run agents in production; unbounded power can lead to catastrophic, non-malicious failures.
- The standard fix of narrowing token scope is insufficient and analogous to removing verbs from a new engineer; it does not scale.
- Three primitives help: asymmetric verbs (safeguards on destructive actions), rate limits (bound operation speed), and trip wires (circuit breakers over allow lists).
- The 'undo test' is a lens to evaluate whether an agent's actions can be reversed or rolled back.
- Agents, unlike humans, never tire and can be confidently wrong, so they need explicit policy-based guardrails.