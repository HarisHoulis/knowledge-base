---
domain: system-design
subdomain: distributed-systems
concept: distributed-systems-intro
title: Introduction to Distributed Systems
sources:
  - title: "Lecture 1: Introduction"
    url: "https://www.youtube.com/watch?v=cQP8WApzIQQ"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-02-06T18:38:04+00:00"
---

# Introduction to Distributed Systems

A distributed system is a set of cooperating computers communicating over a network to accomplish a coherent task (source: Lecture 1). Key examples include storage for large websites, big data computation like MapReduce, and peer-to-peer file sharing. The lecturer emphasizes that if a problem can be solved on a single computer, it should be, as distributed systems are inherently more complex (source: Lecture 1).

- Distributed systems consist of multiple computers cooperating over a network.
- Only use distributed systems when necessary; single-computer solutions are simpler.
- Key motivations: performance, fault tolerance, physical distribution, and security.
- Main challenges: concurrency, partial failures, and achieving expected speedup.
- Examples include big data storage, MapReduce, and peer-to-peer file sharing.