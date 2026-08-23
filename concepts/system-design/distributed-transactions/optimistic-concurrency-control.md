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

The lecture introduces FaRM, a research prototype distributed system that leverages optimistic concurrency control to achieve extremely low-latency transactions. FaRM is contrasted with Spanner: both replicate data and use two-phase commit, but Spanner focuses on geographic replication across data centers, while FaRM assumes all replicas are in the same data center, aiming to exploit RDMA high-speed networking. FaRM achieves a simple transaction in 58 microseconds (Figure 7, Section 6.3), roughly 100x faster than Spanner's 10-100 milliseconds, primarily because its bottleneck is CPU time on servers rather than network delays between data centers.

FaRM uses a configuration manager (implemented with Zookeeper) to assign each shard to primary-backup pairs. Data is sharded by key, and all updates must be applied to both primary and backup replicas. Reads are always served from the primary. Replication provides fault tolerance, but unlike Spanner, FaRM does not use a consensus protocol like Paxos; instead, it relies on optimistic concurrency control to manage concurrent transactions efficiently.

- FaRM uses optimistic concurrency control to achieve 58 microsecond transactions, about 100x faster than Spanner.
- FaRM is designed for a single data center with RDMA networking, unlike Spanner's geographic replication.
- The primary bottleneck in FaRM is CPU time, not network speed of light delays.
- Data is sharded across primary-backup pairs; reads go to the primary, and all replicas are updated on writes.
- FaRM is a research prototype, not a deployed system, exploring RDMA's performance potential.