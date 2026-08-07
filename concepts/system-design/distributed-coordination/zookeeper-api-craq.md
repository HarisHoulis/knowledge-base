---
domain: system-design
subdomain: distributed-coordination
concept: zookeeper-api-craq
title: Lecture 9: More Replication, CRAQ
sources:
  - title: "Lecture 9: More Replication, CRAQ"
    url: "https://www.youtube.com/watch?v=IXHzbCuADt0"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-07T22:03:27+00:00"
---

# Lecture 9: More Replication, CRAQ

ZooKeeper is a fault-tolerant coordination service built on Raft. It provides a filesystem-like API with a directory hierarchy, enabling multiple applications to share a single ZooKeeper cluster. Writes are processed in order by all replicas, but reads may be served by any replica and can be stale. This design supports critical distributed systems needs such as implementing a fault-tolerant test-and-set service, master election, configuration storage, and work queues. The lecture also introduces CRAQ (Chain Replication with Apportioned Queries), a replication technique for improving read scalability while maintaining strong consistency, though the transcript focuses primarily on ZooKeeper's API and its use cases.

- ZooKeeper provides a filesystem-like API with directories and files, designed for sharing across many applications.
- Reads can be served by any replica and may be stale, while writes are applied in the same order on all replicas.
- ZooKeeper can implement a fault-tolerant test-and-set service, crucial for systems like VMware FT.
- Common uses include master election, storing configuration/state of masters, and coordinating workers via ephemeral files.
- The lecture also covers CRAQ, an alternative replication method for consistent and scalable reads.