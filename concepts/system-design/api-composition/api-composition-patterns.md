---
domain: system-design
subdomain: api-composition
concept: api-composition-patterns
title: A Detailed Guide to API Composition Techniques
sources:
  - title: "A Detailed Guide to API Composition Techniques"
    url: "https://blog.bytebytego.com/p/a-detailed-guide-to-api-composition"
    author: "ByteByteGo"
    date: "2026-08-13"
---

# A Detailed Guide to API Composition Techniques

The article from ByteByteGo (2026) explains that API composition is the process of merging data from multiple services to satisfy a single client request, which becomes necessary when data is split across service boundaries. The location where this merging happens—client, server, edge, or an API gateway—has significant trade-offs in latency, availability, caching, and ownership. Client-side composition is the default due to no extra infrastructure, but it suffers from multiple round trips over slow networks, complex error handling, limited observability, and the inability to update deployed mobile clients. Server-side composition, such as a backend for frontend (BFF), can reduce latency by trading one expensive mobile round trip for several cheap internal calls, but introduces coordination overhead depending on the team structure.

The article also contrasts aggregation and orchestration patterns: aggregation issues independent calls in parallel and merges results, approximating the slowest call, while orchestration sequences dependent calls, summing their latencies. Availability math shows that when all services are required, the overall success rate is the product of individual availabilities—five services at 99.9% availability compose to roughly 99.5%. Optional dependencies can be handled with timeouts, fallbacks, or cached defaults to improve resilience. Caching trade-offs are highlighted: fine-grained resource endpoints cache well because they are identical across requesters, but composed personalized responses are poorly cacheable since they are user-specific. The ratio of personalized to public data should guide the decision.

The article further explores API gateways, BFFs, and GraphQL as composition layers. Gateways centralize cross-cutting concerns like authentication and rate limiting but risk becoming a shared product layer, causing coordination bottlenecks. BFFs are dedicated to one client and owned by its team, enabling independent release cycles at the cost of duplicated code—duplication is often cheaper than shared-dependency coordination. GraphQL provides a flexible query layer where clients specify fields, decoupling client and server releases, but introduces the N+1 problem and caching challenges. Ultimately, the choice of composition location depends on balancing latency, availability, caching efficiency, and organizational ownership (ByteByteGo, 2026).

- API composition is unavoidable in service-based architectures; the merge can run client-side, in a gateway or BFF, or in a GraphQL layer.
- Client-side composition is simple but suffers from high latency, poor error handling, and limited observability; server-side composition typically reduces total time by trading one expensive mobile round trip for several cheap internal calls.
- Aggregation (parallel calls) approximates the slowest call, while orchestration (sequential calls) sums latency; required dependencies multiply failure rates, so optional dependencies should be isolated with fallbacks.
- Composed personalized responses are poorly cacheable; the ratio of personalized to public data should guide whether to compose or use fine-grained cached endpoints.
- Ownership matters: BFFs avoid cross-team coordination at the cost of duplication, while shared gateways or common libraries reintroduce coordination overhead.