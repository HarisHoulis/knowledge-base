---
domain: system-design
subdomain: cell-based-architecture
concept: cell-based-architecture
title: Built for Reliability: How American Express Processes Payments at Scale
sources:
  - title: "Built for Reliability: How American Express Processes Payments at Scale"
    url: "https://blog.bytebytego.com/p/built-for-reliability-how-american"
    author: "ByteByteGo"
    date: "2026-09-08"
---

# Built for Reliability: How American Express Processes Payments at Scale

The article explains how American Express processes card payments at scale using a cell-based architecture. A cell is a complete, self-sufficient copy of the payment processing stack—including microservices, databases, DNS, and infrastructure—deployed independently and forming a single failure domain. This isolation ensures problems inside a cell stay inside, and cells can be pulled out of rotation without affecting the rest of the platform. Crucially, cells avoid synchronous cross-cell dependencies in the critical path, which keeps them loosely coupled and resilient (ByteByteGo, 2026).

To maintain data locality, American Express pushes immutable and semi-static reference data (e.g., exchange rates, merchant category codes) to every cell ahead of time, avoiding cold caches and synchronous lookups outside the cell. For dynamic data, which changes with every transaction, the platform inverts the problem: rather than moving data to the transaction, it moves the transaction to the data using deterministic routing based on attributes like partner, market, and payment type. This routing is performed by the Global Transaction Router, which also enforces cell boundaries by acting as the sole path for all inter-cell and external traffic. The router is deliberately simple, stateless, and has minimal dependencies, so it does not become a centralized bottleneck (ByteByteGo, 2026).

When a mid-transaction failure occurs, an orchestrator detects the failure, halts processing, and sends the transaction back to the Global Transaction Router. The router selects a healthy cell, and processing restarts from the beginning using the original transaction data—discarding all partial work. This avoids the need for shared state between cells, which would introduce synchronization and consistency risks. The design prioritizes loose coupling and isolation over resumability, ensuring that failures are contained and payments continue processing even when services are down (ByteByteGo, 2026).

- Cells are self-contained failure domains, each with its own services, databases, and infrastructure, with no synchronous cross-cell calls in the critical path.
- Reference data is proactively pushed to cells to avoid cold caches and out-of-cell lookups; dynamic data is handled by deterministically routing transactions to the cell that already holds the data.
- The Global Transaction Router is the single chokepoint for traffic and is kept simple, stateless, and free of business logic to remain reliable.
- Mid-transaction failures are handled by restarting the entire transaction in a healthy cell from scratch, discarding partial work to preserve cell independence.