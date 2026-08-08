---
domain: system-design
subdomain: distributed-systems
concept: linearizability
title: Linearizability in Distributed Systems
sources:
  - title: "Lecture 8: Zookeeper"
    url: "https://www.youtube.com/watch?v=pbmyrNjzdDk"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-05T16:52:13+00:00"
---

# Linearizability in Distributed Systems

This lecture from MIT 6.824 introduces linearizability as the standard definition for strong consistency in storage systems. It emphasizes that systems like lab 3 must be linearizable, meaning that the observed sequence of read and write operations can be rearranged into a total order that respects real-time ordering. Specifically, if one request finishes before another starts, the first must appear before the second in the linearizable order, and each read must return the value of the most recent write in that order.

The lecture also outlines methods for verifying whether a given history is linearizable. One approach is to construct a total order of operations that satisfies the real-time and read-write constraints. Alternatively, one can analyze the precedence edges implied by these constraints; if a cycle exists, the history is not linearizable. These concepts are fundamental to understanding consistency guarantees in distributed systems and are directly applied in course labs such as lab 3.

- Linearizability is a standard for strong consistency, requiring a total order of operations consistent with real time.
- A history is linearizable if each read sees the value of the most recent preceding write in that total order.
- Non-linearizability can be proven by finding a cycle in the must-precede graph of operations.
- Lab 3 specifically requires a linearizable storage system.