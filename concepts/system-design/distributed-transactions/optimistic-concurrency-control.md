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

This MIT 6.824 lecture introduces FaRM, a research prototype for distributed transactions that exploits RDMA networking to achieve extremely low latencies. The talk contrasts FaRM with Spanner: while Spanner is a deployed system focused on geographic replication and wide-area consistency, FaRM targets a single data center and achieves 58-microsecond transactions, roughly 100x faster than Spanner's 10-100 millisecond latencies. The key technique is optimistic concurrency control, which FaRM is forced to use because RDMA seriously restricts design options, particularly by making CPU time the main bottleneck rather than network delay (MIT 6.824, 2020).

FaRM's architecture consists of sharded primary-backup pairs managed by a configuration service like Zookeeper. All replicas must be updated on writes, while reads always go to the primary. Since FaRM assumes a single data center, it does not protect against entire data center failures, only individual crashes or restoration after power loss. The lecture highlights how the performance potential of RDMA motivates the design and why optimistic concurrency control is a natural fit for this high-speed networking environment.

- FaRM delivers ~58 microsecond transactions, about 100x faster than Spanner's 10-100 ms.
- Optimistic concurrency control is required because RDMA constrains design options, shifting the bottleneck from network latency to CPU time.
- FaRM is a single-datacenter system using sharded primary-backup replication; writes update all replicas, reads go to the primary.
- Unlike Spanner, FaRM does not address geographic replication or whole-datacenter failures, focusing instead on maximizing performance within one data center.