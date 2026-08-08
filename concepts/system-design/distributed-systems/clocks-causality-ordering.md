---
domain: system-design
subdomain: distributed-systems
concept: clocks-causality-ordering
title: A Beginner's Guide to Clocks, Causality, and Ordering in Distributed Systems
sources:
  - title: "A Beginner’s Guide to Clocks, Causality, and Ordering in Distributed Systems"
    url: "https://blog.bytebytego.com/p/a-beginners-guide-to-clocks-causality"
    author: "ByteByteGo"
    date: "Thu, 23 Jul 2026 15:30:41 GMT"
---

# A Beginner's Guide to Clocks, Causality, and Ordering in Distributed Systems

Distributed systems lack a shared clock, so ordering events across machines is fundamentally hard. Each machine has its own hardware clock, and even with Network Time Protocol (NTP), clocks do not stay perfectly aligned. This can lead to incorrect results when comparing timestamps: a later update might be discarded because its timestamp appears older, logs can show effects before their causes, and operations that depend on ordering can act on stale data (ByteByteGo, 2026).

- Single-machine systems can rely on one clock; distributed systems cannot because machine clocks drift apart, and NTP only reduces but never eliminates skew.
- Clock skew can cause lost updates, reversed causality in logs, and stale reads in operations that depend on order.
- Logical clocks capture causality (happened-before) but cannot distinguish concurrent events; vector clocks can compare concurrent events but require more storage.
- Hybrid logical clocks combine physical time with logical ordering to get both real-time closeness and causal consistency.
- Systems such as Google Spanner use TrueTime and commit-wait to achieve globally ordered transactions at scale.