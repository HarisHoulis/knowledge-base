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

Distributed transactions are necessary when data is sharded across multiple servers, such as bank balances split across servers to balance load and storage. A transaction allows a programmer to group multiple read and write operations into a single logical unit, marked with begin and end, so that operations like a bank transfer affecting records on different servers are handled atomically and in isolation from other concurrent activities (MIT 6.824, 2020).

The lecture breaks distributed transactions into two core implementation pieces: concurrency control and atomic commit. Correctness is defined in terms of ACID properties, with atomicity ensuring all-or-nothing execution and concurrency control managing isolation between transactions. Using an example of a transfer transaction and an audit transaction reading both balances, the lecture illustrates how the system must produce only legal outcomes despite concurrency and failures (MIT 6.824, 2020).

- Distributed transactions handle operations that span data sharded across multiple servers.
- Transactions are built from two main pieces: concurrency control and atomic commit.
- ACID properties, especially atomicity and isolation, define correctness for distributed transactions.
- The transaction abstraction hides sharding complexity from application programmers by using begin/end markers.