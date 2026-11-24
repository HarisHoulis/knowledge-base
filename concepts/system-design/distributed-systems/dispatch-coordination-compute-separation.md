---
domain: system-design
subdomain: distributed-systems
concept: dispatch-coordination-compute-separation
title: DoorDash Dispatch: Scaling Delivery Assignment via Coordinator/Compute Separation
sources:
  - title: "DoorDash Dispatch: Building a Lightning-Fast Delivery System"
    url: "https://blog.bytebytego.com/p/doordash-dispatch-building-a-lightning"
    author: "ByteByteGo"
    date: "2026-11-23"
---

# DoorDash Dispatch: Scaling Delivery Assignment via Coordinator/Compute Separation

DoorDash redesigned its dispatch platform to handle the growing complexity of assigning Dashers to orders. The original monolith combined logistics state, business rules, and expensive routing calculations, and its roughly quadratic algorithms meant computational work grew far faster than delivery volume, forcing the system to limit search or fall back to simpler rules during peaks (ByteByteGo).

The redesign split the system into two independently scalable tiers: a coordinator that maintains logistics state, applies business rules, and organizes work, and a stateless compute tier of workers that run routing, optimization, and ML calculations. The coordinator sends self-contained, localized payload shards over gRPC each dispatch tick, avoiding the cost of broadcasting the full logistics state to every worker (ByteByteGo).

To shrink the optimization problem itself, DoorDash introduced hierarchical decomposition: the coordinator groups work into localized geographic clusters and delivery trajectories using rapid pre-clustering followed by centroid-based refinement. Workers solve these smaller partitions in parallel, and a global reconciliation and scoring layer recombines results so boundary-spanning relationships between orders and routes are preserved (ByteByteGo).

The team rolled out the critical replacement safely via shadow testing (duplicating production work to the new engine while the old one controlled deliveries) followed by production switchback experiments with limited exposure and fallback mechanisms. Reported results include 10x dispatch processing scale, over 99.96% of runs completing under 20 seconds, and over 99.99% availability during Super Bowl spikes (ByteByteGo).

- Separating a stateful coordinator tier from stateless compute workers enables independent scaling and parallel execution of expensive routing and optimization work.
- Localized payload sharding over gRPC avoids shipping the full logistics state to every worker on each dispatch tick.
- Hierarchical decomposition (pre-clustering plus centroid refinement) shrinks the optimization problem, while a global reconciliation layer preserves cross-partition quality.
- Shadow testing followed by production switchback experiments de-risked replacing a critical live system.
- Results: 10x processing scale, >99.96% of runs under 20 seconds, and >99.99% availability during peak traffic.