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

In this video, Kent C. Dodds introduces Cody, a tool that gives AI agents a shared home—a central place where they can collaborate, communicate, and share memories, tasks, and software. This enables users to seamlessly context-switch between different agents like Cursor, Grok, and Devin, because each agent can access the same persistent context and resources (Dodds, 2026).

Cody works through an MCP server that agents query when they lack context. For example, when Cursor is asked about a recent GitHub release, it searches Cody's shared memory and secrets. The search returns a conversation ID and relevant memory context, allowing subsequent tool calls to be correlated and efficient. Cody also executes agent-written code in an isolated worker environment, intercepting fetch calls to enforce security policies. Secrets are referenced via templates and swapped in by Cody, so agents never directly expose or access sensitive credentials (Dodds, 2026).

The architecture supports a collaborative ecosystem where agents build and use software together, while maintaining strict security boundaries. The isolated worker spins up in milliseconds, making the shared home fast enough for real-time agent interactions. This approach allows multiple agents to work as a cohesive unit, solving the problem of fragmented context across different tools (Dodds, 2026).

- Cody provides a shared home for AI agents, enabling cross-agent context switching and collaboration.
- Agents use an MCP server to search Cody for memories, secrets, and packages, with conversation IDs tying together related tool calls.
- Code execution happens in an isolated worker environment where fetch calls are intercepted and secrets are securely substituted by Cody.
- The system supports an ecosystem of agents working together while keeping sensitive data inaccessible to any single agent.