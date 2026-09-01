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

This lecture introduces Spanner, Google's globally distributed database that provides distributed transactions across data centers. The speaker emphasizes that Spanner is a rare production system able to run transactions over data scattered across the internet, combining the desirability of transactions with the fault tolerance and locality of replicated data. Two key ideas are highlighted: running two-phase commit over Paxos-replicated participants to prevent a crashed coordinator from blocking progress, and using synchronized time to enable efficient read-only transactions [1]. The motivation for Spanner came from Google's advertising system, which had data sharded across many MySQL and Bigtable databases, making manual sharding maintenance awkward and preventing transactions across shards. The workload was dominated by read-only transactions, and the system required strong serializability and external consistency, meaning a transaction that commits must be visible to any later transaction that starts after the commit completes [1]. Physically, Spanner splits data by key and replicates each shard across multiple data centers, with Paxos managing replication. The lecture also notes that Spanner has been successful in production, inspired open-source systems like CockroachDB, and was developed partly to handle the advertising database's need for wide-area transactions and performance [1].

- Spanner provides externally consistent distributed transactions across globally replicated data, a rare capability in production systems.
- Two-phase commit is run over Paxos-replicated participants, allowing the system to tolerate coordinator failures without blocking.
- Synchronized time (TrueTime) enables efficient, lock-free read-only transactions by assigning precise snapshot timestamps.
- Spanner was motivated by Google's advertising system, which needed transactions across many shards and had a workload dominated by reads.
- The design has influenced open-source systems such as CockroachDB.