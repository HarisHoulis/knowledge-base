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

This lecture from MIT 6.824 discusses FaRM, a research prototype that explores the potential of RDMA high-speed networking for distributed transactions. Unlike Spanner, which focuses on geographic replication and synchronizes time across data centers, FaRM assumes all replicas reside in the same data center, enabling extremely low-latency transactions. The key trade-off is that FaRM targets CPU time as the bottleneck rather than speed-of-light delays, allowing it to achieve transaction latencies of 58 microseconds—roughly 100x faster than Spanner's 10-100 milliseconds (MIT 6.824, 2020).

FaRM uses primary-backup replication instead of Paxos, with all reads going to the primary and updates propagated to backups for fault tolerance. This replication model is simpler and faster because it avoids consensus overhead, relying instead on the primary's coordination. The design is heavily influenced by the constraints of RDMA, which restricts certain communication patterns and forces FaRM to adopt optimistic concurrency control rather than pessimistic locking (MIT 6.824, 2020).

The lecture highlights that FaRM is an exploratory system, not a finished product, and is not designed to handle data center failures as Spanner does. Its performance advantages come from co-locating replicas and minimizing network delays, making it suitable for workloads where high throughput and low latency are more critical than geographic redundancy (MIT 6.824, 2020).

- FaRM achieves 58-microsecond transactions using RDMA, about 100 times faster than Spanner's 10-millisecond transactions.
- FaRM assumes all replicas are in the same data center, focusing on CPU bottlenecks rather than network delays between data centers.
- FaRM uses primary-backup replication and always reads from the primary; updates are sent to both primary and backup for fault tolerance.
- RDMA's restrictions force FaRM to use optimistic concurrency control, a key design choice.
- FaRM is a research prototype, not a deployed system, and does not handle geographic replication or data center failures.