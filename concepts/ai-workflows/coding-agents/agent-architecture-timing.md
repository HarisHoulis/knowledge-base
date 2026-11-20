---
domain: ai-workflows
subdomain: coding-agents
concept: agent-architecture-timing
title: What It Takes to Set Intelligence Free: Lessons from Lovable's Agent Journey
sources:
  - title: "What it takes to set intelligence free — Fabian Hedin, CTO, Lovable"
    url: "https://www.youtube.com/watch?v=pZWPq_ZAmM4"
    author: "AI Engineer"
    date: "2026-11-19"
---

# What It Takes to Set Intelligence Free: Lessons from Lovable's Agent Journey

Fabian Hedin, co-founder and CTO of Lovable, recounts how his company nearly went bankrupt in 2023 after betting on multi-agent architectures before the underlying models were capable enough. Building on GPT-4, Lovable's first product (GPT Engineer) used a single LLM call per user message and worked well for simple single-page sites, but the team assumed intelligence would grow and preemptively built a sophisticated multi-agent framework with a main orchestrator agent delegating to specialized implementation, frontend, and backend agents that exchanged messages. The framework made the product worse, and the company reverted at the end of 2024 to a simpler system of smaller LLMs for knowledge retrieval plus one main LLM generating code in a single message, which was responsive and robust.

Hedin argues the timing was the problem, not the direction: in 2023 intelligence alone wasn't enough to support complex agent systems, but now it is, and Lovable is running agents in production at over a billion tokens per minute. He frames Lovable's core thesis as abstraction over code—users describe intent in a chat and see a preview, working at the architecture or results level rather than reading code daily, because what matters is the outcome (building a business, monetizing, creating value), not the code itself.

The platform pairs a general-purpose coding agent (with browser access for testing and GitHub integration) with cloud and business components: authentication, databases, storage, backend compute, security scanners, backups, and logs, all auditable by the agent so users don't have to stitch together separate services.

- Building multi-agent orchestration before models are capable enough can degrade a product—Lovable nearly went bankrupt on a 2023 agent framework that made things worse than a single LLM call.
- The simpler 2024 architecture (small retrieval LLMs plus one main code-generating LLM) was more responsive and robust, and agents only became viable again once model intelligence caught up.
- Lovable's thesis is that developers increasingly work at the architecture/results level rather than reading code, since outcomes matter more than the code itself.
- The platform bundles a coding agent with cloud primitives (auth, databases, storage, compute, security scanning, backups, logs) that the agent can audit, avoiding service-by-service setup.
- Agents are now in production at over a billion tokens per minute.