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

Frangipani is an old distributed file system paper studied in MIT 6.824 for its design ideas around cache coherence, distributed transactions, and crash recovery. The system is intended to provide a network file system that looks like a local file system to existing UNIX applications, similar to AFS, allowing users to access home and project directories from any workstation in a small research lab of about 50 trusted people. Security is essentially not addressed because all users and computers are trusted.

- Frangipani uses a shared virtual disk called Petal for all file system data structures, including file contents, inodes, directories, and free-space information.
- Each workstation runs a Frangipani software module that implements the file system and caches data locally, while Petal acts like a remote disk with read/write block operations.
- The design focuses on supporting human users in a small organization, emphasizing shared file access and mobility across workstations.
- Key topics include cache coherence (ensuring modifications are visible despite caching), distributed transactions for complex updates, and crash recovery across multiple servers.