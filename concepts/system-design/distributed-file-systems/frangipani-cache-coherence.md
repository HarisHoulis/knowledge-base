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

Frangipani is a distributed file system designed to provide cache coherence, distributed transactions, and crash recovery. The system is structured as a set of workstations, each running a Frangipani module that implements the file system locally, while the actual storage of file system data structures (inodes, directories, file contents, free-block info) resides on a shared virtual disk called Petal. Petal acts like a network-attached disk, replicating data for fault tolerance, and workstations communicate with it via remote procedure calls to read and write disk blocks. The intended use case is a small, trusted research lab where users share files and want to access their home directories from any workstation.

- Frangipani uses a shared virtual disk (Petal) as the central store, with each workstation caching file system data locally.
- Cache coherence is a central concern: if one client modifies a cached file, other clients must eventually see the changes.
- Distributed transactions are used internally to make complex updates to file system data structures consistently.
- Crash recovery is critical because the file system is split among many servers, requiring careful handling of failures.
- The design targets small, trusted environments (e.g., a research lab), with no strong security focus.