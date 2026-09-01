---
domain: ai-workflows
subdomain: agent-interoperability
concept: shared-agent-home
title: How Kody Gives Your Agents a Shared Home
sources:
  - title: "How Kody Gives Your Agents a Shared Home"
    url: "https://www.youtube.com/watch?v=h5G8uaZHrVI"
    author: "Kent C. Dodds"
    date: "2026-08-27"
---

# How Kody Gives Your Agents a Shared Home

Cody acts as a shared home for AI agents like Cursor, Grok, and Devin, enabling them to operate together, communicate, and share an ecosystem of software and context. The core idea is structuring your agent setup so you can context-switch between different agents while they all access a common repository of memories, tasks, secrets, and tools. This is achieved through a Model Context Protocol (MCP) server that agents consult when they need information beyond their fresh context windows (Dodds, 2026).

When an agent like Cursor needs to answer a question, it searches Cody via the MCP server, providing a memory context and a query. The search returns a conversation ID, which associates subsequent tool calls together, along with relevant memories and entities such as secrets. For instance, if an agent needs to check what a favorite bot shipped on GitHub, Cody can surface a GitHub access token descriptor and relevant memories. The agent then writes code using a template syntax for secrets, and Cody executes that code in an isolated worker environment, swapping in the actual secret only when the request is allowed to the target domain. This ensures the agent never directly accesses raw secrets, as it only sees the secret's name (Dodds, 2026).

Cody's isolated worker environment spins up in milliseconds, allowing dynamic code execution while maintaining security boundaries. The system is designed so that agents can operate together with a shared home, avoiding the fragmentation of context across different tools. This approach gives agents a persistent, shared memory and task space, making it easier to move between them without losing continuity (Dodds, 2026).

- Cody provides a shared home for multiple AI agents, enabling them to cooperate and share context, memories, and software.
- Agents use an MCP server to search Cody's shared memory and secrets, receiving a conversation ID to link related tool calls.
- Secrets are managed securely: agents write template placeholders, and Cody swaps in real secrets during isolated execution, so agents never see raw credentials.
- The isolated worker environment runs code quickly (milliseconds), allowing dynamic actions like fetch calls while enforcing domain-level secret permissions.
- This structure supports seamless context switching between agents for different tasks, creating a unified ecosystem.