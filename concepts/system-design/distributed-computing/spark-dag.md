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

The lecture highlights Spark's advantage for iterative applications, using PageRank as a motivating example. PageRank involves a loop that must run many times, and while it can be cobbled together with multiple MapReduce applications, doing so is painful and slow. Spark's DAG-based model makes such iterative computations much more convenient and efficient (MIT 6.824, 2020).

- Spark generalizes MapReduce's two stages into a multi-step data flow graph, improving expressiveness and optimization potential.
- Iterative algorithms like PageRank are much better supported in Spark than in MapReduce, which requires chaining multiple MapReduce jobs.
- PageRank models a user who follows links with 85% probability and jumps to a random page with 15% probability, updating page ranks iteratively.
- The source text does not yet cover RDD internals, but frames Spark as an evolutionary step for large-scale data processing.