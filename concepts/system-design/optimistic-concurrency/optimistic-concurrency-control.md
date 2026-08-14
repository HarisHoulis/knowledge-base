---
domain: system-design
subdomain: optimistic-concurrency
concept: optimistic-concurrency-control
title: Lecture 14: Optimistic Concurrency Control
sources:
  - title: "Lecture 14: Optimistic Concurrency Control"
    url: "https://www.youtube.com/watch?v=Cw6Nj2evjSs"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-10T17:24:08+00:00"
---

# Lecture 14: Optimistic Concurrency Control

This lecture from MIT 6.824 introduces optimistic concurrency control through the lens of FaRM, a research prototype that leverages RDMA networking to achieve extremely low-latency transactions. The lecture contrasts FaRM with Spanner: while Spanner focuses on geographic replication across data centers with transactions taking 10-100 milliseconds, FaRM assumes all replicas reside in the same data center and achieves transaction times around 58 microseconds, roughly 100 times faster than Spanner (Lecture 14). FaRM's design is driven by the performance potential of RDMA NICs, which restrict design choices and push the system toward optimistic concurrency control rather than pessimistic locking or Paxos-based replication.

- FaRM is a research prototype targeting single-datacenter deployments, unlike Spanner which focuses on geographic replication.
- FaRM uses RDMA to minimize network overhead, achieving 58 microsecond transactions compared to Spanner's 10 milliseconds.
- The system shards data across primary-backup pairs and relies on optimistic concurrency control due to RDMA constraints.
- The main bottleneck in FaRM is CPU time on servers, not network speed-of-light delays.
- Replication in FaRM is not managed by Paxos; all replicas are updated on writes and reads always go to the primary.