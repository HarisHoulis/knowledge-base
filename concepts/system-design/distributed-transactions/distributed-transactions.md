---
domain: system-design
subdomain: distributed-transactions
concept: distributed-transactions
title: Lecture 12: Distributed Transactions
sources:
  - title: "Lecture 12: Distributed Transactions"
    url: "https://www.youtube.com/watch?v=aDp99WDIM_4"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-18T18:25:20+00:00"
---

# Lecture 12: Distributed Transactions

Distributed transactions are essential when data is sharded across multiple servers, such as a bank splitting customer balances across machines or a website distributing vote counts. In such systems, a single logical operation (e.g., transferring money between accounts) may require reading and writing data on several servers, making it challenging to maintain consistency and atomicity. The lecture introduces transactions as the standard abstraction to hide this complexity from application programmers, who mark the beginning and end of a transaction (e.g., BEGIN TRANSACTION and COMMIT) to group a set of operations into a single atomic unit (MIT 6.824, 2020).

- Distributed transactions arise from sharding data across servers, requiring coordination for multi-server operations.
- A transaction combines two main implementation pieces: concurrency control and atomic commit.
- The programmer marks transaction boundaries, and the system guarantees ACID properties (notably atomicity).
- Example: a transfer transaction from account X to Y and an audit transaction that checks total balance must execute correctly even concurrently.