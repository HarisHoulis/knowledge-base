---
domain: system-design
subdomain: distributed-filesystems
concept: cache-consistency
title: Lecture 11: Cache Consistency: Frangipani
sources:
  - title: "Lecture 11: Cache Consistency: Frangipani"
    url: "https://www.youtube.com/watch?v=-pKNCjUhPjQ"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-14T16:28:35+00:00"
---

# Lecture 11: Cache Consistency: Frangipani

Frangipani is an older distributed file system paper studied for its design around cache coherence, distributed transactions, and crash recovery. It provides a network file system that appears to existing UNIX applications as a local file system, intended for a research lab of about 50 trusted users who access shared home and project files from any workstation (MIT 6.824 Lecture 11, 2020).

The architecture places a Frangipani server on each user workstation, while all persistent file system data—including inodes, directories, file contents, and free-block information—lives on a shared virtual disk called Petal. Petal is a separate set of server machines that replicate data for fault tolerance, and it behaves like a disk drive: Frangipani sends remote procedure calls to read and write specific blocks by address (MIT 6.824 Lecture 11, 2020).

The main ideas are cache consistency (ensuring a workstation sees modifications made by others despite its local caches), distributed transactions for complex updates to file system data structures, and crash recovery in this distributed setting. Because the environment is small and trusted, the design largely ignores security (MIT 6.824 Lecture 11, 2020).

- Frangipani is a network file system that looks like a local UNIX file system to applications, running on user workstations.
- All data is stored on Petal, a shared virtual disk accessed via RPC, which replicates data for availability.
- The paper focuses on cache coherence, distributed transactions, and crash recovery for a distributed file system.
- The intended use is a small trusted organization (~50 people), so security is not addressed.
- Frangipani aims to allow users to access their home and shared project files from any workstation.