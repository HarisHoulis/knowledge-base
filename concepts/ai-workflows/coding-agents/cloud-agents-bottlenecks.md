---
domain: ai-workflows
subdomain: coding-agents
concept: cloud-agents-bottlenecks
title: Merge Is the Bottleneck: Cloud Agents and the Shift Beyond the IDE
sources:
  - title: "Merge Is the Bottleneck - Prasanna Sankar, Vorflux"
    url: "https://www.youtube.com/watch?v=TlOAhw9t5DA"
    author: "AI Engineer"
    date: "2026-11-10"
---

# Merge Is the Bottleneck: Cloud Agents and the Shift Beyond the IDE

Prasanna Sankar, a three-time YC founder (including Rippling) and founder of Vorflux, describes how the release of Opus 4.5 marked a shift from IDE auto-completion to agents that run autonomously for minutes at a time, making it feasible to skip the IDE and work from the terminal. He argues these runtimes will only grow longer, and that models now outperform even elite human competitive programmers at pure logical thinking—partly because winning setups spend far more compute on inference to access higher-level intelligence.

- Agents moved from IDE auto-completion to autonomous multi-minute runs, enabling terminal-first workflows
- Long-running agents belong in the cloud, not on the developer's machine
- The main barrier to cloud agents is replicating the full localhost environment—dependencies, ports, secrets, auth, and seeding
- Vorflux spends tokens at launch running subagents to provision a clean EC2 instance mirroring the user's environment
- Planning phases consume human time without consuming many agent tokens, making them a key target for improvement