---
domain: system-design
subdomain: distributed-file-systems
concept: frangipani-cache-coherence
title: Lecture 11: Cache Consistency: Frangipani
sources:
  - title: "Lecture 11: Cache Consistency: Frangipani"
    url: "https://www.youtube.com/watch?v=-pKNCjUhPjQ"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-14T16:28:35+00:00"
---

# Lecture 11: Cache Consistency: Frangipani

Frangipani is an early distributed file system studied for its design around cache coherence, distributed transactions, and crash recovery. The system presents a standard file system interface to existing UNIX applications, running a Frangipani server on each user's workstation. Actual file system data structures—inodes, directories, file contents, and free-block metadata—are stored on a shared virtual disk called Petal, accessed via remote procedure calls. This separation allows workstations to cache data locally, but requires careful coherence mechanisms to ensure modifications are visible to all users (MIT 6.824 Lecture 11).

The lecture motivates the design by describing a research lab of about 50 trusted users who need to share files and access their home directories from any workstation. This small, trusted context simplifies security concerns, allowing focus on core distributed systems challenges. The paper explores how cache coherence, distributed transactions, and crash recovery interact to maintain consistency in a system split across many servers. Key ideas include using Petal as a shared storage backend, running file system logic on clients, and coordinating updates through distributed transactions and recovery protocols (MIT 6.824 Lecture 11).

- Frangipani uses a shared virtual disk (Petal) for storage, while file system logic runs on client workstations.
- The design targets a small, trusted user group, emphasizing cache coherence, distributed transactions, and crash recovery.
- The lecture examines the interactions between these mechanisms to keep cached data consistent across workstations.
- Frangipani presents a standard file system interface, allowing existing UNIX applications to work unchanged.