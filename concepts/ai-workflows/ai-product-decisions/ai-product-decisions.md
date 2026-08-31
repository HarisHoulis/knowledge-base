---
domain: ai-workflows
subdomain: ai-product-decisions
concept: ai-product-decisions
title: Use AI to make product decisions
sources:
  - title: "Use AI to make product decisions"
    url: "https://www.youtube.com/watch?v=2cTv5JSVvDc"
    author: "Kent C. Dodds"
    date: "2026-08-11T15:20:14+00:00"
---

# Use AI to make product decisions

In this episode, Kent C. Dodds demonstrates how to use an AI agent (Cody) to make product decisions. He provides the agent with a link to a post about Cloudflare Agent Week, and the agent analyzes it in the context of the Cody repository, identifying opportunities for new built-in features. The discussion centers on 'primitives'—the foundational building blocks that platforms expose—and how Cloudflare's new 'computer' package offers an agent runtime that abstracts away where code runs (isolate, container, or browser). The agent suggests adding a workspace assistant primitive, which would allow the Cody agent to work on a remote computer via MCP, extending beyond the typical session-based interactions. This example illustrates how AI can be used to quickly synthesize external information and propose actionable product improvements (Kent C. Dodds, 2026).

The video also explains how Cody currently handles repo sessions: coding agents can clone repositories and make changes, but for updates outside that context, repo sessions parse commands via MCP to simulate actions. This context helps clarify why new primitives like the workspace assistant are valuable—they enable richer remote interactions. The key takeaway is to continuously think in terms of primitives when making product decisions, and to leverage AI agents to explore and integrate new platform capabilities efficiently.

- AI agents can analyze external content (e.g., blog posts) and propose product opportunities.
- Product decisions should revolve around primitives—the core building blocks of a platform.
- Cloudflare's 'computer' package provides an agent runtime that abstracts execution environments.
- New capabilities should map to existing workflows, such as extending Cody's repo sessions via MCP.
- Understanding current primitives helps evaluate which new features are feasible and impactful.