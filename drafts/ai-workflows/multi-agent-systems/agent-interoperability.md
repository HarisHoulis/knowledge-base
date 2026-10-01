---
domain: ai-workflows
subdomain: multi-agent-systems
concept: agent-interoperability
title: Your Agents Are in Solitary Confinement: Why MCP & A2A Aren't Enough
sources:
  - title: "Your Agents Are in Solitary Confinement: Why MCP & A2A Aren't Enough — Vlad Luzin, Band"
    url: "https://www.youtube.com/watch?v=UOcHfR3_tys"
    author: "Vlad Luzin"
    date: "2026-09-30"
---

# Your Agents Are in Solitary Confinement: Why MCP & A2A Aren't Enough

Vlad Luzin, co-founder and CTO of Band, argues that the future belongs to AI communication within businesses, between businesses, and between consumers and businesses. He envisions autonomous agents written in different frameworks and languages, deployed in different environments, communicating with each other without human intervention. In his picture, agents create conversation spaces, receive tasks from humans or other systems, find and add other agents, exchange messages, solve tasks, and report back (Luzin, 2026).

Current protocols fall short. MCP treats agents as stateless tools, making stateful session-based interaction difficult. A2A is client-server: an agent can send a task to another, but for bidirectional task exchange both must be client and server. Chaining multi-agent calls involves REST API timeouts and requires queues and persistence, and detection is not part of A2A. As a result, developers still act as routers between stateful agents because the agents themselves cannot communicate (Luzin, 2026).

Connecting agents to messaging platforms such as Telegram, Discord, Slack, or WhatsApp takes manual, documented steps—five, seven, eight, or eleven respectively—and usually yields only an agent that can talk to a human. The agents remain unable to see or communicate with each other, a condition Luzin calls digital solitary confinement. He questions whether multi-agent coordination is truly hypothetical or avoidable, and frames the need for real agent-to-agent communication rather than human-mediated orchestration (Luzin, 2026).

- The thesis is that future AI value comes from autonomous agent communication across businesses and consumer interactions.
- MCP treats agents as stateless tools, while A2A is client-server and awkward for bidirectional agent-to-agent tasks.
- Chaining A2A calls brings REST API timeouts, requires queues/persistence, and lacks detection support.
- Today developers act as routers between coding agents because agents cannot directly communicate.
- Connecting agents to Slack, Telegram, Discord, or WhatsApp requires manual multi-step setup and mainly enables human-agent chat, leaving agents in digital solitary confinement.