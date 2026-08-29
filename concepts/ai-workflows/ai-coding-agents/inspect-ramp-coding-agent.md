---
domain: ai-workflows
subdomain: ai-coding-agents
concept: inspect-ramp-coding-agent
title: Why Ramp Built Its Own In-House Coding Agent, Inspect
sources:
  - title: "Why Ramp built its own in-house coding agent, Inspect"
    url: "https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect"
    author: "Gergely Orosz"
    date: "Tue, 25 Aug 2026 15:20:23 GMT"
---

# Why Ramp Built Its Own In-House Coding Agent, Inspect

Ramp built Inspect, an internal AI coding agent, because third-party harnesses like Claude Code and Cursor were limited by local machine constraints and lacked deep internal integrations. Inspect runs on remote sandboxes, allowing unlimited parallel sessions and centralized configuration. It integrates with Ramp's internal tools and data sources, giving agents the same context and access as human engineers. The agent also verifies its own work: running tests, checking telemetry, querying feature flags, and visually confirming frontend changes via screenshots and live previews [Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect).

Inspect began as a Chrome extension for designers to make small UI tweaks, but pivoted to a remote development environment with an AI agent on top, using OpenCode as its harness. This pivot drove adoption: 75% of merged PRs at Ramp are now authored by Inspect, and the platform has hosted over one million sessions. The Inspect team is small (5.5 people), yet more than 150 engineers at Ramp have contributed to the codebase. Inspect is used for coding, bugfixing via Slack, debugging with access to production replicas, and as a platform for building more than 200 internal agents such as ReviewBuddy, Oncall Assistant, Testo, and Ramp Research [Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect).

The decision to build rather than buy was driven by three needs: running more agents in parallel than local machines allow, better frontend tooling so designers could make UI changes, and the need for remote development environments as Ramp's systems grew more complex. Inspect's architecture uses React/Vite, Cloudflare Durable Objects, SQLite, the Cloudflare Agents SDK, and Modal sandboxes. Sandboxes spin up in under five seconds, and all Inspect sessions are public and collaborative by default [Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect).

- Inspect is Ramp's internal coding agent that runs on remote sandboxes, enabling high concurrency and deep internal integrations.
- 75% of merged PRs at Ramp are authored by Inspect, and it has surpassed one million total sessions.
- Key differentiators: remote sandboxes, internal integrations, and automatic verification of backend and frontend changes.
- Inspect evolved from a Chrome extension for designers to a platform supporting 200+ internal agents, including code review, oncall, and data analysis tools.
- The project is run by a small team of 5.5 people, with contributions from 150+ engineers at Ramp.