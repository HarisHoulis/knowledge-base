---
domain: system-design
subdomain: distributed-systems
concept: optimistic-concurrency-control
title: MIT 6.824 Lecture 14: Optimistic Concurrency Control in FaRM
sources:
  - title: "Lecture 14: Optimistic Concurrency Control"
    url: "https://www.youtube.com/watch?v=Cw6Nj2evjSs"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-10T17:24:08+00:00"
---

# MIT 6.824 Lecture 14: Optimistic Concurrency Control in FaRM

This lecture from MIT 6.824 introduces FaRM, a research prototype distributed system that explores the performance potential of RDMA (Remote Direct Memory Access) networking hardware. FaRM is contrasted with Spanner: while Spanner focuses on geographic replication and wide-area transactions, FaRM assumes all replicas are in the same data center, targeting CPU time as the main bottleneck rather than speed-of-light delays. This design choice enables drastically lower latencies, with simple transactions completing in 58 microseconds compared to Spanner's 10 milliseconds, roughly 100 times faster (MIT 6.824, 2020).

FaRM uses sharding across primary-backup pairs, with a configuration manager (backed by Zookeeper) deciding which servers hold each shard. Updates must be applied to both primary and backup replicas, while reads always go to the primary. Replication is not coordinated via Paxos; instead, all replicas are updated on every change, and fault tolerance is provided as long as one replica of each shard remains available.

Because RDMA imposes restrictions on the design, FaRM is forced to use optimistic concurrency control (OCC). The lecture explains how OCC allows transactions to proceed without locking, validating at commit time to ensure serializability, which is well-suited to the low-latency, high-throughput environment enabled by RDMA. The key takeaway is that FaRM demonstrates how specialized hardware can reshape distributed systems trade-offs, achieving orders-of-magnitude performance improvements over systems designed for geo-replication.

- FaRM targets a single data center and uses RDMA to achieve 58-microsecond transactions, about 100x faster than Spanner.
- Unlike Spanner, FaRM optimizes for CPU time rather than network latency, making it unsuitable for geographic replication.
- FaRM uses optimistic concurrency control because RDMA severely restricts the available design options.
- Data is sharded across primary-backup pairs, with all replicas updated on writes and reads served from the primary.
- Replication is not managed by Paxos; fault tolerance relies on one replica per shard being available.