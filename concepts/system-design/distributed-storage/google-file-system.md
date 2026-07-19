---
domain: system-design
subdomain: distributed-storage
concept: google-file-system
title: Lecture 3: GFS
sources:
  - title: "Lecture 3: GFS"
    url: "https://www.youtube.com/watch?v=EpIgvowZr00"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-02-13T11:18:33+00:00"
---

# Lecture 3: GFS

This lecture introduces the Google File System (GFS), a distributed storage system designed for large-scale data processing. The talk highlights the inherent tensions in building distributed storage: performance is achieved through sharding data across many servers, but this leads to frequent faults, requiring automated fault tolerance via replication. Replication, in turn, risks data inconsistency, and achieving strong consistency degrades performance. GFS navigates this trade-off by providing a simple, relaxed consistency model that prioritizes high aggregate throughput and availability over strict consistency, making it suitable for Google's data-intensive applications.

- Distributed storage systems must balance performance, fault tolerance, and consistency; improving one often hurts another.
- Sharding data across many servers enables parallel reads but makes faults common, necessitating automated replication for fault tolerance.
- Replication without careful design leads to inconsistencies, and achieving strong consistency requires costly coordination that reduces performance.
- GFS accepts a relaxed consistency model to achieve high performance and availability for large-scale, append-heavy workloads.