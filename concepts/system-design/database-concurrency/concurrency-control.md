---
domain: system-design
subdomain: database-concurrency
concept: concurrency-control
title: How Databases Keep Their Sanity with Concurrency Control
sources:
  - title: "How Databases Keep Their Sanity with Concurrency Control"
    url: "https://blog.bytebytego.com/p/how-databases-keep-their-sanity-with"
    author: "ByteByteGo"
    date: "Thu, 03 Sep 2026 15:31:17 GMT"
---

# How Databases Keep Their Sanity with Concurrency Control

Database concurrency control addresses bugs that occur when multiple transactions overlap in time, such as the bank account example where two withdrawals of $10 each from $100 leave a balance of $90 instead of $80. The article identifies four concurrency anomalies: lost update, dirty read, non-repeatable read, and phantom read. These arise because a transaction reads a value, does work, and writes it back while another transaction modifies the same data in between (ByteByteGo).

- Lost updates, dirty reads, non-repeatable reads, and phantom reads are the four main ways overlapping transactions corrupt data or produce inconsistent results.
- Pessimistic locking uses SELECT ... FOR UPDATE to block concurrent writers until the first transaction commits, but can lower throughput and cause deadlocks.
- Optimistic locking uses version numbers to detect stale updates and retry conflicting transactions, making it suitable when conflicts are rare.
- MVCC (Multi-Version Concurrency Control) creates new row versions on update and lets each transaction read a consistent snapshot, so readers and writers never block each other.