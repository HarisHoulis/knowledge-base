---
domain: system-design
subdomain: distributed-computing
concept: spark-dag
title: Lecture 15: Big Data: Spark
sources:
  - title: "Lecture 15: Big Data: Spark"
    url: "https://www.youtube.com/watch?v=mzIoSW-cInA"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-14T21:04:47+00:00"
---

# Lecture 15: Big Data: Spark

Spark is presented as a successor to MapReduce, evolving from the rigid two-stage map-reduce model into a general framework for multi-step data flow graphs. This generalization gives programmers more expressive power and gives the system more opportunities for optimization and fault handling, while also making iterative applications like PageRank much more convenient than chaining multiple MapReduce jobs together.

The lecture uses PageRank as a running example to illustrate Spark's advantages. PageRank estimates the importance of web pages by simulating a random user following links, with a damping factor for jumping to random pages. This requires repeated iterations over a large web graph. In MapReduce, each iteration would require separate jobs reading and writing from disk, which is slow and cumbersome. Spark's in-memory data abstractions and lazy evaluation make such iterative algorithms natural and efficient.

Spark's design centers on resilient distributed datasets (RDDs) and a directed acyclic graph (DAG) of transformations and actions. By representing the entire computation as a graph, Spark can optimize execution, recover from failures by recomputing lost RDD partitions, and support applications that reuse data across multiple steps. The lecture highlights that this is both a programmer convenience and a system-level capability that goes beyond MapReduce. (Sources: MIT 6.824 Lecture 15, 2020)

- Spark generalizes MapReduce's map and reduce into multi-step data flow graphs, improving expressiveness and enabling optimization.
- Iterative algorithms like PageRank are much easier to implement in Spark than with multiple MapReduce jobs.
- Spark's RDDs can be cached in memory, avoiding repeated disk I/O across iterations.
- The DAG execution model aids recovery by recomputing lost partitions instead of relying on checkpointing.
- PageRank example demonstrates how Spark handles a loop over a large distributed web graph.