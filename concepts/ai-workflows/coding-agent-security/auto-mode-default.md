---
domain: ai-workflows
subdomain: coding-agent-security
concept: auto-mode-default
title: Auto mode is now the default in Claude Code
sources:
  - title: "Auto mode is now the default in Claude Code for Pro, Max, and Team plans"
    url: "https://simonwillison.net/2026/Aug/8/auto-mode/#atom-everything"
    author: "Simon Willison"
    date: "2026-08-08"
---

# Auto mode is now the default in Claude Code

Simon Willison remains skeptical, particularly about indirect prompt injection via malicious third-party packages. He gives an example where a package instructs the agent to run a seemingly benign command that actually exfiltrates data. Willison argues that auto mode cannot fully protect against such malfeasance and recommends running agents without access to data or tools that could be harmful if triggered incorrectly (Simon Willison, 2026).

- Auto mode is now the default for Claude Code users on Pro, Max, and Team plans.
- Anthropic's evals suggest auto mode is safer than human approval: only 13.6% of humans refused a dangerous action, while auto mode blocked 89%.
- A third-party evaluation (Trajectory Labs) reported 0 successes out of 720 indirect prompt injection attacks against Claude Fable 5, Opus 5, and Sonnet 5 in auto mode.
- Skeptics like Simon Willison highlight that auto mode may still be vulnerable to malicious packages that instruct agents to perform harmful actions.
- Recommended defense: restrict agent access to sensitive data and tools to limit potential damage.