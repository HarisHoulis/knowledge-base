---
domain: system-design
subdomain: distributed-systems
concept: distributed-transactions
title: Lecture 12: Distributed Transactions
sources:
  - title: "Lecture 12: Distributed Transactions"
    url: "https://www.youtube.com/watch?v=aDp99WDIM_4"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-18T18:25:20+00:00"
---

# Lecture 12: Distributed Transactions

The MIT 6.824 lecture introduces distributed transactions as a way to handle operations that span multiple servers when data is sharded or split across machines. A common example is a bank where customer balances are stored on different servers; a transfer between accounts requires reading and writing data on two servers, which demands coordination [1]. The lecture breaks distributed transactions into two core implementation pieces: concurrency control and atomic commit. Concurrency control ensures that concurrent transactions do not interfere improperly, while atomic commit ensures that all servers either commit or abort the transaction together [1]. The transaction abstraction allows programmers to mark a beginning and end to a sequence of operations, providing guarantees like atomicity. The lecture illustrates this with a transfer transaction (T1) that moves money between accounts and an audit transaction (T2) that reads all balances to verify the total is unchanged. Correctness for such concurrent executions is a central theme; the lecture sets up the problem of determining legal results and building mechanisms to execute transactions correctly despite concurrency and failures [1].

- Distributed transactions are necessary when data is sharded across multiple servers and a single logical operation touches multiple servers.
- Two main implementation components are concurrency control and atomic commit.
- The transaction abstraction lets programmers define a unit of work with a beginning and end, providing guarantees such as atomicity.
- A motivating example is a bank transfer where the two accounts reside on different servers, requiring coordinated updates.
- Correct execution must handle both concurrency (e.g., concurrent transfers and audits) and failures.