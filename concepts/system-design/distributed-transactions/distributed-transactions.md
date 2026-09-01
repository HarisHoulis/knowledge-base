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

Distributed transactions are necessary when data is sharded across many servers, such as bank balances split across servers, and an operation like a transfer must read and write data on multiple servers. The lecture frames distributed transactions as composed of two main implementation pieces: concurrency control and atomic commit. Concurrency control manages interleaving of concurrent transactions to preserve correctness, while atomic commit ensures that all participating servers agree on the outcome even in the presence of failures.

- Distributed transactions are motivated by systems that shard data across multiple servers, requiring operations that span multiple machines.
- The two major building blocks are concurrency control and atomic commit.
- Transactions provide ACID semantics, with atomicity ensuring that a transaction's operations are treated as a single unit.
- The bank transfer example illustrates a transaction that modifies balances on potentially different servers, while an audit transaction reads all balances to verify the total is unchanged.
- Correct execution must account for both concurrent execution and failures, ensuring only legal results are produced.