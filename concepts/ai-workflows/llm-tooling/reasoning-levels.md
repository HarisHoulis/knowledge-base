---
domain: ai-workflows
subdomain: llm-tooling
concept: reasoning-levels
title: llm-gemini 0.38.1: Fixing xhigh Reasoning Level Support
sources:
  - title: "llm-gemini 0.38.1"
    url: "https://simonwillison.net/2026/Nov/20/llm-gemini/"
    author: "Simon Willison"
    date: "2026-11-20"
---

# llm-gemini 0.38.1: Fixing xhigh Reasoning Level Support

Simon Willison released llm-gemini 0.38.1 to fix a missing `xhigh` reasoning level for the Gemini 4 Hydrogen and Gemini 4 Neon models in the llm-gemini plugin. Gemini 4 Carbon only supports `low`, `medium`, and `high` levels, while Hydrogen and Neon each have an extra `xhigh` level that was overlooked when the models were added.

The impact of `xhigh` is substantial for Hydrogen. In Willison's updated Gemini 4 comparison grid, Hydrogen at `high` used 5,311 output tokens and cost 3.99 cents, whereas the same model at `xhigh` used 31,477 output tokens, cost 23.61 cents, and produced a pelican image competitive with Gemini 4 Neon.

- Gemini 4 Carbon supports only low/medium/high reasoning levels; Hydrogen and Neon add an xhigh level
- llm-gemini 0.38.1 fixes the missing xhigh support for Hydrogen and Neon
- Hydrogen at xhigh used ~6x the output tokens and cost ~6x more than at high (31,477 tokens / 23.61 cents vs 5,311 tokens / 3.99 cents)
- The xhigh setting noticeably improved Hydrogen's output quality, rivaling Gemini 4 Neon