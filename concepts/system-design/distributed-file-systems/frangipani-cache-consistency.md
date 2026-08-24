---
domain: system-design
subdomain: distributed-file-systems
concept: frangipani-cache-consistency
title: Frangipani: Cache Consistency in a Distributed File System
sources:
  - title: "Lecture 11: Cache Consistency: Frangipani"
    url: "https://www.youtube.com/watch?v=-pKNCjUhPjQ"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-14"
---

# Frangipani: Cache Consistency in a Distributed File System

Frangipani is a distributed file system designed to provide a shared, UNIX-like file system across a group of workstations. The system leverages a shared virtual disk called Petal for persistent storage, while each workstation runs a Frangipani server that caches file data and metadata locally for performance. The core challenge addressed is cache coherence: ensuring that when one client modifies a cached file, other clients with cached copies eventually see those changes (MIT 6.824 Lecture 11, 2020).

The paper emphasizes three intertwined mechanisms: distributed cache coherence, distributed transactions for atomic updates to file system structures (e.g., inodes, directories), and crash recovery that must work across the distributed components. Because the file system spans multiple servers and clients, maintaining consistency requires careful coordination. Frangipani is designed for a trusted environment of roughly 50 researchers, which simplifies security concerns and allows the design to focus on consistency and availability (MIT 6.824 Lecture 11, 2020).

- Frangipani uses a shared virtual disk (Petal) for storage, with client-side caching on workstations to improve performance.
- Cache coherence protocols ensure that file modifications made by one workstation are visible to other workstations despite local caching.
- Distributed transactions are used internally to atomically update file system metadata and data structures across multiple servers.
- Crash recovery is critical because the file system state is distributed across many workstations; the system must recover consistently after failures.
- The system is designed for a small, trusted group of users (e.g., a research lab), allowing the design to omit strict security measures and focus on consistency.