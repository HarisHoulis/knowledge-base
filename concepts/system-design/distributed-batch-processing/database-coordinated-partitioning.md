---
domain: system-design
subdomain: distributed-batch-processing
concept: database-coordinated-partitioning
title: Distributed Spring Batch Without a Message Broker
sources:
  - title: "Distributed Spring Batch Without a Message Broker"
    url: "https://www.infoq.com/articles/spring-batch-without-broker/"
    author: "Janardhan Reddy Chejarla"
    date: "2026-10-21"
---

# Distributed Spring Batch Without a Message Broker

Spring Batch's partitioned processing already requires a shared, persistent job repository; this article proposes using that same database as the entire coordination plane, eliminating the message broker. Work is sized dynamically to the live node count rather than a fixed partition count, and each job elects a per-job master instead of relying on a standing coordinator process.

Correctness under concurrency is handled with compare-and-set claiming of partitions, which prevents two workers from executing the same partition. Failure detection uses a two-phase heartbeat mechanism so that orphaned partitions can be reassigned when a node dies.

The author is explicit that the broker-free design is not universally superior: a message broker remains the right choice in scenarios where its delivery guarantees, decoupling, or throughput characteristics are needed. The approach trades broker infrastructure for tighter coupling to the database as a single coordination point.

- The shared job repository database doubles as the coordination plane, removing the need for a message broker.
- Partition count is sized to the live node count rather than fixed in advance.
- A per-job master is elected dynamically, avoiding a standing coordinator.
- Compare-and-set claiming prevents double-execution of partitions.
- Two-phase heartbeats drive failover; a broker is still appropriate in some cases.