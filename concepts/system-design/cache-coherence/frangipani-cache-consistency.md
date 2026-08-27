---
domain: system-design
subdomain: cache-coherence
concept: frangipani-cache-consistency
title: Lecture 11: Cache Consistency: Frangipani
sources:
  - title: "Lecture 11: Cache Consistency: Frangipani"
    url: "https://www.youtube.com/watch?v=-pKNCjUhPjQ"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-14T16:28:35+00:00"
---

# Lecture 11: Cache Consistency: Frangipani

Frangipani is a distributed file system that presents a shared file namespace to workstations in a small trusted group. Each workstation runs the Frangipani server, which caches file system blocks locally, while all persistent data is stored on a shared virtual disk called Petal. This design allows applications like text editors and compilers to access shared files with low latency, while relying on Petal for durable storage (MIT 6.824, 2020).

The core challenge addressed is cache consistency: when one workstation modifies a cached file, other workstations with cached copies must see the update. Frangipani uses a lock service (via Petal) and cache invalidation to ensure coherence. Additionally, distributed transactions are used internally to atomically update file system structures such as inodes and free-block lists, which are spread across Petal. This ensures that complex multi-block updates are all-or-nothing even in the presence of crashes (MIT 6.824, 2020).

Crash recovery is simplified by Petal's replication (multiple Petal servers) and by transactional logging. Since the system is intended for a small, trusted research lab, security is not a concern; the design focuses on availability, consistency, and a familiar POSIX-like interface (MIT 6.824, 2020).

- Uses a shared virtual disk (Petal) for all file system data, with clients caching blocks for performance.
- Employs distributed transactions to atomically update file system metadata across the cluster.
- Cache coherence is maintained through invalidation and locks to ensure clients see consistent views.
- Crash recovery relies on Petal's replication and transactional logging.
- Targeted at small trusted groups, intentionally omitting security mechanisms.