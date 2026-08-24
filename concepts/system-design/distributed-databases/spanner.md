---
domain: system-design
subdomain: distributed-databases
concept: spanner
title: Lecture 13: Spanner - MIT 6.824 Distributed Systems
sources:
  - title: "Lecture 13: Spanner"
    url: "https://www.youtube.com/watch?v=4eW5SWBi7vs"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-07T20:23:30+00:00"
---

# Lecture 13: Spanner - MIT 6.824 Distributed Systems

Spanner is a rare production system that provides distributed transactions over data spread across multiple data centers. The lecture highlights two key innovations: running two-phase commit over Paxos-replicated participants to avoid coordinator crashes blocking progress, and using synchronized time (TrueTime) to enable efficient read-only transactions with external consistency. The motivating use case was Google's advertising system, which previously used sharded MySQL/Bigtable and lacked cross-shard transactions. The workload was dominated by read-only transactions, so Spanner focuses on fast reads while still providing strong consistency (serializability and external consistency). Physically, data is sharded by key and each shard is replicated across data centers using a Paxos-based consensus protocol.

- Spanner combines two-phase commit with Paxos replication to make wide-area transactions fault-tolerant.
- Synchronized clocks (TrueTime) allow read-only transactions to avoid locks and still provide external consistency.
- The system was motivated by Google's advertising database, which needed cross-shard transactions and better performance.
- Spanner has inspired open-source systems like CockroachDB and is offered as a Google Cloud service.