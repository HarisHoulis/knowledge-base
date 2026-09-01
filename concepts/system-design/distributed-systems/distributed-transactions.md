---
domain: system-design
subdomain: distributed-systems
concept: distributed-transactions
title: Distributed Transactions
sources:
  - title: "Lecture 12: Distributed Transactions"
    url: "https://www.youtube.com/watch?v=aDp99WDIM_4"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-18T18:25:20+00:00"
---

# Distributed Transactions

Distributed transactions are essential when data is sharded across multiple servers, as operations may need to read or write data on different servers. The lecture explains that large datasets are often split across servers to balance load and storage, but this introduces complexity for operations that span multiple servers. Transactions provide an abstraction that hides this complexity from application programmers by allowing them to mark a sequence of operations as a single unit, ensuring atomicity and isolation despite concurrency and failures (MIT 6.824, 2020).

- Distributed transactions combine concurrency control and atomic commit to handle multi-server operations.
- Sharding data across servers for load and space reasons makes transactions necessary for cross-server operations.
- Transactions offer a way to encapsulate multiple operations as a single atomic unit, hiding distribution complexity.
- The bank transfer/audit example illustrates how concurrent transactions must ensure consistency (e.g., total balance invariant).
- Correctness is defined by guarantees such as ACID atomicity, even in the presence of concurrency and failures.