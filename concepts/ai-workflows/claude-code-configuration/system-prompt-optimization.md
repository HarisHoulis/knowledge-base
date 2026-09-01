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
---

# Claude Code's system tools are SO BLOATED

Matt Pocock demonstrates that Claude Code's system prompt is often unnecessarily large, defaulting to around 25,000 tokens because every system tool is enabled out of the box. He explains that most users only need a fraction of these tools, and keeping the rest active adds significant bloat to the prompt, which can impact performance and cost.

By customizing the global settings.json file, users can disable unused features and tools, shrinking the system prompt dramatically. Pocock shows a real example where the prompt size drops from 25,000 tokens to just 8,000 tokens—a 68% reduction—simply by turning off tooling that isn't relevant to a typical workflow.

The video points to a written guide for step-by-step instructions, and emphasizes that this kind of configuration is an easy win for anyone using Claude Code on a regular basis. The key takeaway is that default setups are not optimized for individual use cases, and a little upfront configuration can yield major efficiency gains.

- Claude Code's default system prompt can be as large as 25,000 tokens due to all system tools being enabled.
- Most users do not need every tool, and unused tools contribute to unnecessary bloat.
- Editing the global settings.json file to disable unused features reduces the prompt to around 8,000 tokens.
- This represents a 68% reduction in system prompt size, improving efficiency and lowering token usage.