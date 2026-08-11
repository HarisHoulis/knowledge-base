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

This lecture introduces Apache Spark as a successor to MapReduce, emphasizing its role in generalizing the two-stage map-reduce model into a complete notion of multi-step data flow graphs. This generalization provides more expressiveness for programmers and gives the system more opportunities for optimization and fault handling. Spark is particularly well-suited for iterative applications such as PageRank, which involve repeated loops over data, a scenario that is cumbersome to implement using multiple chained MapReduce jobs (MIT 6.824 Lecture 15).

The PageRank example illustrates how Spark handles iterative computations. Input consists of lines representing links between URLs. PageRank models the probability that a random user clicking links will land on a page: 85% chance of following a link from the current page and 15% chance of jumping to a random page. Ranks are updated iteratively by propagating importance from source pages to target pages. With MapReduce, each iteration would require a separate job, making the process painful and slow; Spark enables a single efficient iterative workflow for such algorithms (MIT 6.824 Lecture 15).

- Spark generalizes MapReduce by supporting multi-step data flow graphs, improving flexibility and optimization opportunities.
- Spark is designed to handle iterative algorithms like PageRank efficiently, whereas MapReduce requires chaining multiple jobs.
- PageRank estimates page importance by simulating random link-following with a damping factor (85% follow links, 15% random jump).
- Spark's abstraction provides more expressiveness for programmers compared to MapReduce.