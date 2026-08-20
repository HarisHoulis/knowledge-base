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

This lecture from MIT 6.824 introduces optimistic concurrency control in the context of FaRM, a research prototype for distributed transactions. FaRM is contrasted with Spanner: while Spanner focuses on geographic replication across data centers and uses synchronized time for read-only transactions, FaRM assumes all replicas are in the same data center and leverages RDMA high-speed networking to achieve dramatically lower latency. FaRM can perform a simple transaction in 58 microseconds, compared to Spanner's 10-100 milliseconds, making it roughly 100 times faster (MIT 6.824, 2020).

The lecture explains that RDMA hardware significantly restricts design options, which forces FaRM to adopt optimistic concurrency control instead of pessimistic locking. FaRM shards data across primary-backup pairs, with all writes going to both primary and backup replicas, and reads always directed to the primary. The system uses Zookeeper for configuration management. By eliminating wide-area network delays, the main bottleneck becomes CPU time on servers, and the design aims to maximize throughput for single-datacenter workloads (MIT 6.824, 2020).

- FaRM targets single-datacenter deployments with RDMA, unlike Spanner which is designed for geographic replication across data centers.
- FaRM achieves 58-microsecond simple transactions, about 100x faster than Spanner's 10-100 millisecond range.
- RDMA hardware constraints force FaRM to use optimistic concurrency control rather than traditional pessimistic locking.
- FaRM uses primary-backup replication per shard: reads always go to the primary, and writes update both primary and backup.
- FaRM is a research prototype exploring RDMA's potential, not a finished deployed product.