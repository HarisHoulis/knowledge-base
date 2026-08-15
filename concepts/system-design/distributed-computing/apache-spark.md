---
domain: system-design
subdomain: distributed-computing
concept: apache-spark
title: Lecture 15: Big Data: Spark
sources:
  - title: "Lecture 15: Big Data: Spark"
    url: "https://www.youtube.com/watch?v=mzIoSW-cInA"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-14T21:04:47+00:00"
---

# Lecture 15: Big Data: Spark

Spark is presented as an evolutionary successor to MapReduce, generalizing the fixed two-stage map-then-reduce pipeline into a complete notion of multi-step data flow graphs. This generalization gives programmers more flexibility and expressiveness, and gives the system more opportunities for optimization and fault handling. A key benefit is Spark's support for iterative applications, which can loop over the same data much more effectively than MapReduce, where each iteration would require a separate MapReduce application run that reads its input from disk via GFS, causing pain and slowness.

The example of PageRank illustrates these points. PageRank is a well-known algorithm for estimating the importance of web pages based on links. The input is a collection of lines, each containing two URLs: the page containing a link and the link target. The algorithm models a user who has an 85% chance of following a randomly selected link from the current page and a 15% chance of jumping to a random page. Ranks are updated iteratively until convergence, simulating this random-surfer behavior across all pages in parallel. While PageRank can be coded in MapReduce by chaining multiple jobs, Spark's support for iterative data flow makes such algorithms far more natural and efficient.

- Spark generalizes MapReduce's map and reduce stages into arbitrary multi-step data flow graphs, improving expressiveness and optimization potential.
- It provides better support for iterative algorithms, such as PageRank, compared to MapReduce.
- PageRank models a random surfer who follows links with 85% probability and jumps randomly with 15% probability, computing page importance through iteration.
- MapReduce requires multiple chained jobs for iterative algorithms, each reading from GFS/disk, which is slow and inconvenient.
- Spark's ability to keep data in memory across iterations makes it well-suited for data center computations.