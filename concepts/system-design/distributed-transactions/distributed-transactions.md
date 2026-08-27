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

This lecture from MIT 6.824 introduces distributed transactions, which are essential when data is sharded across multiple servers. For instance, a bank might split customer balances across servers, yet a transfer between accounts on different servers requires coordinated read/write operations. Distributed transactions combine two key pieces: concurrency control and atomic commit, to provide the appearance of a single, reliable unit of work despite distribution and failures.

- Distributed transactions are built from two main components: concurrency control and atomic commit.
- Transactions allow programmers to group operations (reads/writes) into a single unit with ACID guarantees.
- Example: transferring $1 from account X to Y while an audit transaction reads both balances illustrates the need for atomicity and isolation.
- Sharding data across servers for scalability creates the need for distributed transaction coordination.