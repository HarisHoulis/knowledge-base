---
domain: ai-workflows
subdomain: coding-agents
concept: agent-generated-unit-tests
title: 225,000 Lines of Tests, Written and Merged by Agents at Duolingo
sources:
  - title: "225,000 Lines of Tests, Written and Merged by Agents - Kush Agrawal, Duolingo"
    url: "https://www.youtube.com/watch?v=D_4Rn6uLdQM"
    author: "AI Engineer"
    date: "2026-11-11"
---

# 225,000 Lines of Tests, Written and Merged by Agents at Duolingo

Kush Agrawal, a lead engineer on Duolingo's platform team, describes how Duolingo used AI agents to write and merge over 200,000 lines of unit tests in its iOS codebase. Duolingo ships weekly, runs 600+ concurrent A/B tests, and its iOS repo grew from ~200,000 lines in 2019 to nearly 2 million, with contributors rising past 250 people—many of them backend engineers, Android engineers, managers, and designers enabled by tools like Cursor and Claude Code. As agents and humans write code faster, the bottleneck shifts from writing code to verifying it, making unit tests the key safeguard and feedback loop for agent-generated changes.

Starting in March with only 11% overall unit test coverage (repositories 11%, ViewModels 9%, data sources 5%, ~9% across the MVVM layers), the team focused on the MVVM portion of the codebase since it is easiest to test while legacy code is migrated. After eight months, coverage rose from 11% to 24%, repositories from 11 to 72, ViewModels from 9 to 58, data sources from 5 to 41, and MVVM share from 9% to 59%.

The system follows a simple cycle—identify files needing tests, write tests with an agent, check quality and pass CI, get engineer review and merge, then feed learnings into the next batch—implemented in production as multiple Temporal workflows coordinated through shared state in S3. Temporal provides reliable, resumable execution for agent sessions lasting seconds to hours, plus schedules, composite workflows for parallelism, retries, timeouts, and idempotence to avoid duplicate work per file. Claude Code acts as the coding agent, GitHub handles actions and PRs, and Datadog monitors pipeline health. The rollout was divided into phases, beginning with a local inspection to assess viability, then a planned workflow for writing tests against existing code, followed by the PR lifecycle.

- Duolingo agents wrote and merged 225,000+ lines of iOS unit tests, raising coverage from 11% to 24% in eight months.
- With AI-assisted coding, verification—not writing code—becomes the bottleneck, so unit tests serve as safeguards and living documentation for agent changes.
- The pipeline is orchestrated with Temporal workflows sharing state via S3, using Claude Code as the agent, GitHub for PRs, and Datadog for monitoring.
- Temporal's retries, timeouts, schedules, and idempotence make long-running agent sessions reliable and prevent duplicate work per file.
- The team scoped work to the MVVM layers (easiest to test) while legacy code is migrated, and iterated on engineer review feedback to improve each batch.