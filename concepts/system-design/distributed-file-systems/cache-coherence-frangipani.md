---
domain: system-design
subdomain: distributed-file-systems
concept: cache-coherence-frangipani
title: Lecture 11: Cache Consistency: Frangipani
sources:
  - title: "Lecture 11: Cache Consistency: Frangipani"
    url: "https://www.youtube.com/watch?v=-pKNCjUhPjQ"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-14T16:28:35+00:00"
---

# Lecture 11: Cache Consistency: Frangipani

Frangipani is an early distributed file system designed to provide cache coherence, distributed transactions, and crash recovery in a shared network file system. The lecture highlights how these mechanisms interact, making the paper a rich source of distributed systems design ideas. The system is built around workstations, each running a Frangipani server module that implements the file system locally, while all persistent data is stored on a shared virtual disk called Petal, which is accessed via remote procedure calls for block-level reads and writes. Petal itself replicates data to survive server crashes, but from Frangipani's perspective it appears as a simple network-attached disk drive.

The intended use case is a small research lab of about 50 trusted users who need to share files and access their home directories from any workstation. This drives the design: read and write caching on each workstation, with cache coherence ensuring that modifications made by one user are visible to others despite local caches. The paper also addresses distributed transactions needed to update file system metadata (e.g., inodes, directories, free block lists) atomically across the shared disk. Crash recovery is critical because the file system is split across many servers; the design must handle failures of individual workstations and Petal servers without corrupting file system structures. Notably, the paper does not address security, as all users and computers are assumed trusted.

- Frangipani provides cache coherence by letting workstations cache file data locally while using a shared virtual disk (Petal) for persistent storage, with invalidation and update protocols to reflect changes across caches.
- Distributed transactions are used internally to atomically update file system metadata, such as inodes, directories, and free block lists, even when these structures are spread across the shared disk.
- Crash recovery is a central concern; the system must recover from failures of individual workstations and Petal servers while preserving file system consistency.
- The design targets a small, trusted research lab (~50 users) sharing files and home directories, which simplifies security but emphasizes availability and consistency for cooperative work.
- Petal acts as a network-attached disk that replicates data for fault tolerance, while Frangipani servers on each workstation manage file system logic and caching.