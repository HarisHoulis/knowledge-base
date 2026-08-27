---
domain: system-design
subdomain: distributed-transactions
concept: spanner
title: Lecture 13: Spanner
sources:
  - title: "Lecture 13: Spanner"
    url: "https://www.youtube.com/watch?v=4eW5SWBi7vs"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-07"
---

# Lecture 13: Spanner

Spanner is a rare production system that provides distributed transactions over data spread across multiple data centers. According to the MIT 6.824 lecture, it combines two-phase commit with Paxos-replicated participants to avoid the classic problem of a crashed coordinator blocking all participants. It also uses synchronized time to enable efficient read-only transactions, which is key because the motivating workload—Google's advertising system—was dominated by billions of read-only transactions compared to millions of read-write transactions. The system requires strong consistency, serializable transactions, and external consistency, meaning a transaction started after another commits must see the first transaction's effects.

- Spanner runs two-phase commit over Paxos replicated participants to prevent a coordinator crash from blocking the entire transaction.
- Synchronized clocks enable high-performance read-only transactions without heavy coordination.
- The design was motivated by Google's advertising database, which was sharded across MySQL and Bigtable and lacked cross-shard transactions.
- Data is sharded by key and each shard is replicated across data centers using Paxos, with web servers acting as clients.
- Spanner has inspired other systems like CockroachDB and is a successful example of wide-area distributed transactions.