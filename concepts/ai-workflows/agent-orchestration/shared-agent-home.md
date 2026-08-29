---
domain: ai-workflows
subdomain: agent-orchestration
concept: shared-agent-home
title: How Kody Gives Your Agents a Shared Home
sources:
  - title: "How Kody Gives Your Agents a Shared Home"
    url: "https://www.youtube.com/watch?v=h5G8uaZHrVI"
    author: "Kent C. Dodds"
    date: "2026-08-27T22:09:03+00:00"
---

# How Kody Gives Your Agents a Shared Home

In this video, Kent C. Dodds introduces Cody, a tool designed to give AI agents a shared home, enabling them to operate together, communicate, and maintain a common ecosystem of software, memories, and tasks. The core idea is to solve the context-switching problem: users can freely move between different agents (such as Cursor, Grok, and Devin) without losing context, because all agents can access a central repository of shared information via Cody (Dodds, 2026).

Cody functions as an MCP server that agents query when they need information. For example, when Cursor needs to know what a user's favorite bot shipped on GitHub, it searches Cody for relevant secrets, packages, webhooks, and memories. The search returns a conversation ID, memory context, and search results, allowing Cursor to refine its actions. This metaphorically lets each agent "enter the user's home" and retrieve whatever it needs, whether that's a GitHub access token or a memory about a preferred bot (Dodds, 2026).

Security is handled through an isolated execution environment. When an agent writes code to perform an action, it runs in a sandboxed worker. Secret placeholders in the code are resolved by Cody in the secure worker context, so the agent itself never directly accesses sensitive values. This allows agents to execute arbitrary code while keeping secrets confidential, and the worker environment spins up in milliseconds, making the process efficient (Dodds, 2026).

- Cody provides a shared home for multiple AI agents, allowing them to share memories, tasks, and software context.
- Agents use Cody as an MCP server to search across secrets, packages, webhooks, and memories.
- Conversation IDs and memory context maintain state across different agents and tool calls.
- Code execution happens in an isolated worker environment, with secrets resolved server-side so agents never see raw credentials.
- This setup reduces context-switching friction and enables a seamless multi-agent workflow.