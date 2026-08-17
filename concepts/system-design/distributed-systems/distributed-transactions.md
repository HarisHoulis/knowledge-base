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

Distributed transactions are necessary when data is sharded across multiple servers and a single logical operation must read or write data on more than one server. As discussed in MIT 6.824 Lecture 12, they consist of two main implementation pieces: concurrency control and atomic commit. The lecture motivates the need with a bank transfer example, where moving money between accounts requires atomically modifying balances that may reside on different servers. The transaction abstraction hides this complexity from the programmer by marking the beginning and end of a sequence of operations, with the system providing guarantees about correctness despite concurrency and failures. The standard correctness notion is ACID—atomicity, consistency, isolation, and durability—which ensures that transactions execute as if they were serialized and are not split by failures or other concurrent activity.

- Distributed transactions combine concurrency control and atomic commit to manage operations that span multiple servers.
- Sharding data for load or space requires transactions when operations touch multiple shards (e.g., bank transfers).
- The transaction abstraction lets programmers mark begin/end, and the system guarantees ACID properties.
- Concurrency control ensures isolation; atomic commit ensures all servers agree on the final outcome even under failures.