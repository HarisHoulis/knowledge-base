---
domain: ai-workflows
subdomain: coding-agents
concept: software-factory
title: 40x More Merged PRs With 2.7x the Engineers: Cognition's Software Factory
sources:
  - title: "40x More Merged PRs With 2.7x the Engineers — Walden Yan, CPO, Cognition"
    url: "https://www.youtube.com/watch?v=U92J5mCDLMc"
    author: "AI Engineer"
    date: "2026-11-18"
---

# 40x More Merged PRs With 2.7x the Engineers: Cognition's Software Factory

Walden Yan, co-founder and CPO of Cognition, describes how his engineering team achieved a 40x increase in combined PRs over roughly a year while only growing the engineering headcount 2.7x, implying each engineer became more than 10x more productive, with PR quality claimed to be equal or better than a year prior. The core mechanism is a "software factory" in which everything is automated by default: PRs flow from initial bug report through merge, monitoring, and support without human intervention, with an escalation system reserved for cases that genuinely require human judgment.

This shift required redefining the engineer's role. Yan told the team that simply pulling tickets off the Linear board and handing them to an agent would not succeed in the AI era, since anything describable and implementable can be sent to Devin. Instead, large teams were split into small groups of two or three engineers who own greater vertical responsibility—reviewing user bug reports, running QA, product management and governance—each managing their own Linear task board and dispatching work to agents.

Workflows are centered on Slack: a user bug report (often a video) is forwarded to an internal channel, Devin is tagged, and it creates a PR and replies with a video demonstrating the fix. This makes development evidence-based and video-driven, letting the team avoid opening an IDE or GitHub in most cases. Yan stresses that buying a coding agent is not enough—the underlying infrastructure must change. Cognition migrated from cloud-based testing environments to per-service local runs via Docker Compose, with mocked third-party services, all on a single VM accessible to every developer, rebuilt from scratch hourly so no coding agent needs access to live services to test changes.

- Cognition reports 40x more combined PRs with only 2.7x more engineers over about a year, implying >10x per-engineer productivity with equal or better quality.
- The "software factory" model automates the full lifecycle from bug report to merge, monitoring, and support by default, with human escalation only when judgment is needed.
- Engineers are organized into small 2-3 person groups with vertical ownership spanning bug triage, QA, product management, and agent dispatch via their own Linear boards.
- Slack-centric, video-driven workflows let Devin create PRs and post proof-of-fix videos, so engineers rarely open an IDE or GitHub.
- Infrastructure must change: services run locally via Docker Compose with mocked third-party dependencies on a shared hourly-rebuilt VM, so agents never need live services to test.