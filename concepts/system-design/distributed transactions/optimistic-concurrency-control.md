---
domain: system-design
subdomain: distributed transactions
concept: optimistic-concurrency-control
title: Lecture 14: Optimistic Concurrency Control
sources:
  - title: "Lecture 14: Optimistic Concurrency Control"
    url: "https://www.youtube.com/watch?v=Cw6Nj2evjSs"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-10T17:24:08+00:00"
---

# Lecture 14: Optimistic Concurrency Control

The lecture discusses Farm, a research prototype that explores the performance potential of RDMA networking for distributed transactions. Farm targets a single data center, unlike Spanner which handles geographic replication. The design is driven by RDMA's constraints, forcing the use of optimistic concurrency control. Farm achieves a simple transaction in 58 microseconds, about 100 times faster than Spanner's 10-100 milliseconds. Replication is primary-backup, with reads from the primary and updates sent to both primary and backup. The system uses Zookeeper for configuration management, but the core innovation is the combination of RDMA and optimistic concurrency control.

- Farm is a research prototype exploring RDMA's potential for high-performance transactions in a single data center.
- It uses optimistic concurrency control, which is required by RDMA's design constraints.
- Farm achieves ~58 microseconds per simple transaction, ~100x faster than Spanner's typical 10-100ms.
- Unlike Spanner, Farm focuses on CPU and network latency within a data center, not speed-of-light across data centers.
- Replication uses primary-backup: all writes go to both primary and backup, but reads only go to the primary.