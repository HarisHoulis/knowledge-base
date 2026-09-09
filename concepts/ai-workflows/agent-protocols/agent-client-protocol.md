---
domain: ai-workflows
subdomain: agent-protocols
concept: agent-client-protocol
title: The Universal Remote Control for AI — Alex Hancock, Block
sources:
  - title: "The Universal Remote Control for AI — Alex Hancock, Block"
    url: "https://www.youtube.com/watch?v=YkNulwcc5jk"
    author: "Alex Hancock"
    date: "2026-09-09T16:00:03+00:00"
---

# The Universal Remote Control for AI — Alex Hancock, Block

Alex Hancock, a software engineer at Block and contributor to Goose and MCP, presents a tooling problem: the AI agent ecosystem has many powerful tools but fragmented interfaces, sometimes requiring one specific client application. He argues this is like being forced to use a single browser or protocol on the web, which would have prevented the open web. The essence of standards is that they create ecosystems, as seen with MCP, whose real power is ubiquity — thousands of compatible servers that all agents can connect to (Hancock, 2026).

However, Hancock notes there is still no standard for client software to manage agents: setting tasks, indicating what to work on, and receiving updates. He proposes ACP (Agent Client Protocol), originally developed by the creators of Zed and JetBrains so that an editor could write one client implementation and manage any agent environment. Goose saw broader applicability beyond editors and supports it as an open standards solution. ACP establishes connections between clients and agent environments with negotiation of capabilities, then creates sessions in which user messages are exchanged. The agent can respond with text, images, audio, tool-call updates, and permission requests such as asking the user to approve a tool call. It uses JSON-RPC and is explicitly designed for extensibility: custom methods can be added using an underscore-prefixed convention (Hancock, 2026).

- The AI tool ecosystem lacks a common standard for client-to-agent management, analogous to the browser/protocol fragmentation that would have prevented the open web.
- MCP succeeded because of widespread adoption, giving agents a universal way to call tools, but it does not cover client-driven task management and updates.
- ACP (Agent Client Protocol) originated with Zed and JetBrains to let editors manage any agent with a single client, and Goose adopted it for broader client software.
- ACP uses JSON-RPC for connections, capability negotiation, sessions, agent responses (text/image/audio), tool-call notifications, and permission requests.
- ACP is extensible by design, allowing custom methods through an underscore-prefixed naming convention.