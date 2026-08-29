---
domain: ai-workflows
subdomain: model-context-protocol
concept: stateless-mcp
title: Here's how the new MCP spec works
sources:
  - title: "Here's how the new MCP spec works"
    url: "https://www.youtube.com/watch?v=1B9H6RTAGmE"
    author: "Kent C. Dodds"
    date: "2026-08-20T14:08:18+00:00"
---

# Here's how the new MCP spec works

Kent C. Dodds explains the major update to the Model Context Protocol (MCP), which addresses common complaints by making the protocol stateless. He argues that protocols improve through real-world adoption, comparing MCP's evolution to JavaScript's ubiquity. The new spec enables more scalable and resilient AI agent architectures.

The core change is the shift from stateful connections, where a client must maintain a session with a specific server instance, to a stateless model. In the old design, a load balancer would route the initial request to an instance, and all subsequent requests had to go to that same instance because it held the session state. If that instance failed or overloaded, the connection was broken. The new stateless approach allows any instance to handle any request, making deployments more flexible and fault-tolerant.

Dodds highlights his experience using Cloudflare's Agents SDK, which already handled many MCP pain points and made upgrading to the latest spec straightforward—a 1200-line diff, mostly tests and documentation. He also notes that adoption is gradual, with most requests still using the legacy protocol, but the new spec is gaining traction. He mentions the new client identifier metadata document, which changes how authentication works.

- MCP has become a stateless protocol, removing the need for session-pinned connections.
- Statelessness allows load balancers to route requests to any server instance, improving reliability and scalability.
- The upgrade path can be smooth; Dodds upgraded via Cloudflare's Agents SDK with a 1200-line diff.
- The new spec includes a client identifier metadata document, altering authentication.
- MCP's evolution mirrors JavaScript's adoption-driven improvement, per Dodds.