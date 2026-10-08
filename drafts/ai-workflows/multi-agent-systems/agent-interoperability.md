---
domain: ai-workflows
subdomain: multi-agent-systems
concept: agent-interoperability
title: Why AI Agents Can't Talk to Each Other (Yet)
sources:
  - title: "Why Your AI Agents Can't Talk to Each Other (Yet) — Vlad Luzin, BAND"
    url: "https://www.youtube.com/watch?v=toq-jyGLZDk"
    author: "AI Engineer"
    date: "2026-10-07"
---

# Why AI Agents Can't Talk to Each Other (Yet)

Vlad Luzin, co-founder and CTO of BAND, argues that the future of AI lies in AI-to-AI communication within and between businesses, where autonomous agents distributed around the world delegate tasks, search registries for colleagues, and report back to users. He illustrates this with a vision of agents meeting in a shared conversational space, receiving tasks, inviting other agents, and collecting results on our behalf.

Luzin traces an evolution from adversarial agents — where a human acts as a router between two sessions, one planning and one checking — to "cycle engineering," where Python or TypeScript orchestration code replaces the human router. This shift is motivated by the single-agent bottleneck: transformer limitations such as self-confirmation bias, blurred attention, context fragmentation, and impaired recall mean that even a one- or two-million-token context will not fix performance.

He critiques current interoperability approaches. Messaging platforms like Slack, Teams, Discord, and WhatsApp require manual, multi-step setup (five steps for Telegram, seven for Discord, eight for Slack, eleven for WhatsApp) and still only connect an agent to a person, leaving agents in digital isolation. Protocol-based approaches like MCP and A2A also fall short: MCP uses stateless calls so you cannot revisit a prior agent interaction, A2A is one-way client-server unless both directions are implemented on both sides, chained REST calls cause timeouts, and features like discovery, session state, and queues are missing.

BAND is presented as the company addressing these gaps, though the transcript cuts off before detailing the product.

- The future thesis: autonomous, distributed AI agents will communicate AI-to-AI within businesses, between businesses, and with consumers, delegating tasks on our behalf.
- Multi-agent orchestration evolved from human-as-router adversarial agents to "cycle engineering," where orchestration code replaces the human, driven by the single-agent bottleneck (self-confirmation, blurred attention, context fragmentation, impaired recall).
- Messaging platforms are a poor integration path: connecting an agent requires 5-11 manual steps and only enables agent-to-human, not agent-to-agent, communication.
- Protocols like MCP and A2A are insufficient: MCP is stateless, A2A is one-way client-server requiring both sides to implement client and server, chained REST calls time out, and discovery, session state, and queues are missing.