---
domain: ai-workflows
subdomain: multi-agent-context
concept: shared-agent-home
title: How Kody Gives Your Agents a Shared Home
sources:
  - title: "How Kody Gives Your Agents a Shared Home"
    url: "https://www.youtube.com/watch?v=h5G8uaZHrVI"
    author: "Kent C. Dodds"
    date: "2026-08-27T22:09:03+00:00"
---

# How Kody Gives Your Agents a Shared Home

In this video, Kent C. Dodds introduces Cody (Kody) as a shared home for multiple AI agents, allowing them to operate together, communicate, and share an ecosystem of software, memories, and tasks. The core idea is that users can context-switch between agents like Cursor, Grok, and Devin without losing continuity, because all agents access a common layer that holds persistent knowledge and resources.

Cody acts as an MCP (Model Context Protocol) server that agents query for memories, secrets, packages, webhooks, and other entities. For example, when Cursor needs to know what a favorite bot shipped on GitHub, it searches Cody's memory and discovers relevant secrets like a GitHub token. A notable security feature is that agents never directly access secrets; instead, they write code with template references, and Cody swaps in the actual secret during execution in an isolated environment (Kent C. Dodds, 2026).

Agents use a conversation ID to associate related tool calls within the shared home, making searches and executions more efficient. The isolated worker environment spins up in milliseconds, allowing dynamic execution of agent-authored code while enforcing secret-domain policies. This design enables a seamless multi-agent workflow where different tools can collaborate and share context through a central, secure hub.

- Cody provides a shared home for multiple agents, enabling context switching and inter-agent communication.
- Agents query Cody via an MCP server to access shared memories, secrets, and other entities.
- Secrets are never exposed to agents directly; they are substituted by Cody during execution in a secure, isolated environment.
- Conversation IDs link multiple tool calls across agents, improving efficiency and coherence.
- The isolated execution environment spins up in milliseconds and enforces domain-based secret access policies.