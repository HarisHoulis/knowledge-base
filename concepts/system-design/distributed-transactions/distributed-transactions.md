---
domain: system-design
subdomain: distributed-transactions
concept: distributed-transactions
title: Distributed Transactions
sources:
  - title: "Lecture 12: Distributed Transactions"
    url: "https://www.youtube.com/watch?v=aDp99WDIM_4"
    author: "MIT 6.824: Distributed Systems"
    date: "2020-03-18T18:25:20+00:00"
---

# Distributed Transactions

Distributed transactions are essential when data is sharded across multiple servers, and operations require reading or writing data on different servers. The lecture breaks distributed transactions into two implementation pieces: concurrency control and atomic commit. These pieces work together to hide the complexity of splitting data across servers from the application programmer, a concern traditionally addressed by databases but applicable more broadly in distributed systems.

To illustrate, the lecture uses a bank transfer example where account balances for X and Y are on different servers, both starting at 10. A transfer transaction moves money from X to Y, while an audit transaction reads all balances to verify the total remains unchanged. The lecture emphasizes the need to define what results are legal when transactions run concurrently, and then to build machinery that guarantees only those correct outcomes despite concurrency and failures.

The correctness criterion for transactions is introduced via ACID properties: Atomicity, Consistency, Isolation, and Durability. Atomicity ensures a transaction commits or aborts as a single unit; the lecture points to atomic commit as a key mechanism for this. This overview sets the stage for deeper exploration of concurrency control and atomic commit protocols in distributed systems.

According to MIT 6.824 (Lecture 12, 2020), 'distributed transactions come in really to implementation pieces and that's how I'll cover them: concurrency control and atomic commit' (source: https://www.youtube.com/watch?v=aDp99WDIM_4).

- Distributed transactions combine two core components: concurrency control and atomic commit.
- They are motivated by the need to handle operations that span multiple sharded servers.
- ACID properties define correctness: Atomicity, Consistency, Isolation, Durability.
- A bank transfer example shows how transactions must manage data on different servers while maintaining correct results under concurrency.