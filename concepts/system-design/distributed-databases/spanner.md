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

Spanner is a Google-built distributed database that provides transactions over data spread across multiple data centers, a rare capability in production systems. It is motivated by the need for both fault tolerance and locality—keeping copies of data close to users—while still offering strong consistency and serializable transactions. The lecture highlights two key design ideas: running two-phase commit over Paxos-replicated participants to avoid blocked transactions from a crashed coordinator, and using synchronized time (TrueTime) to enable efficient read-only transactions with external consistency (MIT 6.824, 2020).

The system was driven by Google's advertising database, which previously relied on manually sharded MySQL/Bigtable instances and did not support transactions spanning multiple servers. The workload is dominated by billions of read-only transactions versus millions of read-write transactions, so optimizing read-only performance while maintaining strong consistency was a primary goal. Spanner achieves this by sharding data by key and replicating each shard across data centers using a Paxos variant (similar to Raft) with leaders (MIT 6.824, 2020).

Physically, Spanner servers are spread over data centers worldwide, with each data center holding replicas of various shards. Web servers act as clients, connecting from any data center. The combination of Paxos-managed replication and two-phase commit allows wide-area distributed transactions, while TrueTime provides the clock synchronization necessary for ordering transactions and supporting external consistency—ensuring that if transaction T1 commits before T2 starts, T2 sees T1's effects (MIT 6.824, 2020).

- Spanner enables distributed transactions across data centers using two-phase commit over Paxos-replicated participants, preventing coordinator crashes from blocking.
- TrueTime synchronization provides external consistency and enables fast read-only transactions without expensive coordination.
- The motivating use case was Google's advertising system, which needed to shard data manually and lacked cross-shard transactions.
- Workload is predominantly read-only transactions (billions) compared to read-write transactions (millions), shaping design priorities.
- Data is sharded by key and replicated across data centers via a Paxos-based consensus protocol.