---
domain: ai-workflows
subdomain: coding-agents
concept: software-factory
title: Putting Your Codebase on Autopilot with Agent-Driven Software Factories
sources:
  - title: "How I Put My Codebase on Autopilot"
    url: "https://www.youtube.com/watch?v=lDRjsHjkbjI"
    author: "Kent C. Dodds"
    date: "2026-10-13"
---

# Putting Your Codebase on Autopilot with Agent-Driven Software Factories

Kent C. Dodds describes running a "software factory" where agents autonomously open and complete merge requests, citing 122 PRs issued in 24 hours straight from his software factory, with agents starting and completing valuable work even while he sleeps. He illustrates this with a real example: an agent detected a user experience issue in a table component (a phantom column appearing when the adaptive column is hidden), opened an issue under his account, and another agent fixed it in a merge request — all without his involvement.

The core mechanism is turning agents into "complainers" rather than letting them silently accept workarounds. Agents often say they found an acceptable workaround and ignore problems, but these accumulate into explosive increases in difficulty. His PR release skill instructs agents, after merging and deploying code, to pay attention to their development experience and report minor glitches using a Kodi package, lubricating the mechanisms of the software factory and making agents more efficient at working with code.

He points to Lauren, who produces 2,500 PRs per month, explaining that most of her agents work on polish and code quality — fixing bugs, improving performance, CI, and refactoring — to help the team move faster, while features are added carefully and kept at a high level. Dodds says he remains a "bottleneck" for product decisions and direction, and believes that is how it should be.

To trust autonomous agent decisions, he outlines three requirements: agents must create quality PRs from the start; errors that creep into PRs must be caught before reaching production; and robust defense mechanisms must reduce the radius of damage if something slips into production. He also notes using Devon's cloud agent for a security audit across multiple repositories, and discusses model selection — some subtasks need expensive deep models while routine work can use cheaper ones.

- Agents should be instructed to report problems ("complainers") instead of silently accepting workarounds, since accumulated workarounds cause explosive increases in difficulty.
- Most agent work should target polish and code quality — bug fixes, performance, CI, refactoring — while product decisions remain a human bottleneck.
- Trusting autonomous agents requires three safeguards: quality PRs from the start, catching errors before production, and defense mechanisms to limit damage in production.
- Different subtasks warrant different models: expensive deep models for complex work, cheaper models for routine tasks.