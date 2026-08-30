---
domain: ai-workflows
subdomain: model-context-protocol
concept: stateless-mcp-spec
title: Here's how the new MCP spec works
sources:
  - title: "Here's how the new MCP spec works"
    url: "https://www.youtube.com/watch?v=1B9H6RTAGmE"
    author: "Kent C. Dodds"
    date: "2026-08-20T14:08:18+00:00"
---

# Here's how the new MCP spec works

Kent C. Dodds explains that the Model Context Protocol (MCP), which enables agents to communicate with external services in a standardized way, has been significantly improved. The biggest change is that MCP is now a stateless protocol. Previously, MCP required a client to maintain a connection to a specific server instance that held the session, creating problems if that instance became overloaded or failed. With statelessness, a load balancer can route each request to any available server instance, making the system more resilient and scalable.

Dodds highlights how Cloudflare's Agents SDK handled most of the upgrade for him, making it easy to adopt the latest MCP spec in his personal AI assistant, Kodi. The change involved a 1200-line diff including tests and documentation. He also notes that as of the recording, most requests to Kodi are still legacy, but the new spec is already adopted in Quad code and traffic is gradually shifting. Additionally, the new spec includes a new authentication mechanism via a client identifier metadata document.

- MCP is now a stateless protocol, fixing the previous need for session affinity and improving resilience.
- Statelessness allows load balancers to route requests to any server instance, avoiding single points of failure.
- Cloudflare's Agents SDK made upgrading to the new MCP spec straightforward for Dodds's assistant, Kodi.
- The new spec introduces client identifier metadata for authentication.
- Adoption is still transitioning from legacy requests to the new spec, but it's already used in Quad code.