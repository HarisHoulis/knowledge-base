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

The lecture introduces distributed transactions, which arise when data is sharded across multiple servers. It presents a bank transfer example where balances for different customers reside on different servers, requiring updates to multiple records atomically. The core components of distributed transaction processing are concurrency control and atomic commit. Concurrency control ensures that concurrent transactions do not interfere, while atomic commit guarantees that either all servers agree to commit or all abort, even in the presence of failures. The lecture frames the problem using the ACID properties, starting with atomicity, and emphasizes that these concepts originated in databases but are widely applicable to distributed systems in general.

- Distributed transactions are needed when operations touch data on multiple sharded servers.
- Two key implementation pieces: concurrency control and atomic commit.
- The transaction abstraction lets programmers mark begin/end and guarantees atomicity and isolation.
- ACID provides a correctness standard for running transactions despite concurrency and failures.