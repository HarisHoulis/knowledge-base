---
domain: ai-workflows
subdomain: agent-interfaces
concept: agent-first-cli-design
title: Designing CLIs and MCP Servers for Agents, Not Humans
sources:
  - title: "Designing CLIs for Agents, Not Humans — Pedro Lopez, Airbyte"
    url: "https://www.youtube.com/watch?v=3wj6sgbi1YA"
    author: "AI Engineer"
    date: "2026-10-09"
---

# Designing CLIs and MCP Servers for Agents, Not Humans

Pedro Lopez, a software engineer at Airbyte, describes how Airbyte built an MCP server and CLI to expose its data and action layer to AI agents. Airbyte began as an open-source standard for data movement connecting SaaS tools like Zendesk, Stripe, and GitHub to analytics pipelines, and has transformed that experience into a context store that sits between agents and third-party tools, providing a searchable index of data for efficient queries. The context store is accessible through three interfaces: an SDK for building custom agents, a UI for quick web use, and the MCP/CLI for embedding into existing agents like ChatGPT and Claude.

All interfaces expose three core capabilities: managing resources (organizations, workspaces, connectors), securely authenticating third-party services without revealing credentials to AI agents, and asking/acting—searching the context store, reading and writing data, and performing actions across systems. The MCP and CLI are deliberately structured as lightweight unified interfaces to the platform rather than re-implementations; most of their surface is presentational, calling the shared platform and API. Because Airbyte's platform changes over ten times a day, OpenAPI specifications serve as the source of truth so these interfaces stay up to date.

MCP is positioned as ideal for non-technical users who want to connect data directly to ChatGPT or Claude, with easy installation via a hosted URL or app marketplaces. A demo shows a user asking which connectors are available, then querying for five paid customers with Zendesk support tickets, with the system combining context store, Zendesk, and Stripe data to produce the answer.

Key lessons from building the MCP include limiting the number of tools: for connector execution, Airbyte uses only two main tools—one describing the connector to obtain a data query schema, and one implementation allowing reading, writing, and deleting records—rather than a separate tool per connector. Narrow specialization, progressive connector capability discovery, and limiting the scope of context in tool descriptions significantly improve MCP server performance. The talk also advocates OAuth as the right way to authenticate to the MCP server itself, illustrated with an Anthropic flow where the user clicks connect, logs into Airbyte, and accepts the authorization.

- Airbyte exposes its context store through an SDK, UI, and MCP/CLI, with MCP/CLI acting as lightweight unified interfaces to the shared platform rather than re-implementations.
- All interfaces provide three capabilities: resource management, secure third-party authentication without exposing credentials to agents, and ask/act operations over the context store.
- Limiting MCP tools to two (connector description for schema discovery and a read/write/delete implementation) outperforms creating a separate tool per connector.
- Narrow specialization, progressive capability discovery, and scoped tool descriptions significantly improve MCP server performance.
- OAuth is recommended for authenticating to the MCP server itself, with a flow where users log into Airbyte and accept authorization.