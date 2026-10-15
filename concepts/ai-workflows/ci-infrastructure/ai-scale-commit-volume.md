---
domain: ai-workflows
subdomain: ci-infrastructure
concept: ai-scale-commit-volume
title: Rebuilding CI for AI-Scale Commit Volume
sources:
  - title: "Rebuilding CI for AI-Scale Commit Volume — Gautam Korlam, SonarSource"
    url: "https://www.youtube.com/watch?v=7b9tov5Uc5s"
    author: "AI Engineer"
    date: "2026-10-14"
---

# Rebuilding CI for AI-Scale Commit Volume

Gautam Korlam, co-founder and CTO of Gitar (recently acquired by SonarSource), draws on over a decade of build and merge infrastructure work at Uber to argue that AI agents are creating a new class of bottleneck in software production. At Uber, the monorepo already produced "AI agent-scale commit volumes before the agents themselves existed," with thousands of daily changes and builds so long that sequential validation would take up to 20 days, while uncoordinated merges would constantly leave the master branch red. The solution was Summit Queue, a system that tested all possible combinations of incoming commits in parallel, predicted which PRs would break, removed them from the queue for the author to rebase and fix, and only allowed merges when all combinations passed validation.

The core problem Korlam identifies is that CI and code review queues were designed for human speed—people making changes several times an hour—and cannot handle agents that open several PRs a day and all want to commit at once. These centralized queues become bottlenecks that pile up under pressure, and software factory templates plus background agents running various workflows make the slowdown worse because CI and verification remain the overloaded chokepoints.

He points to evidence that this pressure is already material: his own team's commit count has grown almost tenfold in about three years at the same small team size, and industry data from GitHub shows an exponential growth trajectory in PRs needing review, with roughly 25% month-over-month increases. The key technical gap is that changes are not tested against each other, so individually passing PRs can still break the master branch when merged together. Korlam argues the fix requires changes either in the CI system or in code architecture and queues to make them smarter, and notes that regulated industries like banks face this challenge even more acutely as they pursue AI implementation.

- CI and code review queues were designed for human-speed commits and become centralized bottlenecks when AI agents open many PRs per day.
- Uber's Summit Queue tested all combinations of incoming commits in parallel, predicted breakages, and only merged when all combinations passed validation.
- Individually passing PRs can still break the master branch because changes are not tested against each other.
- Commit volume has grown nearly tenfold in three years at the same team size, with GitHub data showing roughly 25% monthly PR growth.
- Solving AI-scale CI requires smarter CI systems or changes to code architecture and queues, and regulated industries face the problem more acutely.