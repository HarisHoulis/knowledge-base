---
domain: ai-workflows
subdomain: agent-tooling
concept: mcp-gateway
title: How Uber Built a Gateway for AI Agents to Access Tools
sources:
  - title: "How Uber Built A Gateway For AI Agents To Access Tools"
    url: "https://blog.bytebytego.com/p/how-uber-built-a-gateway-for-ai-agents"
    author: "ByteByteGo"
    date: "2026-10-28"
---

# How Uber Built a Gateway for AI Agents to Access Tools

Uber's engineering team built an MCP Gateway to solve the problem of many teams independently building MCP integrations for their services. An off-the-shelf LLM can't answer questions about internal systems, so tools (structured operations like log search or deployment status checks) are needed; MCP (Model Context Protocol) standardizes how AI applications discover and call these tools via MCP clients, servers, and tool definitions using JSON-RPC 2.0. As adoption grew, teams duplicated work on exposing tools, managing connections, and permissions, and Uber's mix of HTTP, gRPC, and TChannel services made direct forwarding of MCP requests impossible.

The gateway splits into two components: the MCP Registry (control plane) holds the catalog of servers and tools and manages configuration, while the Proxy Gateway (data plane) handles live MCP requests, routing them to the right service and returning MCP-compatible results. Tool discovery is automated by AutoCrawler, a Cadence-powered distributed workflow that reads existing API IDL definitions to generate tool schemas (using an LLM to improve descriptions) and also detects native MCP servers via heartbeat metrics and listTools calls.

Newly discovered tools start disabled; the owning service team must review and enable them, with every change tracked as an approvable diff that can be rolled back. The data plane periodically refreshes in-memory configuration to create virtual MCP servers (e.g., logging/mcp), converting JSON tool arguments into the downstream format (Protobuf for gRPC, HTTP, or Thrift/TChannel) and translating responses back. Access control is enforced centrally via Uber's internal Access Control System at server or tool granularity, with PII redaction and token exchange for third-party services like Jira and Google.

To handle a catalog of thousands of tools without exhausting the model's context window, Uber added Omni MCP, a single proxy server that lets agents discover capabilities gradually rather than loading all tool definitions upfront.

- MCP Gateway separates a control plane (Registry for tool catalog and config) from a data plane (Proxy Gateway for live request routing).
- AutoCrawler automates tool discovery from API IDL definitions and native MCP server heartbeats, using an LLM to generate better tool descriptions.
- Discovered tools start disabled and require owner-team review and approval, with versioned diffs and rollback.
- The gateway translates MCP JSON arguments into gRPC/Protobuf, HTTP, or TChannel formats and enforces tool-level access control with PII redaction.
- Omni MCP addresses context-window limits by enabling gradual tool discovery instead of loading thousands of tool definitions upfront.