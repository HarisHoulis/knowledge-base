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

API composition is the practice of merging data from multiple services to satisfy a single client request. In service-based architectures, a typical screen may require data from several services, none of which can fulfill the request alone, so a composition layer collects and combines responses. The article explains that this merging can occur on the client, on a dedicated server, inside a service, or at the edge, and discusses the associated tradeoffs (ByteByteGo, 2026). A key insight is that placing composition on a server often reduces latency despite adding a network hop, because it replaces multiple expensive mobile round trips with one expensive trip plus cheap datacenter calls (ByteByteGo, 2026). The article goes on to explore patterns such as API gateways, Backends for Frontends (BFF), GraphQL as a composition layer, and edge composition, each with different implications for caching, availability, versioning, and team ownership (ByteByteGo, 2026).

- API composition merges responses from multiple services into a single client-facing payload.
- Server-side composition can reduce latency by trading several slow mobile round trips for one slow trip plus fast internal calls.
- Common composition patterns include client-side, API gateway, BFF, GraphQL, and edge composition.
- The choice of composition layer affects availability, caching, versioning, and ownership boundaries.