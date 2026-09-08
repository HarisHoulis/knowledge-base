---
domain: ai-workflows
subdomain: agent-integrations
concept: sandboxed-agent-runtime
title: Introducing Kody: Your Personal Software Factory
sources:
  - title: "Introducing Kody: Your Personal Software Factory"
    url: "https://kentcdodds.com/blog/introducing-kody-your-personal-software-factory"
    date: "2026-09-08"
---

# Introducing Kody: Your Personal Software Factory

The article highlights common pain points with the proliferation of AI coding agents: fragmented integrations, walled gardens, repeated setup, and the risk of exposing secrets in .env files. The author introduces Kody, a cloud-based sandboxed runtime where agents can author and execute code. Kody provides built-in and generic OAuth support and MCP server connectivity, enabling agents to interact with any API through ad hoc code that runs in an isolated environment.

Kody addresses the walled garden problem by making integrations available across all agents, so users do not need to reconfigure automations and memories for each tool. Once an agent creates a useful script, it can be turned into a durable Kody-hosted package with its own SQLite database, scheduled jobs, webhooks, or full web apps. Packages are reusable by any agent and can be published to a public community for forking. Secret storage is encrypted and isolated, preventing agents from reading secrets even while allowing them to use integration credentials, making it safer than a .env file. The author describes using Kody to control home devices via MCP and integrating it with tools like Stripe, Cursor, Cloudflare, Sentry, and Kit.

- Kody is a sandboxed cloud runtime that lets AI agents write and execute code with API integrations, OAuth, and MCP.
- It solves the multi-agent walled garden problem by unifying integrations so users do not need to set them up separately for each agent.
- Ad hoc agent code can be compiled into durable packages with databases, scheduled jobs, webhooks, and web apps.
- Encrypted secrets are stored in an isolated database and are not visible or exfiltratable by agents, reducing .env leakage and prompt-injection risks.
- The article announces a free public launch and a community ecosystem of forkable packages.