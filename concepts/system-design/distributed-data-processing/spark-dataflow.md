---
domain: system-design
subdomain: distributed-data-processing
concept: spark-dataflow
title: Big Data: Spark
sources:
  - title: "Lecture 15: Big Data: Spark"
    url: "https://www.youtube.com/watch?v=mzIoSW-cInA"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-14T21:04:47+00:00"
---

# Big Data: Spark

Spark is presented as an evolutionary successor to MapReduce, generalizing the strict two-stage map-then-reduce model into flexible multi-step data flow graphs. This generalization improves programmer expressiveness and gives the system more opportunities for optimization and fault handling compared to chaining multiple MapReduce jobs [1]. A key advantage is support for iterative applications, such as PageRank, which MapReduce handles poorly because each iteration requires launching a separate MapReduce job [1].

- Spark generalizes MapReduce's two stages into arbitrary multi-step data flow graphs, enabling more expressive programming and better optimization [1].
- It is specifically designed to support iterative algorithms like PageRank more efficiently than repeated MapReduce jobs [1].
- PageRank is modeled as a random surfer who follows links with 85% probability and jumps to a random page with 15% probability, iteratively converging on page importance scores [1].
- The input to PageRank is a large collection of URL pairs representing web links, processed in parallel across pages [1].