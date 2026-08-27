---
domain: system-design
subdomain: distributed-computing
concept: spark-dataflow
title: Lecture 15: Big Data: Spark
sources:
  - title: "Lecture 15: Big Data: Spark"
    url: "https://www.youtube.com/watch?v=mzIoSW-cInA"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-14T21:04:47+00:00"
---

# Lecture 15: Big Data: Spark

Spark is presented as a successor to MapReduce, evolving the two-stage map-reduce model into a general multi-step data flow graph. This generalization gives the system more room for optimization and better handling of failures, while also making the programming model more expressive for developers (MIT 6.824, 2020).

- Spark generalizes MapReduce's two stages into a complete notion of multi-step data flow graphs, enabling optimizations and fault tolerance.
- Spark supports iterative applications much better than MapReduce, which requires chaining multiple jobs for each iteration.
- PageRank is used as an example of a widely used algorithm that is painful to implement in MapReduce but natural in Spark, as it iteratively updates page ranks by simulating random user clicks.
- The input to Spark's PageRank example is a large collection of lines, each representing a web link with source and destination URLs, and the algorithm converges ranks through repeated parallel updates.