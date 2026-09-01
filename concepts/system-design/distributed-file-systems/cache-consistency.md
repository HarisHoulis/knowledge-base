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

The lecture discusses the Frangipani distributed file system, focusing on cache coherence, distributed transactions, and crash recovery. Frangipani is designed as a network file system for a small trusted group of users, providing shared access to home directories and project files from any workstation. Each workstation runs a Frangipani server module that handles file system calls locally, caching data for performance, while the actual data structures (inodes, directories, file contents, free block maps) are stored on a shared virtual disk called Petal. Petal is implemented on separate server machines and replicates data for fault tolerance, acting like a remote disk drive that Frangipani servers read and write via remote procedure calls.

The key challenge addressed is cache coherence: when one workstation modifies cached data, other workstations must eventually see those modifications. The lecture highlights how Frangipani uses a cache consistency protocol to ensure that cached copies remain valid. Additionally, distributed transactions are required to make complex updates to file system data structures atomically, and crash recovery mechanisms are necessary because the file system is split across multiple servers. The design prioritizes support for local operations and sharing among a small, trusted set of users, which simplifies security considerations significantly (MIT 6.824 Lecture 11).

- Frangipani provides a shared file system using workstation-local caches backed by a shared virtual disk called Petal.
- Cache coherence ensures that modifications made on one workstation are visible to others despite local caching.
- Distributed transactions are used to atomically update complex file system structures across the distributed storage.
- Crash recovery is critical because the file system state is spread across multiple servers and cached locally.
- The system is designed for small, trusted groups of users, omitting strong security measures due to the trusted environment.