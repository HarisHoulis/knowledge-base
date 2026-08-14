---
domain: system-design
subdomain: big-data-processing
concept: spark
title: Lecture 15: Big Data: Spark
sources:
  - title: "Lecture 15: Big Data: Spark"
    url: "https://www.youtube.com/watch?v=mzIoSW-cInA"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-04-14T21:04:47+00:00"
---

# Lecture 15: Big Data: Spark

Spark is presented as a successor to MapReduce for data-center computations. It generalizes MapReduce's two stages into multi-step dataflow graphs, giving programmers more expressive power and the system more opportunities for optimization and fault handling. Spark also supports iterative applications much more effectively than MapReduce, which would require chaining many separate MapReduce jobs.

As an example, the lecture walks through PageRank, an iterative algorithm for estimating web page importance. The input is a large collection of link records, each line containing a source URL and a target URL. The algorithm models a random user who 85% of the time follows a link and 15% of the time jumps to an arbitrary page, repeatedly propagating importance from pages to their linked pages until convergence. In Spark this is a natural loop over the data; in MapReduce it would be awkward and slow because each iteration would need its own map-reduce pass. (MIT 6.824, 2020).

- Spark generalizes MapReduce into a complete multi-step dataflow graph, making it more flexible and easier to optimize.
- It was designed as an evolutionary successor to MapReduce and is widely used for large-scale data center computations.
- Iterative algorithms like PageRank are far more natural and efficient in Spark than in repeated MapReduce jobs.
- PageRank estimates page importance by modeling a random user who follows links with 85% probability and switches to a random page with 15% probability.
- The input to Spark's PageRank is a giant set of lines, each representing a link from one URL to another.