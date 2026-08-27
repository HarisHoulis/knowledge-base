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

In service-based architectures, a single user-facing screen often requires data from multiple services, and the merging of these responses into a unified structure is known as API composition. The article by ByteByteGo (2026) illustrates this with a user profile screen that pulls data from four separate services, none of which can return the full set alone. The location where composition occurs—client, server, gateway, or edge—shapes key tradeoffs such as latency, availability, caching, and ownership. For instance, client-side composition requires no extra infrastructure but suffers from slow round trips over mobile networks and complicated retry logic, while server-side composition adds a network hop that is often negligible within a datacenter and can reduce total load time by replacing four expensive round trips with one expensive plus four cheap ones.

- API composition is necessary when data is split across services; the merge can run on the client, server, gateway, or edge, each with distinct tradeoffs in latency, availability, caching, and ownership.
- Client-side composition is simple to start but multiplies round trips and hides failures on individual devices, making server-side composition more attractive for mobile clients.
- Aggregation (parallel calls) minimizes latency and tolerates partial failure, whereas orchestration (sequential calls) adds latency and creates a chain of failure points; real systems often combine both.
- Composed responses with personalized content are poorly cacheable; API gateways that compose for multiple clients become shared product layers and coordination bottlenecks, while BFFs isolate client-specific logic at the cost of duplication.
- GraphQL shifts merging into resolvers, decoupling client releases from server changes, but requires careful batching to avoid the N+1 problem.