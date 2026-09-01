---
domain: system-design
subdomain: api-composition
concept: api-composition
title: A Detailed Guide to API Composition Techniques
sources:
  - title: "A Detailed Guide to API Composition Techniques"
    url: "https://blog.bytebytego.com/p/a-detailed-guide-to-api-composition"
    author: "ByteByteGo"
    date: "Thu, 13 Aug 2026 15:30:27 GMT"
---

# A Detailed Guide to API Composition Techniques

API composition is the merging of responses from multiple services to serve a single client screen. When data is split across services, no single service can satisfy a screen's needs, so composition is required. The location of composition—client, server, edge, or within a service—determines latency, failure handling, cacheability, and ownership. Placing a server between the client and services adds one expensive network hop but replaces several expensive client-server round trips with cheap datacenter round trips, often reducing total load time [1]. The article emphasizes that round-trip count, not payload size, dominates latency for most screens, since mobile round trips can cost hundreds of milliseconds while intra-datacenter trips are sub-millisecond [1].

- Composition exists wherever data is split across services; the merge can happen on the client, in a server, at the edge, or inside a service, with each choice affecting latency, availability, caching, and team ownership.
- The main latency factor is the number of sequential round trips, not payload bytes, except in image-heavy or metered-network cases. Moving composition server-side trades one expensive constrained-network round trip for several cheap datacenter round trips.
- Aggregation runs parallel calls and finishes in the slowest-call time, while orchestration chains sequential dependencies and sums latencies; most systems combine the two.
- Availability degrades multiply when all upstream calls are required, so splitting dependencies into required and optional—with fallbacks or cached defaults—preserves uptime. Composed responses cache poorly when personalized, making the ratio of personalized to public content the key cacheability metric.
- API gateways, BFFs, and GraphQL each solve coordination and ownership differently: gateways centralize cross-cutting concerns but become shared product layers, BFFs isolate per-client logic but risk duplication, and GraphQL decouples clients from server changes but introduces N+1 and caching challenges.