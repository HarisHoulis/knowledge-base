---
domain: ai-workflows
subdomain: claude-code-configuration
concept: system-prompt-optimization
title: Reducing Claude Code System Prompt Bloat
sources:
  - title: "Claude Code's system tools are SO BLOATED"
    url: "https://www.youtube.com/shorts/oLx4yCbeklQ"
    author: "Matt Pocock"
    date: "2026-07-16T10:20:06+00:00"
---

# Reducing Claude Code System Prompt Bloat

Claude Code's default system prompt includes many tools and features that may be unnecessary for specific workflows, leading to excessive token usage (~25,000 tokens). By customizing the global settings.json file, users can disable unused tools and features, dramatically reducing prompt size to roughly 8,000 tokens. This optimization is especially beneficial for improving efficiency, reducing costs, and maintaining focus on the tasks that matter.

- Default Claude Code system prompt can be around 25,000 tokens, much of it unused.
- Disabling unused tools and features via global settings.json can reduce prompt size to ~8,000 tokens.
- A smaller system prompt improves efficiency and reduces token overhead.