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

This lecture from MIT 6.824 introduces FaRM, a research prototype designed to explore the performance potential of RDMA networking in distributed transactions. FaRM is contrasted with Spanner: while Spanner focuses on geographic replication across data centers and prioritizes fault tolerance with transactions taking tens of milliseconds, FaRM assumes all replicas are in the same data center, eliminating wide-area network delays. As a result, FaRM achieves a simple transaction in 58 microseconds, about 100 times faster than Spanner's 10-100 milliseconds. The key design constraint is RDMA, which forces FaRM to use optimistic concurrency control. FaRM shards data across primary-backup replica pairs, with reads always served by the primary, and it uses Zookeeper for configuration management. The main bottleneck in FaRM is CPU time on servers rather than network latency, because RDMA minimizes network overhead.

- FaRM is a research prototype targeting same-data-center deployments, unlike Spanner's geographic replication.
- FaRM achieves 58 microsecond transactions, roughly 100x faster than Spanner.
- RDMA networking restricts design options, leading FaRM to adopt optimistic concurrency control.
- Data is sharded across primary-backup replica pairs; reads go to the primary.
- The primary performance bottleneck is CPU time, not network delays.