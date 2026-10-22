---
domain: system-design
subdomain: distributed-systems
concept: coordination-reduction
title: Why Distributed Systems Prefer Independence over Coordination
sources:
  - title: "Why Distributed Systems Prefer Independence over Coordination"
    url: "https://blog.bytebytego.com/p/why-distributed-systems-prefer-independence"
    author: "ByteByteGo"
    date: "2026-10-22"
---

# Why Distributed Systems Prefer Independence over Coordination

ByteByteGo explains that coordination—components talking to each other and waiting on responses—is essential for correctness in distributed systems (preventing double bookings, keeping replicas in sync), but it is costly because a caller cannot distinguish a slow response from a failure, forcing timeouts and coordination protocols. Coordination imposes four costs: latency (sequential round trips), availability (a service blocked on an unreachable dependency is effectively unavailable), throughput (workers serialized on a shared lock), and complexity (failure recovery across many intermediate states).

The need for coordination grows through familiar mechanisms: locks (mitigated by optimistic locking with version numbers), transactions (kept local where possible), consensus protocols like Raft that require a majority of replicas to acknowledge, and synchronous service calls that chain completion time across services.

To reduce coordination, the article advises first defining invariants—rules that must hold under concurrency and failure, such as a seat having at most one confirmed owner. Strategies include clear ownership so fewer components participate in a decision, eventual consistency to avoid waiting on every replica (accepting stale reads during replication lag), asynchronous messaging with the transactional outbox pattern to keep database updates and event publication atomic, idempotent operations keyed by a stable operation ID to tolerate duplicates, and sagas that split cross-service workflows into local transactions with compensating actions, implemented via orchestration or choreography.

The closing guidance: state invariants precisely, keep ownership boundaries small, and be explicit about retry and duplicate handling so the system makes independent progress where possible and coordinates only where correctness demands it.

- Coordination is necessary for correctness but costs latency, availability, throughput, and complexity because callers cannot distinguish delay from failure.
- Locks, transactions, consensus, and synchronous calls all increase coordination; optimistic locking and local transactions help contain it.
- Define invariants first, then reduce coordination via clear ownership, eventual consistency, and asynchronous messaging.
- The transactional outbox pattern keeps a database update and event publication atomic, and idempotent operations with stable IDs make duplicate deliveries safe.
- Sagas break cross-service workflows into local transactions with compensating actions, using orchestration or choreography.