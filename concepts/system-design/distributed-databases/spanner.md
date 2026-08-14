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

Physically, Spanner shards data by key and replicates each shard across multiple data centers using a Paxos variant with leaders, similar to Raft. Clients are typically web servers within the data centers, and each Paxos group manages the replicas of a given shard [1].

- Spanner provides distributed transactions and external consistency across globally distributed data.
- Two-phase commit is made fault-tolerant by running participants on Paxos replicated groups.
- Synchronized time (TrueTime) enables efficient, lock-free read-only transactions.
- The motivating workload was Google's advertising system, dominated by read-only transactions.
- Data is sharded by key and replicated across data centers via Paxos groups.