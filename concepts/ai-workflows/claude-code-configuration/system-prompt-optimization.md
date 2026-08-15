---
domain: ai-workflows
subdomain: claude-code-configuration
concept: system-prompt-optimization
title: Claude Code's system tools are SO BLOATED
sources:
  - title: "Claude Code's system tools are SO BLOATED"
    url: "https://www.youtube.com/shorts/oLx4yCbeklQ"
    author: "Matt Pocock"
    date: "2026-07-16T10:20:06+00:00"
  - title: "System Prompt Optimization Guide"
    url: "https://aihero.dev/s/D9UXCK"
    author: "Matt Pocock"
    date: "2026-07-16"
---

# Claude Code's system tools are SO BLOATED

Matt Pocock demonstrates that Claude Code's default system prompt is over 25,000 tokens, largely due to unnecessary tools and features being enabled by default. He shows how to reduce the system prompt to just 8,000 tokens by editing the global settings.json file, which significantly trims bloat and potentially improves model responsiveness and context efficiency.

The process involves identifying which built-in tools and features are unused for typical workflows and disabling them via configuration. The video references a guide at aihero.dev for step-by-step instructions. This optimization is relevant for developers using Claude Code who want to streamline their setup, reduce token overhead, and focus the model on relevant capabilities.

The key takeaway is that Claude Code's system prompt is highly customizable, and modest configuration changes can yield dramatic token savings, improving performance and reducing costs in AI-assisted workflows.

- Claude Code's default system prompt is ~25,000 tokens, with much of it bloat from unused features.
- Disabling unnecessary tools in global settings.json can cut the prompt to ~8,000 tokens.
- Small config changes can significantly improve token efficiency and focus the AI on relevant capabilities.
- A detailed guide is available at aihero.dev for step-by-step customization.