---
domain: ai-workflows
subdomain: agent-architecture
concept: agents-over-frameworks
title: Agent Frameworks Considered Harmful
sources:
  - title: "Agent Frameworks Considered Harmful — Rémi Louf, .txt"
    url: "https://www.youtube.com/watch?v=KHudyx5wW3U"
    author: "AI Engineer"
    date: "2026-08-22T16:30:39+00:00"
---

# Agent Frameworks Considered Harmful

Rémi Louf, CEO of a 15-person AI company, took two weeks to explore the sudden leap in agent capabilities (around Opus 4.6) and automate his morning routine: browsing market news, checking Linear/Jira and CRM, and processing voice notes from walks into a 'morning briefing with coffee.' He found that current agent interfaces still require constant human attention, comparing them to a riding mower that still needs someone to stay on it, or later 'SSH with vibes' on a phone. He started building a simple system himself and discovered that agent frameworks made him spend all his time editing prompts inside code. He switched to declarative YAML configuration, which is easier to version, diff, and review in PRs, and can be dropped into a folder to magically work.

- Agent frameworks often lead to prompt editing inside code; declaring agents in YAML is simpler and more maintainable.
- Current agent UX is like needing to stay on a tractor or remote-control it; we need unattended, autonomous agents.
- Combine declarative agent definitions with cron jobs for scheduled, autonomous morning briefings.
- Build the dumbest thing that could possibly work rather than adopting a framework from the start.
- The talk critiques over-engineering in agent frameworks in favor of simple, composable primitives.