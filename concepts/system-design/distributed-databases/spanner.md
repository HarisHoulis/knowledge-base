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

Spanner is a rare example of a production distributed database system that provides distributed transactions over data spread across multiple data centers. The motivation came from Google's advertising system, which previously relied on manually sharded MySQL and Bigtable databases, making multi-shard transactions impossible. The workload was dominated by read-only transactions, and the system required strong consistency, specifically serializable transactions with external consistency, meaning once a transaction commits, subsequently started transactions must observe its effects. (MIT 6.824 Lecture 13, Spanner)

- Spanner runs two-phase commit over Paxos-replicated participants, avoiding the classic problem of a crashed coordinator blocking all participants.
- Synchronized time is used to enable efficient read-only transactions while maintaining external consistency.
- Spanner replicates data across multiple data centers using a Paxos variant similar to Raft, with leaders managing each shard.
- The system was inspired by the need for wide-area transactions and has influenced open-source systems like CockroachDB.
- Google's advertising database workload was predominantly read-only, motivating efficient read-only transaction support.