---
domain: ai-workflows
subdomain: mcp
concept: stateless-mcp
title: Here's how the new MCP spec works
sources:
  - title: "Here's how the new MCP spec works"
    url: "https://www.youtube.com/watch?v=1B9H6RTAGmE"
    author: "Kent C. Dodds"
    date: "2026-08-20T14:08:18+00:00"
---

# Here's how the new MCP spec works

In this video, Kent C. Dodds explains the latest update to the Model Context Protocol (MCP), which he says fixes major criticisms of the protocol. The most significant change is that MCP is now a stateless protocol: a client can send requests to any server instance through a load balancer, rather than being tied to a specific instance that holds the session. This eliminates the fragility of the old stateful model, where an overloaded or failed instance would break the connection and leave the client unable to receive responses (Kent C. Dodds, YouTube). Dodds highlights that this change makes MCP easier to scale horizontally and is a direct response to real-world problems. He also credits Cloudflare's Agents SDK for abstracting away many previous MCP pain points, noting that upgrading to the new spec was mostly about handling 'legacy request' detection. He draws an analogy to JavaScript's ubiquity, arguing that a protocol's value comes from solving problems and gaining adoption, not from being perfect.

- MCP is now stateless, so any server instance can handle any request via a load balancer.
- The old stateful model required sticky sessions, making the system fragile if an instance failed.
- Cloudflare's Agents SDK already handled many MCP challenges, making the spec upgrade seamless.
- The MCP spec's evolution mirrors JavaScript's ubiquity: adoption and real-world problem-solving drive improvement.