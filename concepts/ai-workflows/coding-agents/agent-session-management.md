---
domain: ai-workflows
subdomain: coding-agents
concept: agent-session-management
title: Rethinking Claude Code Best Practices
sources:
  - title: "Rethinking Claude Code Best Practices — Lydia Hallie, Anthropic"
    url: "https://www.youtube.com/watch?v=vlfCjWuv4es"
    author: "AI Engineer"
    date: "2026-11-12"
---

# Rethinking Claude Code Best Practices

Lydia Hallie of Anthropic's Claude Code team argues that as models like Opus 5.5 and Fable 5.2 have improved at long-running tasks, self-checking, and understanding codebases, the way developers should work with them has fundamentally shifted. Earlier in the year, sessions were short, required constant correction, and relied on manual permissioning; today Anthropic runs dozens of concurrent sessions that work for hours and even coordinate other sessions, making developers managers rather than step-by-step approvers.

- As models improve, developers shift from approving every step to managing dozens of long-running, self-checking sessions.
- CLAUDE.md files should now contain only what Claude can't see directly in the code; emphatic instructions like "important" or "never do this" can cause the model to go astray and produce more tool calls and worse results.
- Automatic permissions (default since August) run a classifier that allows safe commands like tests or dependency installs while blocking uncertain ones.
- The "doctor prompt audit" command checks CLAUDE.md and skills to identify what a specific model no longer requires.