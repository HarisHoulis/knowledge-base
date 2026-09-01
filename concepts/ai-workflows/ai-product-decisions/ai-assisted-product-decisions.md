---
domain: ai-workflows
subdomain: ai-product-decisions
concept: ai-assisted-product-decisions
title: Use AI to make product decisions
sources:
  - title: "Use AI to make product decisions"
    url: "https://www.youtube.com/watch?v=2cTv5JSVvDc"
    author: "Kent C. Dodds"
    date: "2026-08-11"
---

# Use AI to make product decisions

In this video, Kent C. Dodds demonstrates how to use an AI agent (Cody) to make product decisions by researching external sources and analyzing their implications. He shares a Cloudflare Agent Week blog post about 'Cloudflare computer', a primitive that provides an agent runtime where code execution across isolates, containers, and web browsers is handled by the platform (Kent C. Dodds, 2026). The agent evaluates this new feature against Cody's existing primitives and recommends adding a workspace assistant primitive, which would allow agents to work on remote computers via MCP—not just during interactive sessions but through triggers and other automated workflows. This highlights how product decisions revolve around primitives, and how platforms like Cloudflare enable building cleaner abstractions on top of foundational primitives.

Additionally, Dodds explains the two tracks for repo sessions in Cody: one where coding agents clone, modify, and push repositories, and another where MCP commands are used to simulate git operations for updates outside the coding agent context. This distinction matters when considering how new platform features like Cloudflare computer could enhance both tracks. The overall message is that AI agents can serve as effective research and decision-support tools when given the right context and primitives (Kent C. Dodds, 2026).

- AI agents can be used to research external sources and synthesize their implications for product decisions.
- Product decisions should focus on primitives—platform features that can be built upon to offer cleaner abstractions.
- New platform primitives (e.g., Cloudflare computer) can inspire new product features (e.g., a workspace assistant primitive in Cody).
- Cody supports repo sessions in two ways: via coding agents that clone/modify/push, and via MCP-based commands for external updates.