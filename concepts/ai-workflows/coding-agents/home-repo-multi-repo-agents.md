---
domain: ai-workflows
subdomain: coding-agents
concept: home-repo-multi-repo-agents
title: The Home Repo: The Effortless Multi-Repo Agent Setup
sources:
  - title: "The Home Repo: The effortless multi-repo agent setup"
    url: "https://www.youtube.com/watch?v=hWe-j78vNpc"
    author: "Matt Pocock"
    date: "2026-11-12"
---

# The Home Repo: The Effortless Multi-Repo Agent Setup

Matt Pocock describes a "home repository" pattern for running coding agents across many repositories. Instead of duplicating skills, tools, and agents.md files across dozens of repos (or hiding them in user directories where they go stale), you keep a single home repo containing all shared agent configuration and run every agent session from inside it. The agent then reaches out to the storefront, payments API, and other repos from that one session, producing pull requests in each.

- Run agent sessions from one home repo holding shared skills, settings, and agents.md instead of duplicating config across many repos.
- agents.md links to other repositories by path; the agent clones missing repos and uses worktrees for concurrent sessions.
- Avoids user-directory config, which is invisible, falls behind, and should be reserved for personal preferences.
- Scales to roughly 20-40 repositories; beyond that, add progressive disclosure.