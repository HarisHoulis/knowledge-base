---
domain: system-design
subdomain: distributed-computing
concept: spark
title: Lecture 15: Big Data: Spark
sources:
  - title: "Lecture 15: Big Data: Spark"
    url: "https://www.youtube.com/watch?v=mzIoSW-cInA"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-14T21:04:47+00:00"
---

# Lecture 15: Big Data: Spark

Spark is presented as an evolutionary successor to MapReduce. It generalizes MapReduce's two-stage map/reduce model into complete multi-step data flow graphs, which gives programmers more flexibility and expressiveness while providing the system with more opportunities for optimization and fault handling. Spark is also much better suited to iterative applications, where data is repeatedly processed in loops, than raw MapReduce.

- Spark generalizes MapReduce into multi-step data flow graphs, improving programming flexibility and system optimization.
- Spark efficiently supports iterative algorithms such as PageRank, which are awkward and slow to implement in MapReduce.
- PageRank estimates page importance by simulating random users who follow links with 85% probability and jump to a random page with 15% probability.
- Implementing iterative algorithms in MapReduce requires chaining multiple separate MapReduce jobs, one per iteration, which is painful and inefficient.