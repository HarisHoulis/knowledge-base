---
domain: system-design
subdomain: distributed-databases
concept: spanner-architecture
title: Spanner: Distributed Transactions over Wide Area
sources:
  - title: "Lecture 13: Spanner"
    url: "https://www.youtube.com/watch?v=4eW5SWBi7vs"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-07T20:23:30+00:00"
---

# Spanner: Distributed Transactions over Wide Area

Spanner is a rare production system that provides distributed transactions over data replicated across multiple data centers worldwide. It addresses the tension between the desirability of transactions and the need for geographic data distribution for fault tolerance and low-latency access. The motivating use case was Google's advertising database, previously sharded over many MySQL/Bigtable instances, where manual sharding was awkward and read-only transactions dominated the workload by several orders of magnitude.

- Spanner runs two-phase commit over Paxos-replicated participants, avoiding the classic two-phase commit problem where a crashed coordinator blocks all participants.
- It uses synchronized time to achieve efficient read-only transactions and external consistency, ensuring that if a transaction commits, later transactions see its effects.
- Data is sharded by key and each shard is replicated across multiple data centers via Paxos, with clients typically being web servers in those data centers.
- The workload was predominantly read-only, motivating a design optimized for strongly consistent, serializable reads with high performance.