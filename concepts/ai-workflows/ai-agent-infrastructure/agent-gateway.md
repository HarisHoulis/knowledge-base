---
domain: ai-workflows
subdomain: ai-agent-infrastructure
concept: agent-gateway
title: DoorDash’s Agent Gateway for AI Agent Tool Access
sources:
  - title: "How DoorDash Built a Toolbox for AI Agents"
    url: "https://blog.bytebytego.com/p/how-doordash-built-a-toolbox-for"
    author: "ByteByteGo"
    date: "2026-09-30"
---

# DoorDash’s Agent Gateway for AI Agent Tool Access

DoorDash built a shared Agent Gateway to govern how AI agents discover and use tools. MCP standardizes tool description, discovery (tools/list), and invocation (tools/call), but it does not handle company-specific concerns such as permissions, credentials, tool curation, and monitoring. Without a shared platform, teams duplicate OAuth flows, secret handling, and usage recording (ByteByteGo, 2026).

DoorDash split the gateway into a proxy and a registry. The proxy, in the data plane, verifies callers, checks permissions, applies rate limits, attaches credentials, forwards approved MCP requests, and emits monitoring/audit data. The registry is the control plane source of truth, storing agent and MCP server registrations, ownership, connection settings, auth modes, policies, discovered tool catalogs, and tool-exposure configuration. Internal and external use cases use separate proxy planes that share libraries and registry concepts but maintain separate trust boundaries (ByteByteGo, 2026).

Authentication establishes caller identity, while authorization determines what that caller may do. The gateway evaluates context including the agent, user, requested tool, environment, and read-only versus modifying access. Credential injection remains separate from caller identity: downstream systems may require internal service identity, gateway-held tokens, per-user OAuth, or service principal credentials. Raw vendor keys and OAuth refresh tokens stay out of agents, giving the platform a central place to manage, rotate, audit, and revoke them (ByteByteGo, 2026).

For user-specific tools, the gateway starts the provider’s OAuth flow when needed and stores encrypted tokens. With MCP elicitation, it can pause the original tool call, ask the user to connect an account, then resume the request; without elicitation, it returns a structured authorization-required response with a connection URL. DoorDash also curates smaller, relevant tool catalogs instead of exposing a server’s full catalog, reducing ambiguous choices for the model (ByteByteGo, 2026).

- MCP standardizes tools/list and tools/call but does not solve enterprise access, credentials, tool curation, or operations.
- DoorDash’s Agent Gateway separates a data-plane proxy from a control-plane registry.
- The gateway centralizes authentication and authorization using context such as agent, user, requested tool, environment, and read/write access.
- Credential injection supports internal service identity, gateway-held tokens, per-user OAuth, and service principals while keeping raw downstream credentials away from agents.
- User account connection uses OAuth, with MCP elicitation for pause-and-resume or a structured response containing a connection URL; tool catalogs are curated per workflow.