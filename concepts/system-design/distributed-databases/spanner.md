---
domain: system-design
subdomain: distributed-databases
concept: spanner
title: Lecture 13: Spanner
sources:
  - title: "Lecture 13: Spanner"
    url: "https://www.youtube.com/watch?v=4eW5SWBi7vs"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-07T20:23:30+00:00"
---

# Lecture 13: Spanner

This lecture discusses Google's Spanner, a rare production system that provides distributed transactions over data spread across multiple data centers worldwide. Spanner addresses the challenge of combining wide-area data replication with ACID transactions, which is highly desirable for programmer productivity and fault tolerance but technically difficult to achieve in practice. The lecture highlights two key design ideas: running two-phase commit over Paxos-replicated participants to avoid the blocking problem of a crashed coordinator, and using synchronized time (TrueTime) to enable efficient read-only transactions with external consistency. The motivating use case was Google's advertising database, which was previously sharded across many MySQL and Bigtable instances, making manual sharding cumbersome and preventing cross-shard transactions. The workload was dominated by read-only transactions (billions) compared to read-write transactions (millions), yet strong consistency and external consistency were required. The lecture also describes the physical arrangement where data is sharded by key and replicated across data centers, with replication managed by a Paxos variant similar to Raft.

- Spanner provides distributed transactions over data replicated across widely separated data centers, a rare capability in production systems.
- Two-phase commit is used over Paxos-replicated participants to prevent a crashed coordinator from blocking all participants.
- Synchronized time (TrueTime) enables efficient read-only transactions while maintaining external consistency.
- The system was inspired by Google's advertising database, which needed serializable transactions across shards and had a read-dominated workload.
- Data is sharded by key and each shard is replicated at multiple data centers using a Paxos-based replication protocol.