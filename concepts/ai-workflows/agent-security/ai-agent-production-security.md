---
domain: ai-workflows
subdomain: agent-security
concept: ai-agent-production-security
title: Securing AI Agents in Production
sources:
  - title: "QCon San Francisco 2026: Securing AI Agents in Production"
    url: "https://www.infoq.com/news/2026/11/qcon-ai-agent-security/"
    author: "Mark Silvester"
    date: "2026-11-23"
---

# Securing AI Agents in Production

At QCon San Francisco 2026, Google's Amanda Walker framed AI agents as an insider-risk problem operating at machine speed, arguing that agents must be treated less like trusted tools and more like potentially compromised insiders. The talk focused on identity, credential, and containment patterns for running agents safely in production.

The core concern is that agents act autonomously and quickly, so traditional perimeter-based trust assumptions break down. Walker's framing suggests applying least-privilege identity and scoped credentials to agents, and containing their blast radius so that a misbehaving or manipulated agent cannot escalate privileges or act broadly across systems.

- Treat AI agents as insider-risk actors operating at machine speed, not as trusted tools
- Apply identity and credential patterns that limit what each agent can access
- Use containment patterns to bound the blast radius of agent actions in production