---
domain: ai-workflows
subdomain: claude-code-configuration
concept: reduce-agent-system-prompt-bloat
title: Reducing Claude Code's System Prompt Bloat
sources:
  - title: "Claude Code's system tools are SO BLOATED"
    url: "https://www.youtube.com/shorts/oLx4yCbeklQ"
    author: "Matt Pocock"
    date: "2026-07-16T10:20:06+00:00"
---

# Reducing Claude Code's System Prompt Bloat

Claude Code's default system prompt includes a large set of tools and features that are often unnecessary for day-to-day coding work. The prompt can balloon to approximately 25,000 tokens, which consumes context window and slows down responses. Matt Pocock demonstrates that by disabling unused features and tools via the global settings.json file, the system prompt can be reduced to just 8,000 tokens—a 68% reduction. This optimization is achieved by customizing the agent's configuration to strip out capabilities that the user doesn't need, striking a balance between powerful defaults and lean, focused prompts. The video provides a practical walkthrough for editing the settings file, and links to a detailed guide and community resources for further exploration.

- Default Claude Code system prompt can be around 25,000 tokens.
- Disabling unused tools and features in settings.json dramatically reduces prompt size.
- The example shows a reduction from 25,000 to 8,000 tokens.
- Smaller system prompts save context window and improve response speed.