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

Salman Munaf argues that the moment a language model starts calling external services, it ceases to be a model problem and becomes a distributed systems problem. He illustrates this with the example of a refund tool timing out: a timeout means unknown, not failure, so an agent's natural instinct to retry can result in a customer being refunded twice unless the system has request identifiers, idempotency keys, and status lookups.

- A timeout in an agent tool call means unknown, not failure; retries require idempotency keys and status lookup to avoid duplicate side effects.
- An agent is best understood as a probabilistic coordinator: determinism must be enforced through circuit breakers, ceilings, compensating actions, and scoped credentials.
- Context that influences an action is state, and should be treated as a cache with invalidation and provenance.
- Human approval must be bound to a specific action, actor, and expiry, otherwise it can be stretched beyond its original scope.