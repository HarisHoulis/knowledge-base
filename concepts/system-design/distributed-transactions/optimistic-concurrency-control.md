---
domain: system-design
subdomain: distributed-transactions
concept: optimistic-concurrency-control
title: Lecture 14: Optimistic Concurrency Control
sources:
  - title: "Lecture 14: Optimistic Concurrency Control"
    url: "https://www.youtube.com/watch?v=Cw6Nj2evjSs"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-10T17:24:08+00:00"
---

# Lecture 14: Optimistic Concurrency Control

This lecture introduces Farm, a research prototype designed to exploit the high performance of RDMA networking for distributed transactions. Unlike Spanner, which focuses on geographic replication and tolerating data-center failures, Farm assumes all replicas are in the same data center, aiming to minimize CPU time and network overhead. The main technique is optimistic concurrency control, which is enabled by RDMA's low-latency communication. Farm achieves a simple transaction in 58 microseconds—about 100 times faster than Spanner's typical 10-millisecond transaction time (MIT 6.824 Lecture 14, 2020).

Farm's design is driven by the constraints of RDMA, which restricts design options and forces the use of optimistic concurrency control. Data is sharded across primary-backup pairs, with reads always going to the primary and updates propagated to backups for fault tolerance. The system uses a configuration manager (Zookeeper) to coordinate replicas, but the core contribution is exploring how optimistic concurrency control can deliver high throughput in a single data center while keeping consistency. The bottleneck in Farm is CPU time on servers, not network delays, which contrasts with Spanner's concern over inter-data-center speed-of-light latency (MIT 6.824 Lecture 14, 2020).

- Farm uses optimistic concurrency control, achieving 58-microsecond transactions, ~100x faster than Spanner's ~10ms.
- Farm targets a single data center with RDMA, assuming all replicas are co-located, unlike Spanner's geographic replication.
- The main bottleneck in Farm is CPU time on servers, not network or speed-of-light delays.
- Replication is primary-backup based, with reads always from the primary, and fault tolerance for individual crashes rather than whole data centers.