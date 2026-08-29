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

The article explores API composition in service-based architectures, where a single screen requires data from multiple services. The core problem is that splitting data across services removes the ability to perform joins across a single database, so the merging of responses must happen elsewhere, such as in the client, a gateway, a backend for frontend, or an edge worker. The choice of composition point affects latency, availability, caching, and team ownership.

The author emphasizes that round-trip time is often the dominant factor in mobile performance compared to payload size, so reducing the number of round trips by composing on a server can be a net win even with an added network hop. The article distinguishes between aggregation (parallel calls) and orchestration (sequential calls), noting that aggregation yields lower latency but requires handling partial failures. Availability is also multiplicative: five services at 99.9% availability compose to roughly 99.5%, motivating the separation of required and optional dependencies.

Caching tradeoffs are highlighted: composed, personalized responses have poor cache hit rates, while fine-grained resource endpoints cache well. Patterns like API gateways centralize common infrastructure concerns but risk becoming a shared product layer, while Backends for Frontends (BFFs) offer client-specific composition at the cost of duplication. GraphQL provides a flexible query layer but introduces challenges like the N+1 problem. The article concludes by discussing ownership and versioning, arguing that the composition layer should be owned by the consuming client team to avoid coordination bottlenecks.

- API composition is the merging of responses from multiple services; the location of composition (client, server, edge) determines tradeoffs in latency, availability, caching, and team coordination.
- Round-trip time generally matters more than payload size for mobile users; reducing round trips via composition can significantly improve load times.
- Aggregation (parallel calls) minimizes latency but requires handling partial failures, while orchestration (sequential calls) is slower and more fragile.
- Availability degrades multiplicatively with each required upstream call; optional dependencies with fallbacks help maintain response availability.
- BFFs and GraphQL layers reduce client complexity and decouple releases, but introduce duplication or N+1 issues that must be managed.