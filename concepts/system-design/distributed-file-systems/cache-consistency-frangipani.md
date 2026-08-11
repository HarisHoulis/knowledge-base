---
domain: system-design
subdomain: distributed-file-systems
concept: cache-consistency-frangipani
title: Lecture 11: Cache Consistency: Frangipani
sources:
  - title: "Lecture 11: Cache Consistency: Frangipani"
    url: "https://www.youtube.com/watch?v=-pKNCjUhPjQ"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-14T16:28:35+00:00"
---

# Lecture 11: Cache Consistency: Frangipani

Frangipani is a distributed file system designed to support a small group of trusted users sharing files across workstations. It uses a shared virtual disk called Petal as the persistent storage layer, with each workstation running a Frangipani module that implements file system logic, allowing applications to use standard UNIX file system calls. The design emphasizes cache coherence, distributed transactions, and crash recovery, as the file system data structures are spread across multiple servers (MIT 6.824, 2020).

The lecture highlights that cache coherence is crucial to ensure that cached data reflects modifications by other users, while distributed transactions are needed internally to make complex updates to file system structures. Because the file system is split among servers, crash recovery is essential. The intended use in a small, trusted research lab shapes the design, with no significant focus on security (MIT 6.824, 2020).

- Frangipani is a network file system intended to work with existing UNIX applications, providing shared file access across workstations.
- It uses a shared virtual disk (Petal) for storage, with all file system metadata and contents stored there.
- Cache coherence is a central concern: despite caching, modifications must be visible to all users.
- Distributed transactions are used internally to ensure consistent complex updates to file system structures.
- Crash recovery is critical because the system is distributed across servers; the design supports recovery from failures.