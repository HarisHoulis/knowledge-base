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

Spark is presented as a successor to MapReduce, generalizing its fixed map and reduce stages into a complete notion of multi-step data flow graphs. This generality gives programmers more expressive power and gives the Spark system more opportunities for optimization and fault handling. A key benefit is much better support for iterative applications compared to MapReduce, where algorithms like PageRank are painful to implement as multiple sequential MapReduce jobs and slow because each job reads its input from disk. The lecture illustrates Spark with a PageRank example: input is a large collection of lines, each containing a source URL and a target URL, representing web links. PageRank estimates page importance by simulating a user who has an 85% chance of following a randomly selected link from the current page and a 15% chance of jumping to an arbitrary page. Over many iterations, these ranks converge. Spark's in-memory, directed data flow graph allows this iteration to run much more efficiently than chaining MapReduce applications.

- Spark generalizes MapReduce's map/reduce stages into multi-step data flow graphs.
- Spark is especially suited to iterative algorithms like PageRank that require repeated passes over the data.
- PageRank models a user who follows links with 85% probability and jumps randomly with 15% probability.
- Compared to chained MapReduce jobs, Spark gives the system more room for optimization and fault handling.
- The PageRank example input is a collection of source-URL/target-URL link lines.