---
domain: system-design
subdomain: distributed-systems
concept: farm-optimistic-concurrency-control
title: Lecture 14: Optimistic Concurrency Control
sources:
  - title: "Lecture 14: Optimistic Concurrency Control"
    url: "https://www.youtube.com/watch?v=Cw6Nj2evjSs"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-10"
---

# Lecture 14: Optimistic Concurrency Control

The lecture discusses FaRM, a research prototype from MIT 6.824 that explores the potential of RDMA high-speed networking. Unlike Spanner, which focuses on geographic replication across data centers, FaRM assumes all replicas are in the same data center, making it unsuitable for wide-area fault tolerance. FaRM achieves a simple transaction in 58 microseconds, about 100 times faster than Spanner's 10 milliseconds, by targeting CPU time as the main bottleneck rather than speed-of-light network delays (MIT 6.824, 2020).

FaRM shards data across primary-backup pairs coordinated by a configuration manager (using Zookeeper). Writes update all replicas, while reads always go to the primary. Replication provides fault tolerance against individual crashes or entire data center power loss, but not across data centers. The design is severely restricted by RDMA, which forces the use of optimistic concurrency control instead of traditional locking mechanisms. This optimistic approach is the central technique explored in the lecture as a way to achieve high performance in a single data center environment.

- FaRM is a research prototype targeting RDMA NICs in a single data center, not geographic replication.
- FaRM's simple transactions take 58 microseconds versus Spanner's 10 milliseconds, roughly 100x faster.
- Data is sharded across primary-backup pairs; reads go to primary, writes update all replicas.
- RDMA constraints force optimistic concurrency control, avoiding locks for better performance.