---
domain: ai-workflows
subdomain: enterprise-agents
concept: governed-agent-infrastructure
title: Paving the Road to Production: Governed Enterprise AI Agents
sources:
  - title: "Paving the Road to Production: Governed Enterprise AI Agents — Harish Gaggar, Credit Karma"
    url: "https://www.youtube.com/watch?v=tZycGA_Fbfo"
    author: "AI Engineer"
    date: "2026-10-14"
---

# Paving the Road to Production: Governed Enterprise AI Agents

Harish Gaggar, a senior staff software engineer at Intuit Credit Karma, argues that most AI agents fail in production because foundational controls are missing. He identifies several gaps: agents lack a gateway to authenticate and route to the right MCP servers, MCP servers may lack the right tools to execute queries, and there is often no tracking/evaluation, memory management, context optimization, or protection against secrets leaking into LLMs or memory databases. Rather than building a "magical agent," he proposes a framework of composable infrastructure components to address these challenges.

The proposed architecture has four main parts. First, an agent framework such as LangGraph (from the LangChain community) builds task-specific nodes that can plug in marketplace plugins, skills, and prompts. Second, an MCP gateway authenticates agent or service-account calls and redirects them to the correct MCP servers. Third, customized MCP servers provide the right tools to execute queries. Fourth, an audit layer records operations. Additional frameworks handle PII/secret blocking, storing tracking and evaluation data in the cloud, processing memories and thread checkpoints, and optimizing context to avoid burning too many tokens.

For local development, the workflow begins by registering the agent in a system with its use case, vertical, and an agent ID. Developers then use an internal dev portal to ingest details such as the agent ID, chosen framework (LangGraph or LangChain), language (Python or TypeScript), and skills or prompts before submitting the information.

- Agents often fail in production due to missing foundational controls like authentication gateways, proper MCP tools, tracking/evaluation, memory management, and secret protection.
- The proposed architecture combines an agent framework (e.g., LangGraph), an MCP gateway for secure authentication and routing, customized MCP servers with the right tools, and an audit layer.
- Additional frameworks are needed for PII/secret blocking, cloud-based tracking and evaluation, memory/thread checkpoint processing, and context optimization to reduce token usage.
- Local development starts with agent registration (use case, vertical, agent ID) and an internal dev portal to capture framework, language, and skills/prompts.