---
domain: ai-workflows
subdomain: agentic-development
concept: ai-assisted-release-cycles
title: How VS Code Went from Monthly to Weekly Releases with AI
sources:
  - title: "How VS Code Went from Monthly to Weekly Releases with AI — Harald Kirschner"
    url: "https://www.youtube.com/watch?v=I2LL_wd89-A"
    author: "AI Engineer"
    date: "2026-10-03"
---

# How VS Code Went from Monthly to Weekly Releases with AI

VS Code moved from a monthly release cycle—maintained since 1.0—to weekly releases, driven by using AI to develop the product itself, not just by shipping agents in the editor. The speaker argues the shift is not about maximizing tokens or using AI daily, but about evolving the entire software delivery system to leverage AI throughout the process (AI Engineer, 2026).

VS Code tracks agent-written code survival rates: the percentage of agent-generated code actually committed. GPT-4.1 started at 55%, and with improved environments and newer models, Cloud Opus 4.6 reached 86%, showing growing developer confidence in AI-generated code. This came with new problems: as one of the largest open-source projects on GitHub, VS Code saw more tickets, including automated low-quality error messages, and more open PRs from both the team and community. Despite expectations of low-quality PRs, accepted community contributions also increased (AI Engineer, 2026).

To go faster, teams prepare agent-ready codebases with lightweight agents.md files that give agents a map of the codebase and serve as living documents that evolve as agents make mistakes. Existing developer experience investments help because quality documentation and onboarding are read by agents. Skills also matter: VS Code encoded accessibility best practices into a tool everyone can use, so checks are automated rather than depending on one person for feedback (AI Engineer, 2026).

- VS Code shifted from monthly to weekly releases after over 10 years of monthly cadence since 1.0.
- Agent code survival rose from 55% with GPT-4.1 to 86% with Cloud Opus 4.6, reflecting increased trust in AI-generated code.
- AI increased ticket and PR volume, including low-quality automated reports, but accepted community PRs also increased.
- Success requires evolving the delivery system, not just generating more code: agent-ready codebases, agents.md maps, skills, and existing docs/onboarding.