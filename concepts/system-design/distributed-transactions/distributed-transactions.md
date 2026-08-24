---
domain: system-design
subdomain: distributed-transactions
concept: distributed-transactions
title: Lecture 12: Distributed Transactions
sources:
  - title: "Lecture 12: Distributed Transactions"
    url: "https://www.youtube.com/watch?v=aDp99WDIM_4"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-18"
---

# Lecture 12: Distributed Transactions

Distributed transactions are essential when data is sharded across multiple servers, as operations like bank transfers may need to modify records on different servers atomically (MIT 6.824, 2020). The lecture breaks distributed transactions into two main implementation pieces: concurrency control and atomic commit. Concurrency control ensures that concurrent transactions do not interfere, while atomic commit guarantees that all participants either commit or abort together, even in the presence of failures.

The lecture illustrates the need for transactions with a bank transfer example: transferring money from account X to account Y requires updating two records that may reside on different servers. Programmers mark the beginning and end of a transaction, and the transaction processing system provides guarantees such as atomicity and isolation. The correctness of transactions is defined by ACID properties (Atomicity, Consistency, Isolation, Durability), which ensure that concurrent executions produce results equivalent to some serial execution (MIT 6.824, 2020).

- Distributed transactions require both concurrency control and atomic commit.
- Sharding data across servers motivates the need for transactions spanning multiple nodes.
- Transactions let programmers group operations into an atomic unit with begin/end markers.
- ACID properties define correctness for concurrent and failure-prone executions.