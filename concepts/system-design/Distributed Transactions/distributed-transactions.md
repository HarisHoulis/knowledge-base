---
domain: system-design
subdomain: Distributed Transactions
concept: distributed-transactions
title: Lecture 12: Distributed Transactions
sources:
  - title: "Lecture 12: Distributed Transactions"
    url: "https://www.youtube.com/watch?v=aDp99WDIM_4"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-18T18:25:20+00:00"
---

# Lecture 12: Distributed Transactions

The lecture introduces distributed transactions, which arise when data is split or sharded across many servers. For example, a bank may store balances for half its customers on one server and the other half on another, so a transfer between accounts on different servers requires reading and writing data on multiple servers. The goal is to hide this complexity from application programmers, a traditional database concern that applies broadly to distributed systems (MIT 6.824, 2020).

Distributed transaction implementation is broken into two main pieces: concurrency control and atomic commit. Concurrency control manages simultaneous transactions, while atomic commit ensures that a transaction's operations are applied as a single unit despite failures. Transactions are the abstraction that packages these concerns; the programmer marks the beginning and end of a sequence of operations, and the transaction processing system provides guarantees about what happens between those marks (MIT 6.824, 2020).

Correctness is defined via the ACID properties, with atomicity meaning a transaction's operations are treated as an indivisible unit. The lecture illustrates these concepts with a bank transfer transaction that moves money from account X to account Y and a read-only audit transaction that checks the total balance remains unchanged. Legal results from concurrently running these transactions must preserve the invariant that money is neither created nor destroyed (MIT 6.824, 2020).

- Distributed transactions are necessary when data is sharded across servers and a single operation touches multiple servers.
- Two key implementation components are concurrency control and atomic commit.
- Transactions provide an abstraction where programmers mark a begin and end, and the system guarantees ACID properties.
- Atomicity ensures the transaction's operations are applied as a single unit, even across failures.
- The bank transfer and audit example shows how transactions preserve invariants like total balance.