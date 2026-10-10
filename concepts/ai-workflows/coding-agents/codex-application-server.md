---
domain: ai-workflows
subdomain: coding-agents
concept: codex-application-server
title: Building on the Codex Harness
sources:
  - title: "Building on the Codex Harness — Dominik Kundel, OpenAI"
    url: "https://www.youtube.com/watch?v=9WiBJRO84yY"
    author: "AI Engineer"
    date: "2026-10-09"
---

# Building on the Codex Harness

Dominik Kundel, working on developer experience for Codex at OpenAI, explains how developers can build their own agent interfaces on top of the Codex harness rather than starting from scratch. The Codex application server is a protocol that wraps the Codex shell, conceptually similar to the Agent Client Protocol (ACP), and both the shell and the application server are open source under an Apache 2 license, so developers can fork, modify, and even connect it to other model providers whose APIs are compatible with the Responses API, including convenient settings for LM Studio or Ollama.

The application server is a JSON-RPC-style protocol that OpenAI itself uses to run the Codex app, the IDE extension, and the VS Code extension, as well as third-party interfaces. Kundel notes that Codex through Xcode, JetBrains IDEs, and open source projects like Theos T3 Code or Remote X all run on the same foundation, and that OpenAI used it earlier in the year to implement Codex in Cloud Code, letting users review code or assign tasks through a plugin backed by the same application server.

The protocol works by exchanging messages between the client (the application being built) and the server (the Codex application server) to perform actions and receive events. To demonstrate, Kundel built an inspector that intercepts all events between the real Codex application and the Codex application server, showing real messages such as thread configuration, project context, configuration reads, new thread starts, and streamed delta messages. The protocol's flexibility comes from opening access to everything in the application and its key functionality, so streaming data and file searches are all transferred between the application server and the application itself. There are currently over 120 different client messages, covering initialization with client-specific parameters, changing threads and queues, setting goals for custom goal modes, and listing plugins.

- The Codex application server is a JSON-RPC-style protocol wrapping the open source Codex shell, similar in concept to ACP.
- OpenAI uses the same application server for its own Codex app, IDE extensions, and third-party integrations like Xcode, JetBrains, and Cloud Code.
- The protocol exposes over 120 client messages covering initialization, threads, queues, goals, and plugins.
- Developers can connect the harness to other model providers with Responses API-compatible APIs, including LM Studio and Ollama.