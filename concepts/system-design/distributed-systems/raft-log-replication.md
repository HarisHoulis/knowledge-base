---
domain: system-design
subdomain: distributed-systems
concept: raft-log-replication
title: Fault Tolerance: Raft (2)
sources:
  - title: "Lecture 7: Fault Tolerance: Raft (2)"
    url: "https://www.youtube.com/watch?v=4r8Mz3MMivY"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-01T04:21:19+00:00"
---

# Fault Tolerance: Raft (2)

This lecture from MIT 6.824 focuses on the log replication mechanism in the Raft consensus algorithm. The core challenge is maintaining log consistency across servers when their logs may diverge. Using an example of three servers with differing log entries, the lecturer explains how a newly elected leader (term 6) sends an AppendEntries RPC containing a 'previous log index' and 'previous log term' to ensure the follower's log matches before appending. If a follower's log at the specified index does not have the matching term, it rejects the RPC, preventing any corruption of its log (MIT 6.824, 2020).

Upon receiving a rejection, the leader decrements a per-follower 'nextIndex' and retries with an earlier entry, effectively backing up until it finds the point where the follower's log matches the leader's. Once a match is found, the leader sends all remaining entries from that point forward, and the follower overwrites any divergent entries to converge to the leader's log. This process ensures the Log Matching Property, which is essential for Raft's safety and correctness in a fault-tolerant distributed system (source: https://www.youtube.com/watch?v=4r8Mz3MMivY).

- AppendEntries RPC includes prevLogIndex and prevLogTerm to check log consistency before appending.
- Followers reject RPCs where the previous log entry does not match their own, preventing log divergence.
- Leaders decrement nextIndex on rejection and retry, backing up until finding the matching log point.
- Once a match is found, the leader sends all subsequent entries, and followers overwrite conflicting entries to converge.
- This mechanism enforces the Log Matching Property, a pillar of Raft's safety guarantees.