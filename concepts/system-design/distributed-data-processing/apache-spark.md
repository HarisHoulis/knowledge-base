---
domain: system-design
subdomain: distributed-data-processing
concept: apache-spark
title: Lecture 15: Big Data: Spark
sources:
  - title: "Lecture 15: Big Data: Spark"
    url: "https://www.youtube.com/watch?v=mzIoSW-cInA"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-14T21:04:47+00:00"
---

# Lecture 15: Big Data: Spark

Apache Spark is presented as a successor to MapReduce, offering an evolutionary step that generalizes the fixed two-stage map-then-reduce model into a flexible multi-step dataflow graph. This generalization improves expressiveness for programmers and gives the system more opportunities for optimization and fault handling. Spark is particularly well-suited for iterative applications, which are awkward to implement with multiple chained MapReduce jobs.

The lecture illustrates Spark's benefits using PageRank, an iterative algorithm that estimates the importance of web pages based on link structure. In MapReduce, PageRank requires multiple sequential jobs, each representing one iteration, which is cumbersome and slow due to repeated disk I/O. Spark's ability to keep data in memory and express loops directly makes such algorithms much more convenient and efficient.

- Spark generalizes MapReduce's fixed map-reduce phases into arbitrary multi-step dataflow graphs.
- This design enhances both programmer flexibility and system optimization, including fault tolerance.
- Spark natively supports iterative algorithms like PageRank, avoiding the need for chaining multiple MapReduce jobs.
- PageRank models a random surfer who follows links with 85% probability and jumps to a random page with 15%, updating page importance iteratively.