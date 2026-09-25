---
domain: ai-workflows
subdomain: mcp-server-deployment
concept: stateless-mcp
title: Stateless MCP Removes Session Affinity Requirements for AWS Server Deployments
sources:
  - title: "Stateless MCP Removes Session Affinity Requirements for AWS Server Deployments"
    url: "https://www.infoq.com/news/2026/09/aws-stateless-mcp/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Leela Kumili"
    date: "2026-09-25"
---

# Stateless MCP Removes Session Affinity Requirements for AWS Server Deployments

AWS details how the latest Model Context Protocol specification removes protocol-level sessions, sticky-session requirements, and session storage for remote MCP servers (Kumili, 2026). The change enables independent request routing and simpler horizontal scaling (Kumili, 2026).

The shift moves application state, retries, observability, and idempotency concerns to other layers rather than the protocol itself (Kumili, 2026).

- The latest MCP specification removes protocol-level sessions, sticky-session requirements, and session storage for remote MCP servers.
- Removing sessions enables independent request routing and simpler horizontal scaling.
- Application state, retries, observability, and idempotency concerns shift to other layers.