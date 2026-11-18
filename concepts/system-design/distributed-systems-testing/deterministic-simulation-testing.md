---
domain: system-design
subdomain: distributed-systems-testing
concept: deterministic-simulation-testing
title: Deterministic Simulation Testing
sources:
  - title: "Deterministic Simulation Testing"
    url: "https://martinfowler.com/articles/deterministic-simulation-testing.html"
    author: "Martin Fowler"
---

# Deterministic Simulation Testing

Distributed systems are notoriously hard to test: partial failures overlap with live traffic, and the same injected fault can yield different execution traces across runs, making failures hard to reproduce. Unmesh Joshi's article, summarized by Martin Fowler, describes deterministic simulation testing as a way to address this.

The core technique replaces real clocks, networks, and storage with simulated components driven by a single-threaded execution loop. Because everything is simulated and the loop is single-threaded, every execution becomes reproducible. This lets testers simulate both hard failures and routine slowdowns such as network and disk latency spikes.

The article explains the approach using a quorum key-value store as a running example, with code drawn from Tickloom, a Java implementation of the technique.

- Distributed systems are hard to test because partial failures overlap with live traffic and identical faults can produce different traces on different runs.
- Deterministic simulation testing replaces real clocks, networks, and storage with simulated components driven by a single-threaded execution loop.
- The approach makes every execution reproducible and can simulate both hard failures and routine latency spikes.
- The technique is illustrated with a quorum key-value store example using Tickloom, a Java implementation.