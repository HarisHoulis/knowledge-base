---
domain: system-design
subdomain: distributed-systems
concept: optimistic-concurrency-control
title: Lecture 14: Optimistic Concurrency Control
sources:
  - title: "Lecture 14: Optimistic Concurrency Control"
    url: "https://www.youtube.com/watch?v=Cw6Nj2evjSs"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-10T17:24:08+00:00"
---

# Lecture 14: Optimistic Concurrency Control

Farm shards data across primary-backup pairs, with reads always going to the primary and no consensus protocol like Paxos for replica coordination. The use of RDMA severely restricts design options, which forces the adoption of optimistic concurrency control. The lecture contrasts this with Spanner, where the main bottleneck is speed-of-light delays across data centers, while Farm's bottleneck is CPU time on servers within a single data center (MIT 6.824, 2020).

- Farm achieves 58-microsecond transactions, about 100x faster than Spanner's 10-100ms.
- Optimistic concurrency control is used because RDMA constraints make other approaches difficult.
- Farm assumes all replicas are in the same data center, not geographically distributed.
- Replication uses primary-backup with reads from primary, not Paxos.
- Farm targets CPU-bound bottlenecks, while Spanner targets network-latency bottlenecks.