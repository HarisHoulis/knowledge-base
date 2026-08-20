---
domain: ai-workflows
subdomain: claude-code-optimization
concept: system-prompt-bloat-reduction
title: Claude Code's system tools are SO BLOATED
sources:
  - title: "Claude Code's system tools are SO BLOATED"
    url: "https://www.youtube.com/shorts/oLx4yCbeklQ"
    author: "Matt Pocock"
    date: "2026-07-16"
---

# Claude Code's system tools are SO BLOATED

Matt Pocock highlights that Claude Code's default system prompt is heavily bloated, containing numerous tools and features that many users never use. This bloat inflates the token count and adds unnecessary overhead to every request. By customizing the global settings.json file, users can disable unused features and dramatically reduce the system prompt size (Pocock, 2026).

Pocock demonstrates a concrete reduction from roughly 25,000 tokens down to just 8,000 tokens, a 68% decrease. This optimization makes the system prompt leaner, which can improve efficiency and lower token usage costs. A step-by-step guide is provided for users who want to apply the same configuration changes to their own Claude Code setup (Pocock, 2026).

- Claude Code's default system prompt can be around 25,000 tokens due to bloat.
- Disabling unused tools and features in global settings.json significantly reduces system prompt size.
- A practical example drops the prompt from 25,000 to 8,000 tokens.
- A leaner system prompt reduces overhead and token consumption.
- A detailed guide is available at aihero.dev/s/D9UXCK.