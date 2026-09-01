---
domain: system-design
subdomain: distributed file systems
concept: cache-consistency
title: Lecture 11: Cache Consistency: Frangipani
sources:
  - title: "Lecture 11: Cache Consistency: Frangipani"
    url: "https://www.youtube.com/watch?v=-pKNCjUhPjQ"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-14T16:28:35+00:00"
---

# Lecture 11: Cache Consistency: Frangipani

The lecture discusses Frangipani, a distributed file system designed to provide cache coherence, distributed transactions, and crash recovery. Frangipani places file system logic on client workstations, while the actual data is stored on a shared virtual disk called Petal. This architecture allows workstations to cache file data locally for performance while still ensuring that modifications made by one client are visible to others through cache consistency mechanisms (MIT 6.824, 2020).

- Frangipani uses a shared virtual disk (Petal) for storage, with file system logic running on client workstations.
- Cache coherence ensures that once one client modifies a file, other clients with cached copies see the update.
- Distributed transactions are used internally to make complex file system updates atomically across the distributed system.
- The design includes crash recovery mechanisms to handle failures of both workstations and Petal servers.
- The intended use case is a small, trusted group of ~50 researchers sharing files and home directories across workstations.