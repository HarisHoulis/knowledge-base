---
domain: ai-workflows
subdomain: feature-flag-cleanup
concept: multi-agent-feature-flag-cleanup
title: DoorDash Uses Multi-Agent LLMs to Clean Up 60,000 Feature Flags
sources:
  - title: "DoorDash Uses Multi Agent LLMs to Clean up 60,000 Feature Flags"
    url: "https://www.infoq.com/news/2026/09/doordash-feature-flag-cleanup/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Leela Kumili"
    date: "Fri, 18 Sep 2026 13:50:00 GMT"
---

# DoorDash Uses Multi-Agent LLMs to Clean Up 60,000 Feature Flags

DoorDash built a multi-agent LLM system to automate stale feature flag cleanup across more than 60,000 flags and 623 repositories (InfoQ). The workflow combines live experimentation data through MCP, engineer approval, isolated Git worktrees, parallel agents, and automated validation (InfoQ).

In an evaluation of 50 flags, the system produced 45 usable pull requests, averaging 13.8 minutes and $4.79 per cleanup (InfoQ).

- DoorDash targeted stale feature flag cleanup across 60,000+ flags and 623 repositories.
- The multi-agent LLM workflow uses MCP for live experimentation data, engineer approval, isolated Git worktrees, parallel agents, and automated validation.
- A 50-flag evaluation yielded 45 usable pull requests.
- Average cleanup time was 13.8 minutes at $4.79 per cleanup.