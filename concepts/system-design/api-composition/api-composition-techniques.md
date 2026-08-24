---
domain: system-design
subdomain: api-composition
concept: api-composition-techniques
title: A Detailed Guide to API Composition Techniques
sources:
  - title: "A Detailed Guide to API Composition Techniques"
    url: "https://blog.bytebytego.com/p/a-detailed-guide-to-api-composition"
    author: "ByteByteGo"
    date: "Thu, 13 Aug 2026 15:30:27 GMT"
---

# A Detailed Guide to API Composition Techniques

API composition is the merging of data from multiple services into a single response, required when data is split across service boundaries. The merging code can run in the client, a server, a CDN edge, or inside a service. Although adding a server introduces a network hop, it often reduces total load time because it trades expensive mobile round trips for cheap datacenter round trips (ByteByteGo, 2026).

Client-side composition is the default because it needs no extra infrastructure, but it suffers from multiple round trips over the slowest network, complex retry and failure logic in application code, poor observability, and slow update cycles on mobile devices. The article argues that round-trip count usually matters more than payload size for most screens, except in image-heavy or metered-data contexts. Composition patterns include aggregation, where independent calls run in parallel, and orchestration, where calls are sequential and each depends on the previous result; most real systems combine both (ByteByteGo, 2026). Availability is also affected: if all upstream calls are required, the success rate is the product of their availabilities, but optional dependencies can be given fallbacks to improve resilience.

Server-side composition options include API gateways, Backends for Frontends (BFFs), and GraphQL. An API gateway centralizes cross-cutting concerns and may compose generic resources, but embedding client-specific product logic in a shared gateway creates coordination bottlenecks. A BFF is dedicated to one client and owned by its team, avoiding shared-layer coordination at the cost of duplication; business rules should remain in the owning services. GraphQL provides a query layer where clients specify fields and resolvers fetch data, but it introduces the N+1 problem and changes caching behavior because a single endpoint does not have cacheable URLs (ByteByteGo, 2026).

- API composition is unavoidable when data is split across services; the location of the merging code determines latency, availability, caching, and ownership tradeoffs.
- Client-side composition is simple but often slower due to multiple mobile round trips, poor observability, and slow update cycles; server-side composition can reduce overall latency.
- Round-trip count is usually more important than payload size; aggregation (parallel calls) has different latency and failure characteristics than orchestration (sequential calls).
- API gateways centralize composition but can become coordination bottlenecks; BFFs provide dedicated, client-owned composition layers at the cost of duplication.
- GraphQL shifts composition to a query layer with resolver-based merging, but introduces N+1 query problems and complicates caching.