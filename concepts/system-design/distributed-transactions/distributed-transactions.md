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

Distributed transactions address the challenge of coordinating operations that span multiple servers, often because data is sharded across them for load and space reasons. The lecture introduces two key implementation pieces: concurrency control and atomic commit. Concurrency control ensures that concurrent transactions do not interfere in ways that produce incorrect results, while atomic commit guarantees that all servers either commit or abort a transaction together, even in the presence of failures. This is essential for operations like bank transfers where balances might reside on different servers (MIT 6.824, 2020).

The lecture uses a bank transfer and an audit transaction to illustrate correctness. Transactions are marked with begin and end, and their execution must adhere to ACID properties, starting with atomicity. The bank transfer example shows that a transfer from one account to another must be atomic, so that the total money remains consistent, and the audit transaction must see a consistent snapshot of balances even if it runs concurrently with the transfer (MIT 6.824, 2020).

- Distributed transactions arise when data is sharded across multiple servers, requiring operations to read/write on multiple servers atomically.
- Two main building blocks: concurrency control (for isolation) and atomic commit (for all-or-nothing behavior across servers).
- ACID properties define correctness; atomicity ensures transactions are indivisible units.
- Bank transfer example: moving money between accounts on different servers must be atomic, and concurrent audits must see consistent balances.
- Transactions require explicit begin/end markers from the programmer to define the scope.