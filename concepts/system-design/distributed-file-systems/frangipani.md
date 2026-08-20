---
domain: system-design
subdomain: distributed-file-systems
concept: frangipani
title: Lecture 11: Cache Consistency: Frangipani
sources:
  - title: "Lecture 11: Cache Consistency: Frangipani"
    url: "https://www.youtube.com/watch?v=-pKNCjUhPjQ"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-14T16:28:35+00:00"
---

# Lecture 11: Cache Consistency: Frangipani

Key design challenges include ensuring cache consistency so that modifications are visible to all clients despite local caches, and using distributed transactions to perform complex updates to file system structures atomically. Additionally, crash recovery is critical and interacts with both caching and transaction mechanisms. The lecture highlights these ideas as the core contributions of Frangipani (MIT 6.824, 2020).

- Frangipani uses a shared virtual disk (Petal) as the central storage backend, accessed via RPC, while workstations run local file system modules with caches.
- Cache coherence is a primary focus: the system ensures that cached copies reflect updates made by other clients.
- Distributed transactions are employed to atomically update complex file system metadata structures, such as directories and inode bitmaps.
- Crash recovery is handled carefully, interacting with caching and transactions to maintain consistency after failures.
- The design targets a trusted, small-scale environment (e.g., a 50-person research lab), so security is largely ignored in favor of performance and simplicity.