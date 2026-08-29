---
domain: engineering-culture
subdomain: internal-ai-tools
concept: in-house-coding-agent
title: Why Ramp built its own in-house coding agent, Inspect
sources:
  - title: "Why Ramp built its own in-house coding agent, Inspect"
    url: "https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect"
    author: "Gergely Orosz"
    date: "2026-08-25"
---

# Why Ramp built its own in-house coding agent, Inspect

Ramp built Inspect, an internal background coding agent, because third-party AI coding harnesses like Claude Code and Cursor fell short of their needs. Local machines limited the number of parallel agent sessions, frontend tooling was inadequate, and the company needed remote development environments. As a result, 75% of merged PRs at Ramp are now authored by Inspect (Orosz, 2026).

- Inspect runs on remote sandboxes with access to the same internal data sources and tools as Ramp engineers, enabling unlimited session concurrency and centralized configuration.
- Inspect verifies its own backend changes by running tests and reviewing telemetry, and visually verifies frontend work via screenshots and live previews—capabilities most third-party harnesses lacked even in late 2025.
- Adoption grew quickly after pivoting from a Chrome extension to a remote development environment based on OpenCode; sessions reached one million by July 2026.
- Ramp uses Inspect for coding, debugging with database queries, Slack-triggered bugfixes, and as a platform for over 200 internal agents like ReviewBuddy and Testo.
- The Inspect team is small (5.5 people) and more than 150 engineers at Ramp have contributed to the project, with over 80% of Inspect itself written using Inspect sessions.