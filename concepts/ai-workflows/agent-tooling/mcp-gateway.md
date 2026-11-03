---
domain: ai-workflows
subdomain: agent-tooling
concept: mcp-gateway
title: Uber Builds MCP Gateway to Govern Access to 800+ Servers and 5,000+ AI Agent Tools
sources:
  - title: "Uber Builds MCP Gateway to Govern Access to 800+ Servers and 5,000+ AI Agent Tools"
    url: "https://www.infoq.com/news/2026/11/uber-mcp-gateway-ai-agents/"
    author: "Leela Kumili"
    date: "2026-11-02"
---

# Uber Builds MCP Gateway to Govern Access to 800+ Servers and 5,000+ AI Agent Tools

Uber has built an MCP Gateway to standardize how AI agents discover and invoke internal services across more than 800 MCP servers and 5,000 tools (InfoQ, Leela Kumili). The gateway separates tool registration from runtime execution, decoupling how tools are catalogued from how they are actually called at runtime.

The gateway includes automated API discovery, access controls, sensitive data redaction, incremental tool discovery through Omni MCP, and response filtering. These features let Uber govern which agents can reach which internal services and limit what data flows back to them.

Incremental tool discovery via Omni MCP addresses the scale problem of exposing thousands of tools to agents, while response filtering and redaction add guardrails around sensitive data at the gateway layer rather than in each individual server.

- Uber's MCP Gateway fronts 800+ MCP servers and 5,000+ tools for AI agents
- It separates tool registration from runtime execution
- Features include automated API discovery, access controls, sensitive data redaction, and response filtering
- Omni MCP provides incremental tool discovery to manage scale