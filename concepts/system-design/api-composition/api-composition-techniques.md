---
domain: system-design
subdomain: api-composition
concept: api-composition-techniques
title: A Detailed Guide to API Composition Techniques
sources:
  - title: "A Detailed Guide to API Composition Techniques"
    url: "https://blog.bytebytego.com/p/a-detailed-guide-to-api-composition"
    author: "ByteByteGo"
    date: "2026-08-13"
---

# A Detailed Guide to API Composition Techniques

API composition is the process of merging data from multiple services to fulfill a single client request. The article explains that this problem arises because services are organized around business capabilities while screens are organized around user journeys, so no single service can return the full payload. A composition point can be implemented in different locations—client, server, gateway, BFF, GraphQL resolver, or edge worker—each with distinct trade-offs (ByteByteGo, 2026).

Key trade-offs include round-trip latency, payload size, availability, caching, and ownership. Client-side composition requires no extra infrastructure but suffers from slow mobile network round trips and limited observability. Moving composition to a server reduces total latency by trading one expensive mobile round trip for several cheap datacenter round trips, but introduces coordination and deployment concerns. The article distinguishes between aggregation (parallel calls) and orchestration (sequential calls), noting that availability is the product of upstream service availabilities when all calls are required, and that optional dependencies can be given fallbacks to improve resilience (ByteByteGo, 2026).

The article evaluates server-side patterns: API gateways centralize infrastructure concerns but can become a shared product layer with cross-team coordination overhead; Backends for Frontends (BFFs) provide client-specific composition owned by the client team, at the cost of duplication and potential lack of platform expertise; GraphQL offers a flexible query layer but suffers from N+1 problems and caching challenges. Ultimately, the choice of composition pattern depends on personalization ratio, team ownership, and desired availability/caching behavior (ByteByteGo, 2026).

- API composition is necessary when data is split across multiple services; the merge can happen at the client, gateway, BFF, GraphQL, or edge.
- Moving composition to a server often reduces total latency despite adding a network hop, because datacenter round trips are far cheaper than mobile-to-server ones.
- Aggregation (parallel calls) yields latency of the slowest call, while orchestration (sequential calls) sums latencies; availability is the product of upstream availabilities for required dependencies.
- Caching is inversely related to personalization: fine-grained public endpoints cache well, while composed user-specific responses have near-zero cache hit rate.
- BFFs avoid shared coordination by dedicating a backend layer per client, but risk duplicating logic; GraphQL provides flexible field selection but introduces N+1 and caching complexity.