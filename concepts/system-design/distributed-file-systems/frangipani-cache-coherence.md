---
domain: system-design
subdomain: distributed-file-systems
concept: frangipani-cache-coherence
title: Cache Consistency: Frangipani (MIT 6.824 Lecture 11)
sources:
  - title: "Lecture 11: Cache Consistency: Frangipani"
    url: "https://www.youtube.com/watch?v=-pKNCjUhPjQ"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-14"
---

# Cache Consistency: Frangipani (MIT 6.824 Lecture 11)

Frangipani is a distributed file system designed for a small, trusted research lab of about 50 people. It presents a standard file system interface to applications, running a Frangipani server on each user's workstation. All storage is provided by a shared virtual disk called Petal, which acts like a network-attached disk drive and can be replicated for fault tolerance. Frangipani servers cache data and metadata locally, and the paper's core focus is on cache coherence—ensuring that when one client modifies a file, other clients with cached copies eventually observe the changes. The system also relies on distributed transactions and crash recovery to keep the file system data structures consistent across the distributed set of servers.

The lecture emphasizes three intertwined design concerns: cache coherence, distributed transactions, and crash recovery. Cache coherence is necessary because clients cache file blocks, but modifications must be visible to other clients. Distributed transactions allow complex updates to file system structures (e.g., inodes, directories, free-block lists) to be atomic, even though the data is spread across multiple machines and the Petal disk. Crash recovery is critical because any workstation may fail at any time, and the combination of caching and transactions must ensure that the file system remains consistent and no updates are lost or half-applied.

The authors intended Frangipani for a small, cooperative environment where all users and computers are trusted, so security is not a primary concern. This design choice simplifies many aspects of the system, allowing it to focus on performance and consistency. The paper is studied in distributed systems courses because it illustrates how to build a practical system that integrates caching, transactions, and crash recovery in a compelling way.

- Frangipani is a network file system for small, trusted groups, using a shared virtual disk (Petal) for storage.
- Each workstation runs a Frangipani server that caches file data and metadata for performance.
- Cache coherence ensures that cached data is invalidated or updated when other clients modify files.
- Distributed transactions and crash recovery are used to maintain consistency across the distributed file system structures.
- The system is designed for cooperative environments, so security is not a primary focus.