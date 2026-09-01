---
domain: engineering-culture
subdomain: internal-coding-agents
concept: in-house-coding-agent
title: Why Ramp built its own in-house coding agent, Inspect
sources:
  - title: "Why Ramp built its own in-house coding agent, Inspect"
    url: "https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect"
    author: "Gergely Orosz"
    date: "Tue, 25 Aug 2026 15:20:23 GMT"
---

# Why Ramp built its own in-house coding agent, Inspect

Ramp built Inspect, an internal background coding agent, because third-party AI coding harnesses did not meet its needs. According to the article, local machines could only run one or two agent sessions at a time, while Ramp wanted to run many in parallel. The team also needed better frontend tooling and remote development environments to handle growing system complexity.

Inspect runs on remote sandboxes with access to the same internal tools and data that Ramp engineers have. This allows it to verify changes by running tests, checking telemetry, querying feature flags, and visually confirming frontend work with screenshots and live previews. As a result, Inspect authors 75% of merged PRs at Ramp, and about 90% of PRs to the Inspect repo itself.

The tool started as a Chrome extension for designers, then pivoted to a remote development environment with an AI agent on top. It now handles coding, bugfixing in Slack, debugging with access to production data, and serves as a platform for over 200 internal agents, including ReviewBuddy, Oncall Assistant, Testo, and Ramp Research. Inspect's core principle is that agents should have the same context and tools as engineers, which the article identifies as a key difference from third-party harnesses.

- Inspect is Ramp's custom coding agent that runs on remote sandboxes, enabling unlimited session concurrency and centralized configuration.
- It verifies all changes using internal integrations: runs tests, checks telemetry/feature flags for backend, and uses screenshots/live previews for frontend.
- Adoption reached 75% of merged PRs, and the team is small—only 5.5 people core, with 150+ engineers contributing.
- Inspect is used for coding, Slack bugfixing, debugging, building itself, and as a platform for 200+ internal agents.
- The key differentiator is giving agents the same internal context and tools as human engineers, which third-party harnesses lack.