---
domain: system-design
subdomain: reliability-engineering
concept: design-for-failure
title: How to Design for Failures
sources:
  - title: "How to Design for Failures"
    url: "https://blog.bytebytego.com/p/how-to-design-for-failures"
    author: "ByteByteGo"
    date: "2026-10-15"
---

# How to Design for Failures

ByteByteGo argues that failure-proof software is impossible because applications depend on physical machines, power, storage, and networks that can all break, so developers must instead design for failure by deciding in advance how a system behaves when parts malfunction. This starts with an "assume everything breaks" mindset and a failure model: concrete failure modes (e.g. "database writes become unavailable while reads still work") plus the practical boundary of what the system can tolerate, rather than vague claims of high availability.

Faults are defects or abnormal conditions that may stay dormant until triggered; they can be handled by fault avoidance (code reviews, input validation, capacity planning, configuration management) and fault tolerance (e.g. routing problematic files to other workers). Resilience combines both, limiting disruption and recovering. To scope failures, the article introduces failure domains (components sharing exposure, such as servers running the same defective release) and blast radius (how far consequences reach), with cell-based architecture as a way to confine impact to a subset of customers.

Impact is reduced through isolation: the bulkhead pattern partitions resources (separate worker pools for online requests vs. report exports), multi-tenant concurrency limits prevent one tenant from monopolizing capacity, and canary deployments limit exposure to faulty releases. Recovery relies on redundancy, replication, and backups. Asynchronous replication acknowledges writes before replicas receive them (lower latency, higher availability, possible data loss), while synchronous replication waits for replicas (more reliable but higher latency and lower availability).

Dependency failures are managed with timeouts, deadlines, and retry policies with limited attempts and jitter, plus circuit breakers, load shedding, backpressure, and queues. Correctness under failure requires idempotent operations (e.g. deduplicating payment requests by ID) and careful failover to avoid split-brain when a supposedly failed primary is still accepting writes.

- Design for failure by defining concrete failure modes and a failure model rather than claiming high availability.
- Combine fault avoidance (reviews, validation, capacity planning) with fault tolerance and recovery under the umbrella of resilience.
- Use failure domains and blast radius to scope impact, and isolation patterns like bulkheads, tenant limits, and canary deployments to contain it.
- Recover via redundancy, replication (async vs. sync trade-offs), and backups, while ensuring correctness with idempotency and safe failover.
- Protect against dependency failures with timeouts, deadlines, jittered retries, circuit breakers, load shedding, and backpressure.