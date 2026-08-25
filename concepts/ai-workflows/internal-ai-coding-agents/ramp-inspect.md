---
domain: ai-workflows
subdomain: internal-ai-coding-agents
concept: ramp-inspect
title: Why Ramp built its own in-house coding agent, Inspect
sources:
  - title: "Why Ramp built its own in-house coding agent, Inspect"
    url: "https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect"
    author: "Gergely Orosz"
    date: "2026-08-25"
---

# Why Ramp built its own in-house coding agent, Inspect

Ramp developed Inspect, an internal background AI coding agent, after finding third-party harnesses like Claude Code and Cursor inadequate. Key limitations included local-machine concurrency (only one or two sessions), insufficient frontend tooling for designers, and the need for remote development environments. Inspect evolved from a v1 Chrome extension for UI edits into v2, a remote development environment with a coding agent built on OpenCode, which provides an HTTP API and model agnosticism (source: https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect).

Inspect runs on remote sandboxes with access to internal tools and data, allowing it to verify changes: backend verification via tests, telemetry, and feature flags; frontend verification via screenshots and live previews. This closed-loop verification is a differentiator compared to most third-party harnesses. The cloud-based machine enables unlimited parallel sessions, centralized configuration, and collaboration. Adoption grew rapidly: by May 2026, 75% of merged PRs at Ramp were authored by Inspect, with sandboxes spinning up in under 5 seconds.

Ramp uses Inspect for coding, Slack-triggered bugfixing, debugging (including database queries), and as a platform for 200+ internal agents like ReviewBuddy, Oncall Assistant, Testo, and Ramp Research. Inspect is also used to build itself—over 80% of its codebase is written via Inspect sessions. The team is small (5.5 people) and more than 150 engineers have contributed to the project, illustrating a successful buy-vs-build outcome for internal AI tooling.

- Inspect is Ramp's custom background coding agent running on remote sandboxes with internal integrations, distinguishing it from third-party harnesses.
- Ramp built Inspect because local machines limited concurrent agent sessions, frontend tooling was lacking, and remote dev environments were needed.
- Inspect verifies its own work through backend tests/telemetry and frontend screenshots, closing the feedback loop better than external tools.
- Adoption reached 75% of merged PRs at Ramp, with under 5-second sandbox spin-up.
- Inspect serves as a platform for 200+ internal agents (e.g., ReviewBuddy, Oncall Assistant, Ramp Research) and is used to build itself.