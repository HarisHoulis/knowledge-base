---
domain: system-design
subdomain: low-latency-distributed-apis
concept: sub-100ms-latency-budgets
title: From Fan-Out to Fast: Sub-100ms API Design in Distributed Systems
sources:
  - title: "Presentation: From Fan-Out to Fast: Sub-100ms API Design in Distributed Systems"
    url: "https://www.infoq.com/presentations/sub-100ms-latency-distributed-systems/"
    author: "Saranya Vedagiri"
    date: "2026-11-27"
---

# From Fan-Out to Fast: Sub-100ms API Design in Distributed Systems

Saranya Vedagiri presents strategies for designing resilient, low-latency distributed APIs that respond in under 100ms, drawing on practical experience at eBay scale. The talk centers on treating latency as a first-class engineering concern rather than an afterthought.

A core technique is hop-by-hop latency budgeting: allocating a latency allowance to each network hop and downstream dependency so that the end-to-end request stays within the sub-100ms target. She also examines the tradeoffs of asynchronous fanout, where parallelizing downstream calls can reduce latency but introduces complexity and risk.

The presentation covers thread pool sizing to avoid contention and queuing delays, caching to short-circuit expensive work, and circuit breakers to contain failures and prevent cascading slowdowns. A recurring theme is eliminating tail-latency bottlenecks, since outliers often dominate perceived performance.

Overall, Vedagiri argues for establishing performance-first engineering practices so that latency targets are enforced systematically across distributed systems rather than left to chance.

- Use hop-by-hop latency budgets to keep end-to-end requests under 100ms across distributed hops
- Weigh the tradeoffs of async fanout when parallelizing downstream calls
- Size thread pools carefully to avoid contention and queuing delays
- Apply caching and circuit breakers to cut latency and contain failures
- Focus on eliminating tail-latency bottlenecks and institutionalize performance-first practices