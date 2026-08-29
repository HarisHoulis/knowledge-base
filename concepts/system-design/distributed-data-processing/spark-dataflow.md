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

Spark is presented as an evolutionary successor to MapReduce, widely used for data-center computations. Unlike MapReduce's fixed map-then-reduce structure, Spark generalizes computation into multi-step dataflow graphs, making it more expressive and giving the system more opportunities for optimization and fault handling [1].

The lecture motivates this with PageRank, a web-page importance algorithm that is naturally iterative. PageRank models a user who, with 85% probability, follows a random link from the current page and, with 15% probability, jumps to another page; the algorithm repeatedly updates each page's rank based on incoming links. In MapReduce, this requires chaining many map/reduce jobs one after another, which is painful and slow. Spark is designed to support such iterative applications more conveniently and effectively [1].

- Spark is a widely used successor to MapReduce, designed for data-center-scale computations.
- It generalizes MapReduce's two stages into multi-step dataflow graphs, enabling better optimization and fault handling.
- Iterative algorithms like PageRank are awkward in MapReduce because each iteration requires a separate chained job.
- PageRank estimates page importance by simulating a random user who follows links 85% of the time and jumps randomly 15% of the time.