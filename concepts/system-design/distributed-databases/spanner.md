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

Spanner is Google's distributed database that supports distributed transactions over data spread across multiple data centers. The lecture highlights two key design ideas: running two-phase commit over Paxos-replicated participants to prevent a crashed coordinator from blocking everyone, and using synchronized time to enable efficient read-only transactions with external consistency (MIT 6.824 Lecture 13).

- Spanner combines two-phase commit with Paxos replication to make wide-area transactions fault-tolerant.
- It uses synchronized time (TrueTime) to provide externally consistent read-only transactions efficiently.
- Data is sharded by key and replicated across data centers, with each shard managed by a Paxos group.
- The motivating workload was Google's advertising system, which was sharded across many MySQL/Bigtable databases and dominated by read-only transactions.
- Spanner inspired other systems like CockroachDB.