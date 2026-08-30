---
domain: system-design
subdomain: agent-reliability
concept: probabilistic-coordinator
title: AI Agents Are Just Distributed Systems Now
sources:
  - title: "AI Agents Are Just Distributed Systems Now — Salman Munaf, TikTok"
    url: "https://www.youtube.com/watch?v=hD9-V56FNRI"
    author: "AI Engineer"
    date: "2026-08-29T16:00:06+00:00"
---

# AI Agents Are Just Distributed Systems Now

Salman Munaf, an SRE at TikTok, argues that once an AI model starts calling external services, it ceases to be a model problem and becomes a distributed systems problem. Using the example of a refund tool that times out, he explains that a timeout means unknown, not failure—so an agent's reflexive retry can double-refund a customer unless protected by request identifiers, idempotency keys, and status lookups. The agent is best understood as a probabilistic coordinator: unlike older decision-tree workflows, its behavior is nondeterministic, so determinism must be pushed into surrounding controls.

- A timeout means unknown, not failure; agents need idempotency keys and status lookups before retrying.
- Treat an agent as a probabilistic coordinator—determinism must live in external controls like circuit breakers, rate limits, and spend/action ceilings.
- Define compensating actions per step and scope credentials to separate reads from writes instead of granting blanket permissions.
- Context that influences agent behavior is state; treat memory as a cache with invalidation and provenance.
- Human approvals must bind to a specific action, actor, and expiry to prevent scope creep (e.g., approving $30 becoming $300).