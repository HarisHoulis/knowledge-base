---
domain: ai-workflows
subdomain: coding-agents
concept: external-sandbox-pattern
title: External Sandboxes for Coding Agents
sources:
  - title: "External sandboxes for coding agents"
    url: "https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/"
    author: "Simon Willison"
    date: "2026-11-17"
---

# External Sandboxes for Coding Agents

Simon Willison describes work with Prime Radiant on the "external sandbox" pattern, in which code executed by a coding agent runs inside a dedicated sandbox while the agent itself lives outside that sandbox. This separates the untrusted code execution surface from the agent process.

To demonstrate the pattern, three sandbox server implementations were released, each exposing the same localhost API. Agents such as Pi, Claude Code, or Codex can be configured to send API calls to that sandbox whenever they want to execute code.

The sandboxes also include an optional HTTP/HTTPS allow-list proxy for controlling which hosts the agent's code may contact, plus a credential replacement mechanism that enables authenticated API calls without sharing a secret with the agent. The proxy can be reconfigured via a UI while the sandbox is still running. Willison frames this as a way to experiment with different approaches to safely running untrusted code.

- External sandbox pattern keeps the agent outside the sandbox while its executed code runs inside it
- Three sandbox server implementations share a common localhost API usable by Pi, Claude Code, and Codex
- An optional HTTP/HTTPS allow-list proxy restricts which hosts agent code can reach
- Credential replacement allows authenticated API calls without exposing secrets to the agent
- The proxy can be reconfigured at runtime through a UI