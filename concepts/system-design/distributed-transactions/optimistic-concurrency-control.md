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

The lecture introduces Farm, a research prototype for distributed transactions that leverages RDMA networking. Farm uses optimistic concurrency control as a core technique, achieving extremely fast transaction latencies—58 microseconds per simple transaction, about 100x faster than Spanner. Unlike Spanner, which targets geographic replication across data centers, Farm assumes all replicas are in the same data center, focusing on CPU and network latency within a single facility (MIT 6.824, 2020).

- Farm achieves 58-microsecond transactions using RDMA and optimistic concurrency control, about 100x faster than Spanner.
- It targets single-datacenter deployments, unlike Spanner's geographic replication.
- Data is sharded across primary-backup pairs; reads go to primary, writes replicate to all.
- RDMA constraints force the use of optimistic concurrency control.
- Farm is a research prototype exploring the performance potential of high-speed RDMA NICs.