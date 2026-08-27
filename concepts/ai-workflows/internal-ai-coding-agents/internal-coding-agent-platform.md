---
domain: ai-workflows
subdomain: internal-ai-coding-agents
concept: internal-coding-agent-platform
title: Why Ramp built its own in-house coding agent, Inspect
sources:
  - title: "Why Ramp built its own in-house coding agent, Inspect"
    url: "https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect"
    author: "Gergely Orosz"
    date: "2026-08-25"
---

# Why Ramp built its own in-house coding agent, Inspect

Ramp built its own internal AI coding agent, Inspect, after finding third-party harnesses insufficient for its needs. The company wanted to run many agents in parallel, which local machines could not support, and needed better frontend tooling for designers as well as remote development environments. Inspect runs on remote sandboxes with access to most internal data sources and verifies all backend and frontend changes, a capability most third-party tools lacked at the time (Orosz, 2026).

Inspect started as a Chrome extension for designers to make small UI tweaks, but pivoted to a remote development environment with a coding agent on top, using the open-source OpenCode harness. This shift drove rapid adoption: by May 2026, 75% of merged PRs at Ramp were authored by Inspect, and over 150 engineers have contributed to its codebase. Inspect is also used for debugging, Slack-triggered bug fixes, and as a platform for more than 200 internal agents like ReviewBuddy and Ramp Research. Its core principle is giving agents the same context and tools as software engineers, with sandboxes spinning up in under five seconds (Orosz, 2026).

- Ramp built Inspect because third-party harnesses limited parallel agent sessions on local machines, lacked frontend tooling, and didn't provide remote dev environments.
- Inspect uses remote sandboxes with internal integrations, enabling it to verify backend changes via tests, telemetry, and feature flags, plus frontend changes with screenshots and live previews.
- Adoption grew quickly: 60% of PRs authored by Inspect two months after v2 launch, reaching 75% by May 2026.
- Inspect functions as a platform, with 200+ internal agents built on top, including ReviewBuddy, Oncall Assistant, Testo, and Ramp Research.
- The design principle is to give agents the same context and tools as software engineers, which is a key differentiator from third-party AI harnesses.