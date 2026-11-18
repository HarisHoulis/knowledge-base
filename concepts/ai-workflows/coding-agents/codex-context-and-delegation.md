---
domain: ai-workflows
subdomain: coding-agents
concept: codex-context-and-delegation
title: New Ways of Working with Codex
sources:
  - title: "New Ways of Working with Codex — Dominik Kundel & Charlie Guo, OpenAI"
    url: "https://www.youtube.com/watch?v=IPh9YsWvDQk"
    author: "AI Engineer"
    date: "2026-11-17"
---

# New Ways of Working with Codex

Dominik Kundel and Charlie Guo of OpenAI's development team present recent Codex developments, arguing that Codex is not dead but "available more than ever, in more places, and with more features than ever before." A major shift is Codex's merger with ChatGPT, which let tens of millions of users work with long-term agents, and Codex now underpins ChatGPT, the ChatGPT CLI, Slack, Docs, and a new Agent API. They note Codex's first version was a cloud-based agent running in its own environment, and that the team is gradually returning to that model with better tools for remotely managing Codex and more powerful cloud environments.

The talk frames context as the most important input for a coding agent. Beyond the last two years of "context engineering," they describe moving toward "vague hints"—communicating with an agent as you would with a colleague who already has the context, rather than dictating every detail. Because OpenAI works in a huge monorepo, Codex must navigate giant repositories and find "a needle in a haystack." Context also extends beyond code: repository standards (agents.md files, linters) should be added directly to the repo so a qualified engineer—or agent—can work without errors, while context outside the repository is supplied via plugins combining MCP servers, skills, and additional resources.

The presenters outline the session's themes: context, iteration with long-acting agents to get the right result ("not everything is a cool one-time demo"), working with Codex everywhere (on-premises, cloud, remote), going from idea to production, delegation with subagents and different form factors, and practical tips for daily work.

- Codex merged with ChatGPT, giving tens of millions of users access to long-term agents; it now underpins ChatGPT, the CLI, Slack, Docs, and a new Agent API.
- Context is the key enabler: the team is moving from heavy context engineering toward "vague hints" that assume shared context, like talking to a colleague.
- Repository standards (agents.md, linters) should live in the repo so agents, like qualified engineers, can work without errors; out-of-repo context comes via plugins combining MCP servers and skills.
- Codex's first version was a cloud-based agent, and the team is returning to remote/cloud operation with better remote-management tooling.
- Long-running iteration and delegation (subagents, different form factors) matter more than one-off demos.