---
domain: engineering-culture
subdomain: internal-ai-tooling
concept: in-house-coding-agent
title: Why Ramp built its own in-house coding agent, Inspect
sources:
  - title: "Why Ramp built its own in-house coding agent, Inspect"
    url: "https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect"
    author: "Gergely Orosz"
    date: "2026-08-25"
---

# Why Ramp built its own in-house coding agent, Inspect

Ramp built Inspect, an internal AI coding agent, because third-party harnesses like Claude Code and Cursor had limitations: they constrained how many agents could run locally, lacked advanced frontend tooling, and did not integrate deeply with internal systems. Inspect runs on remote sandboxes, giving developers unlimited session concurrency, centralized setup, and access to the same tools and context as Ramp engineers. Its agents can verify changes by running tests, querying telemetry, checking feature flags, and visually confirming frontend work via screenshots and live previews—capabilities most third-party tools lacked at the time (Pragmatic Engineer, 2026).

- Inspect is Ramp's internal coding agent running on remote sandboxes, enabling unlimited parallel sessions and centralized setup.
- It integrates with Ramp's internal data sources and verifies its own changes, both backend (tests, telemetry, feature flags) and frontend (screenshots, live previews).
- Adoption grew quickly: 75% of merged PRs at Ramp are now from Inspect, and 80% of Inspect is built using Inspect.
- Ramp built it because local machines limited agent concurrency, third-party harnesses lacked frontend tooling, and remote dev environments were needed.
- Inspect is used as a platform for 200+ internal agents, including code review, oncall assistance, QA testing, and data analysis.