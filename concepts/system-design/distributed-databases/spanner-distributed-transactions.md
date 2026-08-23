---
domain: system-design
subdomain: distributed-databases
concept: spanner-distributed-transactions
title: Lecture 13: Spanner
sources:
  - title: "Lecture 13: Spanner"
    url: "https://www.youtube.com/watch?v=4eW5SWBi7vs"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-07"
---

# Lecture 13: Spanner

Spanner is a Google system that provides distributed transactions over data spread across multiple data centers, a rare capability in production systems. The lecture highlights two key design ideas: running two-phase commit over Paxos-replicated participants to avoid coordinator crash blocking, and using synchronized time to make read-only transactions efficient. Spanner was inspired by Google's advertising system, whose workload was dominated by read-only transactions and required serializable transactions with external consistency—meaning a transaction that starts after another commits must see the first transaction's writes. The system physically shards data by key across servers and replicates each shard in multiple data centers, with replication managed by a leader-based Paxos variant similar to Raft. Spanner became a Google Cloud service and influenced open-source systems like CockroachDB (Lecture 13: Spanner).

- Spanner combines two-phase commit with Paxos replication to achieve wide-area distributed transactions without a single point of failure.
- Synchronized time enables efficient read-only transactions, which dominated the motivating workload (billions of read-only vs millions of read-write transactions).
- Spanner guarantees external consistency: once a transaction commits, subsequent transactions must observe its effects.
- Data is sharded by key and replicated across data centers; each Paxos instance manages the replicas of a shard.
- Spanner was motivated by Google's advertising database needs and later became a cloud service, influencing CockroachDB.