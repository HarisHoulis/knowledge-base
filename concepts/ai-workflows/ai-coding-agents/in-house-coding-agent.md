---
domain: ai-workflows
subdomain: ai-coding-agents
concept: in-house-coding-agent
title: Why Ramp built its own in-house coding agent, Inspect
sources:
  - title: "Why Ramp built its own in-house coding agent, Inspect"
    url: "https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect"
    author: "Gergely Orosz"
    date: "Tue, 25 Aug 2026"
---

# Why Ramp built its own in-house coding agent, Inspect

Ramp built Inspect, an internal AI coding agent that runs on remote sandboxes with access to most internal data sources and full verification capabilities. The primary motivation was dissatisfaction with third-party harnesses: local machines limited concurrent agents, frontend tooling was lacking, and remote development environments were needed as Ramp scaled. Inspect was initially a Chrome extension for designers, but pivoted to a background agent on remote dev environments, leading to 75% of merged PRs now authored by Inspect and over one million total sessions by July 2026 (Sengottuvelu, Dadkhah, and Bruggeman via Orosz, 2026).

Inspect differentiates itself through remote sandboxes that allow unlimited concurrency, deep internal integrations with Ramp's tools and data, and a 'close the loop' verification approach: backend changes are verified with tests, telemetry, and feature flags, while frontend changes are visually confirmed with screenshots and live previews. The architecture uses React/Vite, Cloudflare Durable Objects, SQLite, the Cloudflare Agents SDK, and Modal sandboxes, with OpenCode as the harness. Sandboxes spin up in under five seconds due to smart tricks (Orosz, 2026).

Beyond coding, Inspect is used for Slack-triggered bugfixing, debugging with access to sanitized production databases, and as a platform for over 200 internal agents like ReviewBuddy (code review), Oncall Assistant, Testo (QA), Ramp Research (data analyst), and Voice of the Customer. The founding team emphasized that giving agents the same context and tools as engineers is the key principle, and this internal integration gives Ramp an edge over third-party tools (Orosz, 2026).

- Ramp built Inspect because third-party AI harnesses couldn't support running many agents in parallel, lacked frontend tooling, and didn't offer remote dev environments.
- Inspect uses remote sandboxes with full internal data access, enabling unlimited concurrency, centralized configuration, and verification of backend and frontend changes.
- Adoption is high: 75% of merged PRs at Ramp are raised by Inspect, and over 150 engineers have contributed to its codebase.
- Inspect has become an agent platform with 200+ internal agents built on top, including code review (ReviewBuddy), oncall assistance, and data analysis (Ramp Research).
- Under 5 seconds to spin up a fully provisioned remote dev environment is achieved through technical optimizations in the stack, which includes Cloudflare Durable Objects and Modal sandboxes.