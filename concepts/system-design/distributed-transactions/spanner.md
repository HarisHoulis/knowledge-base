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

Spanner is a rare production system that provides distributed transactions over data spread across multiple data centers worldwide. It was motivated by Google's advertising database, where data was sharded over many MySQL and Bigtable systems, making manual sharding difficult and preventing transactions across shards. The designers required serializable transactions and external consistency, meaning if one transaction commits, later transactions must see its effects (MIT 6.824 Lecture 13, 2020).

To achieve this, Spanner uses two-phase commit over Paxos-replicated participants, avoiding the classic problem where a crashed coordinator blocks all participants. It also uses synchronized time (TrueTime) to enable efficient read-only transactions without complex coordination. The workload was dominated by read-only transactions (billions vs. millions of read-write transactions), so this optimization was critical (MIT 6.824 Lecture 13, 2020).

Spanner has been widely used inside Google, offered as a cloud service, and inspired open-source systems like CockroachDB. Its design combines sharding, Paxos-based replication, and global transactions to provide strong consistency across geographically distributed data (MIT 6.824 Lecture 13, 2020).

- Spanner runs two-phase commit over Paxos-replicated participants to prevent coordinator crashes from blocking transactions.
- TrueTime synchronized clocks enable efficient read-only transactions without expensive coordination.
- Motivated by Google's advertising system, which needed cross-shard transactions and external consistency.
- Workload is dominated by read-only transactions, shaping Spanner's optimization priorities.
- Spanner inspired open-source distributed databases like CockroachDB.