---
domain: engineering-culture
subdomain: internal-ai-tools
concept: in-house-coding-agent
title: Why Ramp Built Its Own In-House Coding Agent, Inspect
sources:
  - title: "Why Ramp built its own in-house coding agent, Inspect"
    url: "https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect"
    author: "Gergely Orosz"
    date: "2026-08-25"
---

# Why Ramp Built Its Own In-House Coding Agent, Inspect

Ramp built its own internal AI coding agent, Inspect, after finding third-party harnesses like Claude Code and Cursor insufficient. Local machines could only run one or two agent sessions at a time, frontend tooling was lacking, and Ramp needed remote development environments to handle growing system complexity. Inspect runs agents in remote sandboxes with access to the same tools and data as Ramp engineers, and it verifies changes by running backend tests, checking telemetry, and providing live frontend previews. As a result, 75% of merged PRs at Ramp are now raised by Inspect, with over one million sessions by July 2026 [source](https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect).

- Inspect was built because local machines limited parallel agent sessions and third-party tools lacked internal integrations for verification.
- It runs in remote sandboxes with access to Ramp's internal data, enabling backend test runs and visual frontend verification.
- 75% of merged PRs at Ramp are authored by Inspect, up from 60% in January 2026.
- Inspect is also a platform for 200+ internal agents, including ReviewBuddy, Oncall Assistant, and Testo.
- A small team of 5.5 people maintains Inspect, with 150+ engineers contributing; 80% of Inspect is written via Inspect sessions.