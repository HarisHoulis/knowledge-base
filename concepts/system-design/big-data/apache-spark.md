---
domain: system-design
subdomain: big-data
concept: apache-spark
title: Lecture 15: Big Data: Spark
sources:
  - title: "Lecture 15: Big Data: Spark"
    url: "https://www.youtube.com/watch?v=mzIoSW-cInA"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-14T21:04:47+00:00"
---

# Lecture 15: Big Data: Spark

This lecture introduces Apache Spark as an evolutionary successor to MapReduce for data center computations. Spark generalizes the two-stage MapReduce model into a complete notion of multi-step data flow graphs, giving the system more opportunities for optimization and fault handling while providing programmers with a more expressive API. A major advantage is support for iterative applications, such as PageRank, which naturally involve loops over data; in contrast, MapReduce requires chaining multiple jobs, each reading from and writing to disk, making such workflows painful and slow.

The instructor walks through a PageRank example that processes a large collection of web links. PageRank estimates the importance of each page by modeling a random user who, with 85% probability, follows a randomly chosen link from the current page, and with 15% probability jumps to an arbitrary page. The algorithm iteratively updates rank values until they converge. Spark's ability to keep data in memory across iterations eliminates the repeated disk I/O overhead inherent to MapReduce, making it well suited for this and other iterative workloads.

- Spark is a successor to MapReduce, designed for modern data center computations.
- It generalizes map and reduce into multi-step data flow graphs, improving expressiveness and enabling better optimization and fault tolerance.
- Spark natively supports iterative applications like PageRank, which require repeated passes over data, much more effectively than chained MapReduce jobs.
- PageRank models a random surfer with an 85% link-following probability and 15% random jump, iterating until convergence.