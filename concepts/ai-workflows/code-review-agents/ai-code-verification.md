---
domain: ai-workflows
subdomain: code-review-agents
concept: ai-code-verification
title: Catching Bugs in Agent-Generated Code with AI Code Review
sources:
  - title: "Catch the Bugs Your Code Review Misses - Killian Carlsen-Phelan & Taylor Luttrell-Williams, Sonar"
    url: "https://www.youtube.com/watch?v=wP3P89YB9fA"
    author: "AI Engineer"
    date: "2026-10-29"
---

# Catching Bugs in Agent-Generated Code with AI Code Review

Killian Carlsen-Phelan and Taylor Luttrell-Williams of Sonar (creators of SonarQube) present a workshop on using an AI code-checking agent to catch issues in agent-generated code before merge. They frame the core problem: AI coding agents generate code faster than teams can verify it, creating a review bottleneck where queues grow and merges wait unattended, and increasing incidents as agents scale with the pace of change.

- AI coding agents produce code faster than humans can review, creating a verification bottleneck and growing merge queues.
- Agents lack context on project architecture, team coding standards, and organizational guidelines, leading to more incidents.
- The proposed solution is an AI agent for checking code changes that operates at a high signal-to-noise ratio to minimize false positives and reduce token costs.
- The workshop covers installing the tool as a GitHub app, project-specific configuration for rules and conventions, and CI error diagnostics with automatic fixes applied to pull requests.