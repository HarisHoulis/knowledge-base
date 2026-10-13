---
domain: ai-workflows
subdomain: coding-agents
concept: agent-check-hooks
title: Stop Running Your Checks in Hooks for AI Coding Agents
sources:
  - title: "STOP running your checks in hooks"
    url: "https://www.youtube.com/shorts/zgy8_ApYNDk"
    author: "Matt Pocock"
    date: "2026-10-13"
---

# Stop Running Your Checks in Hooks for AI Coding Agents

Matt Pocock argues that running automated checks on every file edit is the wrong approach for AI coding agent workflows. Instead, checks should be moved to pre-commit hooks, which provide a more appropriate checkpoint for validating agent-generated changes [Source: https://www.youtube.com/shorts/zgy8_ApYNDk].

The video distinguishes between per-edit checks and pre-commit hooks, positioning the latter as the right place to enforce quality gates when agents are producing code. This also has implications for optimizing the CI/CD pipeline to fit agent-driven development [Source: https://www.youtube.com/shorts/zgy8_ApYNDk].

The practical takeaway is to restructure automated checks so they run at commit time rather than on every edit, reducing overhead while still catching issues before code enters the pipeline [Source: https://www.youtube.com/shorts/zgy8_ApYNDk].

- Running checks on every file edit is the wrong setup for AI coding agents
- Pre-commit hooks are the recommended place to run automated checks
- CI/CD pipelines should be optimized for agent workflows