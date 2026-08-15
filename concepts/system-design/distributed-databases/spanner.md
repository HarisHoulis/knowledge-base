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

Spanner is Google's distributed database that provides distributed transactions over data replicated across data centers, a rare capability in production systems. It uses two-phase commit over Paxos-replicated participants to avoid the classic problem of a crashed coordinator blocking all transactions, and it uses synchronized time (TrueTime) to enable external consistency and efficient read-only transactions. The system was motivated by the needs of Google's advertising business, which required sharding across many servers and transactions spanning multiple shards, with a workload dominated by read-only operations. Spanner's architecture shards data by key and replicates each shard across multiple data centers using a Paxos-based protocol similar to Raft with leaders, ensuring both fault tolerance and data locality.

- Two-phase commit is run over Paxos-replicated participants so that the coordinator is replicated and a single crash does not block distributed transactions.
- TrueTime, a synchronized-clock mechanism with bounded uncertainty, is used to provide external consistency and support lock-free read-only transactions.
- Spanner shards data by key and replicates each shard across multiple data centers using a Paxos-based replication protocol, balancing performance and fault tolerance.
- The design was driven by Google's advertising database requirements, where cross-shard transactions and read-heavy workloads were common.