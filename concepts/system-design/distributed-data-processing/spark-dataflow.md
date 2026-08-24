---
domain: system-design
subdomain: distributed-data-processing
concept: spark-dataflow
title: Lecture 15: Big Data: Spark
sources:
  - title: "Lecture 15: Big Data: Spark"
    url: "https://www.youtube.com/watch?v=mzIoSW-cInA"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-14T21:04:47+00:00"
---

# Lecture 15: Big Data: Spark

Spark is presented as an evolutionary successor to MapReduce for large-scale data-center computations. It generalizes MapReduce's two fixed stages into flexible multi-step data-flow graphs, which improves programmer expressiveness and gives the system more opportunities for optimization and fault handling (MIT 6.824, 2020).

- Spark generalizes MapReduce's map and reduce stages into multi-step data-flow graphs.
- This design enables better optimization and fault tolerance compared to classic MapReduce.
- Spark supports iterative applications much more naturally than chained MapReduce jobs.
- PageRank is used as an example: it requires repeated iteration over the web graph, which is painful with MapReduce.
- PageRank models a random surfer and iteratively updates page importance until convergence.