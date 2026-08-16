---
domain: system-design
subdomain: distributed-data-processing
concept: spark-vs-mapreduce
title: Lecture 15: Big Data: Spark
sources:
  - title: "Lecture 15: Big Data: Spark"
    url: "https://www.youtube.com/watch?v=mzIoSW-cInA"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-14T21:04:47+00:00"
---

# Lecture 15: Big Data: Spark

Spark is presented as a successor to MapReduce, evolving it from a fixed two-stage map-then-reduce model into a general multi-step dataflow graph. This generalization makes Spark more expressive for programmers and gives the system more opportunities for optimization and fault handling. It also supports iterative applications much more naturally than MapReduce, which typically requires chaining multiple separate MapReduce jobs (MIT 6.824 Lecture 15).

The lecture uses PageRank as an example. The input is a large collection of lines, each containing two URLs: the page containing a link and the link target. PageRank models a user who, with 85% probability, follows a randomly selected link from the current page and, with 15% probability, jumps to an arbitrary page. The algorithm iteratively propagates page importance along links until ranks converge. While PageRank can be implemented with repeated MapReduce jobs, each job reads input from disk (e.g., GFS), making it slow and cumbersome. Spark's support for in-memory iterative computation makes such workloads significantly more convenient and efficient (MIT 6.824 Lecture 15).

- Spark generalizes MapReduce into multi-step dataflow graphs, improving expressiveness and optimization opportunities.
- Spark is better suited than MapReduce for iterative algorithms like PageRank, which require repeated passes over the data.
- PageRank estimates page importance by simulating users who follow links 85% of the time and jump randomly 15% of the time.
- A naive MapReduce implementation of PageRank is painful because each iteration must be a separate job that reads from disk, e.g., GFS.