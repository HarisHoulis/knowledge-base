---
domain: ai-workflows
subdomain: ai-agent-security
concept: auto-mode-default
title: Auto mode is now the default in Claude Code for Pro, Max, and Team plans
sources:
  - title: "Auto mode is now the default in Claude Code for Pro, Max, and Team plans"
    url: "https://simonwillison.net/2026/Aug/8/auto-mode/#atom-everything"
    author: "Simon Willison"
    date: "2026-08-08"
---

# Auto mode is now the default in Claude Code for Pro, Max, and Team plans

Claude Code now defaults to auto mode for Pro, Max, and Team plans, a shift that Anthropic claims improves safety by reducing confirmation fatigue. According to Simon Willison's post, Anthropic's own data shows that human reviewers approve dangerous commands 13.6% of the time in a controlled test, whereas auto mode would block 89% of such actions. This suggests that frequent manual approvals lead to complacency, making automated safeguards potentially more reliable than human judgment in routine scenarios (Willison, 2026).

- Auto mode is now the default in Claude Code for Pro, Max, and Team plans, aiming to cut down on confirmation fatigue.
- A test with 1,053 paid testers found 13.6% of humans approved a dangerous command, while auto mode would block 89% of those actions.
- Anthropic claims 720 indirect prompt injection attacks all failed against their latest models in auto mode, but Simon Willison remains skeptical, citing risks from malicious packages that instruct agents to exfiltrate data.
- Willison recommends running agents without access to sensitive data or tools to mitigate potential harm from prompt injection.