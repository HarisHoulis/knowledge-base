---
domain: system-design
subdomain: distributed-file-systems
concept: frangipani-cache-coherence
title: Lecture 11: Cache Consistency: Frangipani
sources:
  - title: "Lecture 11: Cache Consistency: Frangipani"
    url: "https://www.youtube.com/watch?v=-pKNCjUhPjQ"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-14"
---

# Lecture 11: Cache Consistency: Frangipani

Frangipani is a distributed file system designed for a small, trusted organization, intended to provide a shared file system for UNIX applications across multiple workstations. It uses a shared virtual disk called Petal for storage; all file system metadata and contents are stored on Petal, while each workstation runs a Frangipani module that implements file system logic and caches data locally. The architecture aims to achieve cache coherence so that modifications by one user are visible to others, and it relies on distributed transactions for complex updates to file system structures (MIT 6.824, 2020).

The paper emphasizes three key mechanisms: cache coherence, distributed transactions, and crash recovery. Cache coherence ensures that if a user modifies a cached file, other caches eventually see the update. Distributed transactions are used to make complex updates to file system data structures atomic, which is critical because the file system is split across multiple servers. Crash recovery is also essential, as both workstations and Petal servers can fail, and the system must maintain consistency despite such failures (MIT 6.824, 2020).

The intended use case is a research lab of about 50 trusted users sharing files, which simplifies security considerations and focuses the design on consistency and availability. The separation of file system logic (in workstations) from storage (in Petal) allows each workstation to act as a cache for the shared disk, reducing network traffic and improving performance (MIT 6.824, 2020).

- Frangipani provides a shared network file system with client-side caching, backed by a Petal virtual disk.
- Cache coherence is a central design goal, ensuring updates are visible across all client caches.
- Distributed transactions enable atomic updates to file system metadata and data structures.
- Crash recovery handles failures of both workstations and storage servers to maintain consistency.
- The system targets a small trusted user group, so security is not a primary focus.