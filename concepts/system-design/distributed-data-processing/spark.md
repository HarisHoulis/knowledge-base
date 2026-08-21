---
domain: system-design
subdomain: distributed-data-processing
concept: spark
title: Lecture 15: Big Data: Spark
sources:
  - title: "Lecture 15: Big Data: Spark"
    url: "https://www.youtube.com/watch?v=mzIoSW-cInA"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-14T21:04:47+00:00"
---

# Lecture 15: Big Data: Spark

Spark is presented as an evolutionary successor to MapReduce and is widely used for data-center computations. It generalizes MapReduce's two fixed stages into a more complete notion of multi-step dataflow graphs. This improves expressiveness for programmers and gives the system more opportunities for optimization and fault handling (MIT 6.824, 2020).

- Spark generalizes MapReduce from single map/reduce steps into multi-step dataflow graphs.
- It is better suited than MapReduce for iterative algorithms like PageRank.
- PageRank estimates page importance by modeling a random surfer who follows links 85% of the time and jumps to a random page 15% of the time.
- Implementing iterative PageRank with MapReduce requires chaining many jobs, each reading from disk, which is painful and slow.
- Spark's design supports in-memory multi-stage workflows, making iterative and interactive workloads practical.