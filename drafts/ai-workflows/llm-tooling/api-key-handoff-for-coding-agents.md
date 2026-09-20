---
domain: ai-workflows
subdomain: llm-tooling
concept: api-key-handoff-for-coding-agents
title: llm-keys-ui 0.1: Saving API Keys for Remote Coding Agents Without Pasting Them Into Chat
sources:
  - title: "llm-keys-ui 0.1"
    url: "https://simonwillison.net/2026/Sep/20/llm-keys-ui/"
    author: "Simon Willison"
    date: "2026-09-20"
  - title: "llm-keys-ui 0.1 release"
    url: "https://github.com/simonw/llm-keys-ui/releases/tag/0.1"
    author: "Simon Willison"
    date: "2026-09-20"
---

# llm-keys-ui 0.1: Saving API Keys for Remote Coding Agents Without Pasting Them Into Chat

llm-keys-ui 0.1 is a plugin by Simon Willison that solves a narrow problem: getting API keys onto remote machines running coding agents without pasting the keys directly into an agent session [llm-keys-ui 0.1]. The motivation came from using Codex Remote to run coding agents on various machines while controlling them from a phone, where hacking on LLM projects occasionally requires configuring an API key [llm-keys-ui 0.1].

The workflow is a two-step handoff. First, the agent is told to run `uvx --with llm-keys-ui llm keys-ui --all`, which reports a URL — including local network or Tailscale device IPs — for a web interface where the user can save additional API keys [llm-keys-ui 0.1]. The user supplies the key through that interface rather than typing it into the ChatGPT app [llm-keys-ui 0.1].

Second, the agent can later retrieve the key at use time with a command such as `llm keys get anthropic` as part of a shell command [llm-keys-ui 0.1]. The design keeps the secret out of the agent conversation while still making it available to the agent's shell.

- llm-keys-ui 0.1 is a plugin for handing API keys to remote coding-agent machines without pasting them into an agent session
- The agent runs `uvx --with llm-keys-ui llm keys-ui --all` to start a web UI, reachable via local network or Tailscale IPs, for saving keys
- Keys are later consumed by the agent through shell commands like `llm keys get anthropic`
- The motivating setup is Codex Remote driving coding agents on multiple machines from a phone