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

In a YouTube short, Matt Pocock (2026) demonstrates that Claude Code's default system prompt is bloated with unused tools and features, amounting to roughly 25,000 tokens. He shows how to dramatically reduce this by customizing the global settings.json file, bringing the system prompt down to approximately 8,000 tokens. This is achieved by disabling features and tools that are not needed for a given workflow.

- Claude Code's default system prompt can be around 25,000 tokens.
- Customizing the global settings.json file allows disabling unused tools and features.
- This reduces the system prompt size to roughly 8,000 tokens.
- A written guide is referenced for step-by-step details.