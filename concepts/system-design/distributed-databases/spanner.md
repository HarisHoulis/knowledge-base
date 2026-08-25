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

Spanner is a rare example of a distributed database system that provides distributed transactions over data spread across multiple data centers. The paper was motivated by Google's advertising system, which needed to shard data across many MySQL and Bigtable databases and required transactions spanning multiple shards. The workload was dominated by readonly transactions, and external consistency was a key requirement.

Spanner uses two-phase commit, but runs it over Paxos-replicated participants to avoid the problem of a crashed coordinator blocking everyone. Data is sharded by key and each shard is replicated across data centers using a Paxos variant with leaders, similar to Raft.

Spanner uses synchronized time (TrueTime) to enable efficient readonly transactions and external consistency. External consistency ensures that if transaction T1 commits before T2 starts, T2 sees T1's modifications, which is interesting with replicated data. Spanner has inspired other systems like CockroachDB.

- Distributed transactions over wide-area replicated data are possible and practical.
- Two-phase commit over Paxos groups prevents a crashed coordinator from blocking the system.
- TrueTime synchronization enables efficient readonly transactions and external consistency.
- Spanner was motivated by Google's advertising system, with a workload dominated by readonly transactions.
- Spanner's design has influenced open-source systems such as CockroachDB.