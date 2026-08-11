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

Distributed transactions are essential when data is partitioned across many servers. For example, a bank may split customer balances across servers, so a transfer from one account to another requires reading and writing data on two different servers. The goal is to hide this complexity from the application programmer by providing a transaction abstraction that groups operations into a single unit (MIT 6.824, 2020).

Transactions provide ACID guarantees, beginning with atomicity. Concurrency control and atomic commit are the two major implementation pieces. Concurrency control ensures serializability when multiple transactions run concurrently, while atomic commit ensures that either all servers commit or none do, even in the presence of failures (MIT 6.824, 2020).

Using a bank transfer and an audit as examples, the lecture illustrates that legal results require both transactions to appear as if they executed one-at-a-time. This motivates the need for careful scheduling and commit protocols (MIT 6.824, 2020).

- Sharding data across servers makes distributed transactions necessary for operations that span multiple servers.
- The transaction abstraction hides complexity from application programmers by grouping operations into a single unit.
- Distributed transactions involve two key components: concurrency control and atomic commit.
- ACID properties, especially atomicity and isolation, are central to correct transaction behavior.
- Examples like bank transfers and audits demonstrate the need for serializability even with concurrent transactions.