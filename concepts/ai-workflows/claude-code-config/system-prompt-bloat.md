---
domain: ai-workflows
subdomain: claude-code-config
concept: system-prompt-bloat
title: Reducing Claude Code System Prompt Bloat
sources:
  - title: "Claude Code's system tools are SO BLOATED"
    url: "https://www.youtube.com/shorts/oLx4yCbeklQ"
    author: "Matt Pocock"
    date: "2026-07-16T10:20:06+00:00"
---

# Reducing Claude Code System Prompt Bloat

The video demonstrates that Claude Code's default system prompt contains many unused tools and features, resulting in a bloated system prompt of around 25,000 tokens. This bloat can slow down interactions and consume context window unnecessarily. By customizing the global settings.json file, users can disable these unnecessary features and tools, dramatically reducing the system prompt size to as low as 8,000 tokens. The optimization focuses on retaining only the tools and capabilities actually needed for the user's workflow, leading to more efficient AI interactions and lower token usage.

- Claude Code's default system prompt includes many tools that are not commonly used, causing bloat.
- System prompt size can be reduced from 25,000 tokens to about 8,000 tokens via settings customization.
- Disabling unused features helps improve performance and reduce token consumption.
- The optimization is done through editing the global settings.json file for Claude Code.