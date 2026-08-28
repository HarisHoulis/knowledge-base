---
domain: system-design
subdomain: api-composition
concept: api-composition
title: A Detailed Guide to API Composition Techniques
sources:
  - title: "A Detailed Guide to API Composition Techniques"
    url: "https://blog.bytebytego.com/p/a-detailed-guide-to-api-composition"
    author: "ByteByteGo"
    date: "2026-08-13"
---

# A Detailed Guide to API Composition Techniques

The article explains that API composition is the process of merging data from multiple services to fulfill a single client request, a necessity when data is split across service boundaries. It emphasizes that the location of composition—client, server, gateway, or edge—drives tradeoffs in latency, availability, caching, and team coordination. While client-side composition avoids infrastructure, it suffers from slow round trips on mobile networks, complex failure handling, and poor observability; a server-side hop often reduces total latency by trading one expensive mobile round trip for several cheap internal ones.

- API composition is required when a screen needs data from multiple services; the merge location determines latency, availability, caching, and ownership.
- Aggregation (parallel calls) minimizes latency but can still fail on required dependencies; orchestration (sequential calls) sums latency and adds chain failure points.
- Composed availability degrades as the product of upstream availabilities; design for optional dependencies with fallbacks to improve resilience.
- Composition reduces round trips but hurts cacheability for personalized responses, so the public-to-personalized ratio matters.
- BFFs avoid shared-layer coordination at the cost of duplication, while GraphQL offers flexible queries but introduces N+1 resolver issues that need batching.