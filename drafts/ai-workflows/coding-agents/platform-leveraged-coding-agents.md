---
domain: ai-workflows
subdomain: coding-agents
concept: platform-leveraged-coding-agents
title: Monzo's Agent Ship: Building an Internal Coding Agent on Existing Platform Foundations
sources:
  - title: "A Bank Built Its Own Coding Agent. It Took Off — Felipe Felisola Caso & Francesco Galletta, Monzo"
    url: "https://www.youtube.com/watch?v=adfw3xJBx1o"
    author: "AI Engineer"
    date: "2026-10-20"
---

# Monzo's Agent Ship: Building an Internal Coding Agent on Existing Platform Foundations

Felipe Felisola Caso and Francesco Galletta describe how Monzo, a digital bank operating over 3,000 backend services, ~13,000 data warehouse models, and dozens of ML prediction models, built an internal LLM-powered coding agent called Agent Ship. It began as a Slack bot triggered by a custom emoji reaction that could answer questions, review code, and pick up Linear tickets, and it went viral internally after launching in a dedicated Slack channel. Today it generates over 10% of all merged PRs across the technology department, completes over 1,800 tasks per day, and is increasingly used by business users for queries and business questions.

The core argument is that the agent's success came not from the LLM itself but from Monzo's existing platform. The speakers reinterpret "LLM" as "lots of little multipliers" — notifications, monitoring, third-party integrations, staging environments, queues, easy deployment, and database abstractions — all of which the agent could compose. This platform leverage is what let Agent Ship be built quickly and efficiently.

Before Agent Ship existed as a remote agent, Monzo invested in supporting coding agents in on-premises environments. They built an MCP gateway exposing internal services and knowledge sources behind an MCP server for deterministic behavior, with managed authorization and authentication for many different agents. On top of that, an agent orchestration system runs Agent Ship in a sandbox with strict tools and permissions, reflecting the principle that more safely-provided context and data yields better agents.

- Agent Ship generates over 10% of merged PRs across Monzo's technology department and completes 1,800+ tasks per day, spanning data, ML, backend, and application work.
- The speakers credit Monzo's existing platform (notifications, monitoring, staging, queues, deployment, database abstractions) as the real enabler — "LLM" as "lots of little multipliers."
- An MCP gateway exposes internal services and knowledge sources with deterministic behavior and managed auth for multiple agents, originally to support local coding agents.
- Agent Ship runs via an orchestration system in a sandbox with strict tools and permissions, following the principle that more safely-provided context improves agent performance.
- The agent evolved from an emoji-triggered Slack bot into a colleague-like assistant used for code review, ticket execution, and business-user queries.