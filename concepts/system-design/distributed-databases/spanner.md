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

Spanner is Google's globally distributed database that provides distributed transactions with external consistency. The lecture explains that Spanner achieves this by combining two-phase commit with Paxos replication, ensuring that the coordinator is not a single point of failure even when participants and coordinators are spread across data centers. This approach enables transactions over data that is widely separated, which is rare in production systems (MIT 6.824 Lecture 13, 2020).

A major motivation for Spanner was Google's advertising system, which previously relied on manually sharded MySQL and Bigtable databases, making cross-shard transactions impossible and maintenance difficult. The workload was dominated by read-only transactions—billions compared to millions of read-write transactions—so Spanner is optimized for efficient read-only operations. It uses synchronized time to provide consistent snapshots without locking, allowing these reads to be fast and non-blocking (MIT 6.824 Lecture 13, 2020).

The physical architecture of Spanner involves servers spread across multiple data centers, with data sharded by key and each shard replicated across data centers. The replication is managed by a Paxos-based protocol with leaders, similar to Raft, ensuring high availability and consistency for each shard. This design allows Spanner to offer serializable transactions and external consistency, meaning that if one transaction commits before another starts, the second transaction sees the first's modifications (MIT 6.824 Lecture 13, 2020).

- Spanner provides distributed transactions over globally replicated data using two-phase commit over Paxos groups.
- External consistency guarantees that a transaction starting after another commits will see the earlier transaction's changes.
- The system is optimized for read-only transactions, which dominate the workload, using synchronized clocks for efficient snapshot reads.
- Data is sharded by key and each shard is replicated across data centers via a leader-based Paxos protocol.
- Spanner was motivated by Google's advertising system needs for cross-shard transactions and easier shard management.