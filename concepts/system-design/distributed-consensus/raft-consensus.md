---
domain: system-design
subdomain: distributed-consensus
concept: raft-consensus
title: Lecture 6: Fault Tolerance: Raft (1)
sources:
  - title: "Lecture 6: Fault Tolerance: Raft (1)"
    url: "https://www.youtube.com/watch?v=64Zp3tzNbpE"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-01"
---

# Lecture 6: Fault Tolerance: Raft (1)

The lecture opens by examining a common pattern in fault-tolerant systems such as MapReduce, GFS, and VMware FT: they replicate data or computation but rely on a single entity (e.g., a master or test-and-set server) to make critical decisions like electing a primary. This centralization pushes the core fault-tolerance machinery into a single point of failure, which is problematic.

The fundamental issue is avoiding split-brain, where two nodes both believe they are the primary, leading to inconsistent state and unsafe operations. The lecture illustrates this with a replicated test-and-set server. A naive rule requiring clients to contact both replicas for every operation is shown to be worse than a single server, because any single server failure halts progress entirely. Instead, the solution must allow progress with a majority of replicas, which is exactly what Raft provides.

- Existing systems like MapReduce, GFS, and VMware FT replicate work but rely on a single decision-maker, creating a single point of failure.
- Split-brain occurs when two nodes both think they are the primary, causing conflicting updates to replicated state.
- Requiring all replicas to be contacted for each operation destroys availability; a fault-tolerant design must function with only a majority.
- Raft is introduced as a consensus protocol for state machine replication that safely avoids split-brain.