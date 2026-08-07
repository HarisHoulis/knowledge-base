---
domain: system-design
subdomain: distributed-systems
concept: distributed-systems-intro
title: MIT 6.824: Distributed Systems - Lecture 1: Introduction
sources:
  - title: "Lecture 1: Introduction"
    url: "https://www.youtube.com/watch?v=cQP8WApzIQQ"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-02-06T18:38:04+00:00"
---

# MIT 6.824: Distributed Systems - Lecture 1: Introduction

The lecture defines distributed systems as a set of cooperating computers communicating over a network to accomplish a coherent task, citing examples like storage for big websites, MapReduce, and peer-to-peer file sharing. It emphasizes that much critical infrastructure is built on distributed systems, but advises that if a problem can be solved on a single computer, that is always the simpler and preferable approach (MIT 6.824, 2020).

Motivations for building distributed systems include high performance through parallelism, fault tolerance via redundant computers, problems that are inherently physically distributed (e.g., interbank transfers), and security through isolation between untrusted components. The course primarily focuses on performance and fault tolerance, though physical and security constraints also appear in case studies.

Distributed systems are hard due to concurrency, which introduces complex timing interactions, and partial failures, where some components fail while others continue working—a situation unique to multi-computer systems. Additionally, achieving linear speedup with many computers is difficult, requiring careful design to realize the expected performance gains.

- Distributed systems consist of cooperating computers communicating over a network to achieve shared goals.
- Primary drivers are performance, fault tolerance, physical distribution, and security.
- Concurrency and partial failures make distributed systems inherently complex and unpredictable.
- Single-computer solutions should always be considered first because they are simpler; distributed systems are a last resort.