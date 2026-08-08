---
domain: system-design
subdomain: distributed-storage
concept: google-file-system
title: Lecture 3: GFS (Google File System)
sources:
  - title: "Lecture 3: GFS"
    url: "https://www.youtube.com/watch?v=EpIgvowZr00"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-02-13T11:18:33+00:00"
---

# Lecture 3: GFS (Google File System)

This lecture introduces GFS as a case study in building large-scale distributed storage systems. It emphasizes that storage is a key and general abstraction in distributed systems, and that sharding data across hundreds or thousands of servers is a way to achieve high aggregate performance. However, with that many servers, faults become a constant, everyday occurrence, so automatic fault tolerance is required [1].

Replication is highlighted as a powerful technique for fault tolerance, but if replicas are not carefully managed, they can diverge, causing applications to get different answers depending on which replica they contact. Strong consistency is possible but requires extra coordination and reduces performance, creating an inherent tension between performance, fault tolerance, and consistency [1].

- Storage is a central and general abstraction in distributed systems.
- Sharding across many servers enables huge aggregate performance but makes faults the norm.
- Replication provides fault tolerance but can lead to inconsistent replicas if not coordinated.
- Strong consistency is expensive and trades off against performance.