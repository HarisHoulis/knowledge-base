---
domain: ai-workflows
subdomain: mcp-protocol
concept: stateless-mcp
title: Here's how the new MCP spec works
sources:
  - title: "Here's how the new MCP spec works"
    url: "https://www.youtube.com/watch?v=1B9H6RTAGmE"
    author: "Kent C. Dodds"
    date: "2026-08-20T14:08:18+00:00"
---

# Here's how the new MCP spec works

Kent C. Dodds explains that the Model Context Protocol (MCP) has undergone a major upgrade, addressing many earlier criticisms. The biggest change is that MCP is now a stateless protocol, allowing clients to send requests to any server instance via a load balancer rather than being pinned to a single stateful session. This improves scalability and resilience, as a server instance failure no longer breaks the connection (Kent C. Dodds, 2026). Dodds highlights that adoption and real-world usage are what drive protocol improvements, comparing MCP's evolution to JavaScript's ubiquity despite imperfections. He also credits Cloudflare's Agents SDK for smoothing the transition, handling legacy request detection and enabling a straightforward upgrade path (a ~1200-line diff) for his personal AI assistant, Kodi. The new spec also introduces a client identifier metadata document for authentication, which Dodds notes is the new way auth works. He observed that most requests to Kodi are still legacy, but the new spec is already adopted in 'quad code' and traffic on the new lane is growing.

- MCP has become a stateless protocol, eliminating the need for sticky sessions and enabling horizontal scaling via load balancers.
- Statelessness improves resilience: if one server instance goes down, other instances can still handle requests.
- The new spec includes a client identifier metadata document for authentication, updating how MCP auth works.
- Cloudflare's Agents SDK handles legacy requests and makes upgrading to the new MCP spec nearly seamless.
- Adoption of MCP in real-world tools like Kodi is driving the protocol's evolution and gradual transition away from legacy requests.