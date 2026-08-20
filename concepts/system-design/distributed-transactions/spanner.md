---
domain: system-design
subdomain: distributed-transactions
concept: spanner
title: Lecture 13: Spanner
sources:
  - title: "Lecture 13: Spanner"
    url: "https://www.youtube.com/watch?v=4eW5SWBi7vs"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-07T20:23:30+00:00"
---

# Lecture 13: Spanner

Spanner is Google's distributed database that provides distributed transactions over data spread across data centers worldwide. The lecture highlights two key ideas: running two-phase commit over Paxos-replicated participants to avoid the coordinator crash blocking problem, and using synchronized time (TrueTime) to enable efficient read-only transactions (MIT 6.824 Lecture 13). The motivating use case was Google's advertising system, which previously used manually sharded MySQL/Bigtable and lacked cross-server transactions. The workload was dominated by read-only transactions (billions vs millions of read-write), and the system required strong consistency, specifically serializable transactions with external consistency (if one transaction commits, a later transaction must see its effects).

- Distributed transactions across wide-area data centers are achieved via two-phase commit over Paxos groups.
- TrueTime (synchronized clocks) allows efficient read-only transactions without heavy coordination.
- External consistency guarantees that committed transactions are visible to later transactions.
- Spanner was motivated by Google's advertising system, which needed cross-shard transactions and had a read-mostly workload.
- Replication uses a Paxos variant with leaders, similar to Raft.