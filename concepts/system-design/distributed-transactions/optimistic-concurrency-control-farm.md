---
domain: system-design
subdomain: distributed-transactions
concept: optimistic-concurrency-control-farm
title: Lecture 14: Optimistic Concurrency Control (FaRM)
sources:
  - title: "Lecture 14: Optimistic Concurrency Control"
    url: "https://www.youtube.com/watch?v=Cw6Nj2evjSs"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-10T17:24:08+00:00"
---

# Lecture 14: Optimistic Concurrency Control (FaRM)

The lecture introduces FaRM, a research prototype for distributed transactions that leverages RDMA (Remote Direct Memory Access) networking to achieve extremely low latency within a single data center. FaRM is contrasted with Spanner: while Spanner focuses on geographic replication and handles wide-area latency via synchronized clocks, FaRM assumes all replicas are co-located, eliminating speed-of-light concerns and focusing on CPU efficiency. The design is forced to adopt optimistic concurrency control because RDMA restricts coordination overhead, yet still achieves a simple transaction in 58 microseconds—about 100x faster than Spanner's typical 10-100 ms (MIT 6.824 Lecture 14, 2020).

FaRM uses primary-backup replication for fault tolerance: each shard has a primary and backup, reads go to the primary, and updates propagate to both replicas. Configuration management is handled via Zookeeper, though this is not the paper's focus. The lecture highlights that FaRM's performance gains come from targeting CPU bottlenecks rather than network delays, and from using optimistic concurrency control to avoid locking overhead. This design makes FaRM suitable for in-datacenter workloads where high throughput and sub-millisecond transactions are critical, but it does not provide the geographic resilience of Spanner.

- FaRM is a research prototype using RDMA to achieve 58-microsecond transactions, roughly 100x faster than Spanner's 10-100 ms.
- FaRM targets a single data center, unlike Spanner's geographic replication, so its main bottleneck is CPU time rather than speed of light.
- Optimistic concurrency control is used because of RDMA's design constraints, avoiding expensive locking.
- FaRM replicates data via primary-backup pairs: reads from primary, writes to both primary and backup.
- Configuration management uses Zookeeper, but the core innovation is the RDMA-optimized transaction protocol.