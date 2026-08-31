---
domain: system-design
subdomain: distributed-file-systems
concept: cache-consistency
title: Lecture 11: Cache Consistency: Frangipani
sources:
  - title: "Lecture 11: Cache Consistency: Frangipani"
    url: "https://www.youtube.com/watch?v=-pKNCjUhPjQ"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-14T16:28:35+00:00"
---

# Lecture 11: Cache Consistency: Frangipani

Frangipani is a distributed file system designed to provide cache coherence, distributed transactions, and crash recovery in a shared network environment. The system consists of workstations running Frangipani servers that implement file system logic, while all data is stored on a shared virtual disk called Petal, accessed via remote procedure calls. Petal replicates data for fault tolerance, and workstations cache file blocks locally for performance. The key challenge is maintaining cache coherence: when one workstation modifies a cached block, others must see the update despite having local caches (MIT 6.824, 2020).

Distributed transactions are essential internally to the file system for making complex updates to file system data structures, such as inodes, directories, and free-block lists. Because the file system is split across multiple servers, crash recovery is critical to ensure consistency after failures. Frangipani's design is motivated by a small research lab of around 50 trusted users who need to share home directories and project files across any workstation; thus, security is not a primary concern and the system assumes all machines and users are trusted (MIT 6.824, 2020).

- Frangipani uses a shared virtual disk (Petal) for storage, with workstations caching blocks for performance.
- Cache coherence ensures that cached data reflects modifications made by other clients.
- Distributed transactions manage complex updates to file system metadata across multiple servers.
- Crash recovery is critical because the file system is distributed and must remain consistent after failures.
- The system is designed for a small, trusted research group, so security is largely ignored.