---
domain: system-design
subdomain: distributed-data-processing
concept: spark-dag-iterative
title: Big Data: Spark
sources:
  - title: "Lecture 15: Big Data: Spark"
    url: "https://www.youtube.com/watch?v=mzIoSW-cInA"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-14T21:04:47+00:00"
---

# Big Data: Spark

Spark is presented as a successor to MapReduce that generalizes the two-stage map-reduce model into multi-step dataflow graphs (MIT 6.824, 2020). This makes it more expressive for programmers and gives the system more opportunities for optimization and fault handling. Spark is widely used for data center computations and better supports iterative applications than MapReduce (MIT 6.824, 2020).

- Spark generalizes MapReduce into multi-step dataflow graphs, improving expressiveness and enabling system optimizations.
- Spark is better suited than MapReduce for iterative algorithms because it can loop over data effectively.
- PageRank is used as an example: it requires repeated iteration, which is cumbersome to implement with multiple chained MapReduce jobs.
- PageRank models a user following links with 85% probability and randomly jumping with 15% probability, updating page ranks iteratively until convergence.