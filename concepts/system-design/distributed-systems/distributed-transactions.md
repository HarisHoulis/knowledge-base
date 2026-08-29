---
domain: system-design
subdomain: distributed-systems
concept: distributed-transactions
title: Distributed Transactions (MIT 6.824 Lecture 12)
sources:
  - title: "Lecture 12: Distributed Transactions"
    url: "https://www.youtube.com/watch?v=aDp99WDIM_4"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-18T18:25:20+00:00"
---

# Distributed Transactions (MIT 6.824 Lecture 12)

Distributed transactions arise when data is sharded across multiple servers, so operations must read or modify data on different servers. The lecture introduces transactions as an abstraction that combines concurrency control and atomic commit, hiding the complexity of splitting data from the application programmer. A bank transfer example illustrates two concurrent transactions: a transfer that updates balances on two servers and an audit that reads all balances. The correctness of such concurrent executions is defined by ACID properties, with atomicity ensuring all-or-nothing execution and isolation preventing interference between transactions.

- Distributed transactions are needed when data is split/sharded across servers and an operation must touch multiple servers.
- Transactions consist of two main pieces: concurrency control and atomic commit.
- Programmers mark transaction boundaries; the system provides guarantees like atomicity and isolation (ACID).
- The example of a bank transfer and an audit demonstrates the correctness challenges of concurrent transactions.