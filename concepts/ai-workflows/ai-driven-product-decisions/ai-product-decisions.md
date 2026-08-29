---
domain: ai-workflows
subdomain: ai-driven-product-decisions
concept: ai-product-decisions
title: Use AI to make product decisions
sources:
  - title: "Use AI to make product decisions"
    url: "https://www.youtube.com/watch?v=2cTv5JSVvDc"
    author: "Kent C. Dodds"
    date: "2026-08-11T15:20:14+00:00"
---

# Use AI to make product decisions

In this talk, Kent C. Dodds demonstrates how to use an AI agent to make product decisions by handing it a link to a Cloudflare Agent Week blog post. The post argues that 'your agent needs a computer, not a container,' introducing Cloudflare Computer as a primitive that abstracts whether code runs in an isolate, container, or browser. Dodds highlights the importance of primitives in product thinking, noting that Cloudflare's platform exposes clean building blocks that can be composed into higher-level offerings (Dodds, 2026).

Dodds then walks through how his agent (Cody) analyzed the blog post and identified opportunities for Cody, which runs on Cloudflare. The agent suggested a new 'workspace assistant' primitive—essentially a remote computer accessible via MCP—that would allow agents to handle tasks outside interactive sessions, such as through triggers. This would improve repo sessions by complementing the existing two tracks: coding agents that clone/modify/push repos, and repo sessions that parse MCP commands to simulate git operations (Dodds, 2026).

The core takeaway is that AI agents can be leveraged not just for coding, but for strategic product analysis and decision-making. By feeding an agent external information and asking it to map opportunities to existing capabilities, teams can quickly generate actionable product insights. Dodds also emphasizes that thinking in primitives—and aligning product features with platform primitives—is a durable skill for building on evolving infrastructure (Dodds, 2026).

- Use AI agents to analyze external content and surface product opportunities relevant to your platform.
- Cloudflare's 'agent needs a computer, not a container' concept reframes runtime abstraction as a primitive.
- Product decisions should revolve around primitives and the capabilities they enable.
- Cody could add a 'workspace assistant' primitive via MCP for remote agent work, enhancing repo sessions.
- Cody has two repo interaction tracks: coding-agent-driven changes and MCP-based repo sessions.