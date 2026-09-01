---
domain: system-design
subdomain: distributed-data-processing
concept: spark-dag-dataflow
title: Spark: Successor to MapReduce for Big Data
sources:
  - title: "Lecture 15: Big Data: Spark"
    url: "https://www.youtube.com/watch?v=mzIoSW-cInA"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-14T21:04:47+00:00"
---

# Spark: Successor to MapReduce for Big Data

Spark is presented as a successor to MapReduce and a widely used system for data center computations. Its key evolutionary step is generalizing MapReduce's two-stage map/reduce model into a complete notion of multi-step data flow graphs. This gives the system more opportunities for optimization and fault handling, and it gives programmers a more expressive way to build complex data processing pipelines (MIT 6.824, 2020).

The lecture illustrates Spark's benefits with PageRank, an iterative algorithm that estimates the importance of web pages based on link structure. In MapReduce, iterative algorithms are awkward because each iteration would require a separate MapReduce job. Spark supports iterative applications much better, allowing the user to express loops over data directly and run the PageRank simulation for all pages in parallel until the ranks converge (MIT 6.824, 2020).

- Spark generalizes MapReduce's map/reduce phases into multi-step data flow graphs.
- It is designed for large-scale data center computations and is widely used today.
- Spark provides better support for iterative algorithms like PageRank compared to repeated MapReduce jobs.