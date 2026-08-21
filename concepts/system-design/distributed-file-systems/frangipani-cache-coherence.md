---
domain: system-design
subdomain: distributed-file-systems
concept: frangipani-cache-coherence
title: Cache Consistency: Frangipani
sources:
  - title: "Lecture 11: Cache Consistency: Frangipani"
    url: "https://www.youtube.com/watch?v=-pKNCjUhPjQ"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-14T16:28:35+00:00"
---

# Cache Consistency: Frangipani

Lecture 11 of MIT 6.824 discusses Frangipani, an old distributed file system whose design centers on cache coherence, distributed transactions, and distributed crash recovery, and their interactions. Frangipani presents a standard UNIX file-system interface to applications; each workstation runs a Frangipani module that handles file-system calls, while all persistent file-system data structures (inodes, directories, free-block maps) live on Petal, a shared virtual disk accessed over the network as a block device. The intended environment is a small, trusted research lab (roughly 50 people) where users share home and project files and can use any workstation. (MIT 6.824, 2020)

- Frangipani is a network file system that appears as a local UNIX file system to applications, with a Frangipani server module on every workstation.
- All persistent data is stored on Petal, a shared virtual disk, so Frangipani must handle cache coherence when multiple workstations cache and modify the same blocks.
- The design combines distributed transactions with crash recovery, ensuring that complex multi-block file-system updates remain consistent even when servers fail.
- It targets a small, trusted group of users, so security is largely ignored; the goal is usability and sharing rather than fault isolation.