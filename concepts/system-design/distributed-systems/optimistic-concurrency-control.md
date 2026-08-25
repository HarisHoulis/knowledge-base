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

FaRM is a research prototype that uses optimistic concurrency control and RDMA networking to achieve high transaction throughput. The lecture contrasts FaRM with Spanner: Spanner focuses on geographic replication across data centers and takes 10–100 milliseconds per read-write transaction, while FaRM assumes all replicas are in the same data center and can complete a simple transaction in 58 microseconds—roughly 100x faster (MIT 6.824, 2020). FaRM's design is constrained by RDMA, which forces optimistic concurrency control rather than traditional lock-based approaches.

FaRM shards data across primary-backup pairs managed by a configuration service (Zookeeper). Reads go to the primary, and writes propagate to backups for fault tolerance. Unlike Spanner, FaRM is not designed for whole-data-center failures; it tolerates individual crashes and recovery within a single data center (MIT 6.824, 2020). The key trade-off is between performance and geographic replication, with FaRM optimizing for raw speed at the cost of not handling wide-area latency.

- FaRM uses optimistic concurrency control because RDMA networking severely restricts the design options, making traditional locking impractical.
- A simple FaRM transaction takes 58 microseconds, compared to Spanner's 10–100 milliseconds—about 100x faster.
- FaRM targets a single data center, unlike Spanner's geographic replication, and optimizes for CPU time on servers rather than speed-of-light delays.
- Replication in FaRM is primary-backup per shard, coordinated by a configuration manager (Zookeeper), and reads always go to the primary.