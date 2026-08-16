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

Farm is a research prototype that explores the performance potential of RDMA networking. The lecture contrasts Farm with Spanner: Spanner focuses on geographic replication and uses synchronized time for read-only transactions, but its read-write transactions take 10-100 milliseconds. Farm instead assumes all replicas are in the same data center, eliminating wide-area network delays, and achieves a simple transaction in 58 microseconds—about 100x faster than Spanner (MIT 6.824, 2020).

To exploit RDMA, Farm is forced to use optimistic concurrency control because RDMA severely restricts design options. Farm shards data across primary-backup pairs, with all reads going to the primary. Replicas are not maintained by Paxos or similar consensus protocols; they are updated on every change, and fault tolerance is limited to individual crashes, not whole data-center failures (MIT 6.824, 2020).

The lecture emphasizes that Farm and Spanner target different bottlenecks: Spanner is concerned with the speed of light and network delays between data centers, while Farm focuses on CPU time on servers by assuming a same-data-center environment. This design choice yields much higher throughput but sacrifices geographic replication capabilities, making Farm unsuitable for scenarios where an entire data center may go down (MIT 6.824, 2020).

- Farm is a research prototype, not a production system, aimed at exploring RDMA's performance potential.
- It achieves 58-microsecond simple transactions, roughly 100x faster than Spanner's 10-millisecond read-write transactions.
- Farm uses optimistic concurrency control because RDMA restricts design choices, and data is sharded across primary-backup pairs with reads from the primary.
- It targets a single data center, not geographic replication, and does not use consensus for replication—making it less fault-tolerant than Spanner across data centers.