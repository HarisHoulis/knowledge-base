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

The lecture introduces distributed transactions, which arise when data is sharded across multiple servers and operations need to read or modify data on more than one server. It identifies two core implementation pieces: concurrency control and atomic commit. These are packaged into the abstraction of a transaction, which provides ACID guarantees (atomicity, consistency, isolation, durability) so application programmers can treat a sequence of operations as a single unit.

- Distributed transactions are necessary when data is split across servers and an operation touches multiple shards.
- The two main components are concurrency control (managing simultaneous transactions) and atomic commit (ensuring all-or-nothing execution across servers).
- ACID properties define correctness: atomicity, consistency, isolation, and durability.
- The lecture uses a bank transfer example to illustrate how concurrent transactions must produce results equivalent to some serial execution.