---
domain: system-design
subdomain: distributed-databases
concept: spanner
title: Lecture 13: Spanner
sources:
  - title: "Lecture 13: Spanner"
    url: "https://www.youtube.com/watch?v=4eW5SWBi7vs"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-07"
---

# Lecture 13: Spanner

This lecture covers Google's Spanner, a rare production system that provides distributed transactions over data spread across multiple data centers. Spanner employs two-phase commit, but runs it over Paxos-replicated participants to avoid the classic problem of a crashed coordinator blocking all participants. This approach enables serializable transactions even when data is widely separated, which is typically very difficult to achieve in practice.

A key innovation is the use of synchronized time (TrueTime) to support efficient read-only transactions while maintaining external consistency. External consistency ensures that if transaction T1 commits before another transaction T2 starts, T2 sees T1's effects. Spanner's design was motivated by Google's advertising system, which needed to shard data across many servers and required transactions spanning multiple shards, but the workload was dominated by read-only transactions. This motivated the strong emphasis on read-only transaction performance and consistency guarantees.

- Spanner provides distributed transactions across data centers using two-phase commit over Paxos groups.
- TrueTime (synchronized clocks) enables efficient read-only transactions and external consistency.
- The motivating use case was Google's advertising system, which required both sharding and multi-server transactions.
- The workload was overwhelmingly read-only, with billions of read-only transactions versus millions of read-write transactions.