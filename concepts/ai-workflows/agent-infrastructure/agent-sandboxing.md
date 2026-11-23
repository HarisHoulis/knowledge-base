---
domain: ai-workflows
subdomain: agent-infrastructure
concept: agent-sandboxing
title: Google Agent Compute Engine for Secure AI Agent Execution
sources:
  - title: "Google Announces Agent Compute Engine for Secure AI Agent Execution"
    url: "https://www.infoq.com/news/2026/11/google-agent-compute-engine/"
    author: "Renato Losio"
    date: "2026-11-22"
---

# Google Agent Compute Engine for Secure AI Agent Execution

Google announced Agent Compute Engine, a managed service that executes AI agents inside isolated microVMs, providing a hardened boundary around agent workloads. The service also supports checkpointing, allowing execution environments to be suspended and resumed rather than rebuilt from scratch.

A key security design choice is that sensitive material—credentials, API keys, and OAuth refresh tokens—is kept outside the agent sandbox. Instead, an external Agent Gateway authenticates requests and injects the required secrets, so agents never hold long-lived secrets directly.

Together these features address two practical problems of running agents in production: containing untrusted or unpredictable agent behavior, and managing secret exposure while preserving stateful, resumable execution.

- Agents run in isolated microVMs managed by Google's Agent Compute Engine.
- Checkpointing lets execution environments be suspended and resumed.
- Credentials, API keys, and OAuth refresh tokens live outside the agent sandbox.
- An external Agent Gateway authenticates requests and injects secrets.