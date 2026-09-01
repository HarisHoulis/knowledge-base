---
domain: system-design
subdomain: agent-reliability
concept: agents-as-distributed-systems
title: AI Agents Are Just Distributed Systems Now
sources:
  - title: "AI Agents Are Just Distributed Systems Now"
    url: "https://www.youtube.com/watch?v=hD9-V56FNRI"
    author: "Salman Munaf"
    date: "2026-08-29"
---

# AI Agents Are Just Distributed Systems Now

Salman Munaf argues that once an AI agent calls an external service, it ceases to be a model problem and becomes a distributed systems problem. He illustrates this with a refund tool timeout: a timeout means unknown, not failure, and an agent's retry instinct without idempotency can double-refund a customer. He reframes agents as 'probabilistic coordinators' that need deterministic controls around them (Munaf, AI Engineer, 2026).

Because the agent's behavior is not pre-scripted, determinism must live in the surrounding infrastructure: circuit breakers, spend and turn ceilings, compensating actions defined per step, and credentials scoped to separate reads from writes. Munaf also warns that context influencing an action is state, so it goes stale and requires invalidation and provenance like any cache. Human approval must bind to an action, an actor, and an expiry, or approving a $30 refund can quietly become approval for a $300 one.

- Treat timeouts as unknown, not failure; use idempotency keys and status lookups to avoid duplicate side effects.
- Agents are probabilistic coordinators; move determinism into external controls like circuit breakers, budgets, and compensating actions.
- Context that influences action is state; manage it like a cache with invalidation and provenance.
- Human approval must bind to an action, an actor, and an expiry to prevent scope creep.