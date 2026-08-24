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

This lecture from MIT 6.824 focuses on FaRM, a research prototype that leverages RDMA (Remote Direct Memory Access) to achieve extremely fast transactions within a single data center. FaRM is contrasted with Spanner: while Spanner emphasizes geographic replication and handles long-distance two-phase commit using synchronized time for read-only transactions, FaRM targets same-datacenter deployment, reducing the dominant bottleneck to server CPU time rather than network latency. The lecture highlights FaRM's transaction latency of 58 microseconds, which is roughly 100 times faster than Spanner's 10-100 milliseconds, illustrating the performance gains possible with RDMA and optimistic concurrency control (MIT 6.824, 2020).

FaRM's architecture shards data across primary-backup pairs, with all replicas updated on every change and reads always directed to the primary. Unlike consensus-based replication like Paxos, FaRM simply replicates to both primary and backup. The design is heavily influenced by RDMA's capabilities, which restrict certain coordination patterns and push FaRM toward optimistic concurrency control. The lecture also notes that while ZooKeeper is used for configuration management, the core innovation lies in the concurrency control mechanism and its fit with high-speed networking hardware. These choices enable far higher performance than Spanner, but at the cost of geographic fault tolerance, since all replicas must reside in the same data center (MIT 6.824, 2020).

- FaRM uses RDMA to deliver 58-microsecond transactions, about 100x faster than Spanner's 10-100 ms.
- Unlike Spanner's focus on geographic replication, FaRM assumes all replicas are in the same data center, optimizing for CPU time and network efficiency.
- Data is sharded across primary-backup pairs; reads go to the primary, and writes update all replicas without consensus protocols like Paxos.
- RDMA significantly constrains design choices, motivating the use of optimistic concurrency control.
- FaRM is a research prototype, not a deployed product, intended to explore RDMA's potential for transaction processing.