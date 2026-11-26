---
domain: engineering-culture
subdomain: agentic-software-engineering
concept: ai-native-engineering-practices
title: How Anthropic Builds Software in 2026 with Katelyn Lesse
sources:
  - title: "How Anthropic builds software in 2026 with Katelyn Lesse"
    url: "https://newsletter.pragmaticengineer.com/p/how-anthropic-builds-software-in"
    author: "Gergely Orosz"
    date: "2026-11-25"
---

# How Anthropic Builds Software in 2026 with Katelyn Lesse

Katelyn Lesse, who leads platform engineering at Anthropic, describes how the company rewrote its Messages API — the service handling authentication, tokenization, billing, and safety checks for all Claude tokens — from a Python monolith to Rust in roughly five months. Python was chosen in 2023 because researchers worked in Python and the API team overlapped heavily with Research, but CPU overhead became a growing problem amid a global CPU shortage. The rewrite was done without Rust experts: Claude helped engineers learn the language, and the existing Python API served as a perfect test harness via shadow traffic until responses were identical. Engineers closely reviewed only about 20% of the generated code, on the principle that verifiable outcomes reduce the need for line-by-line review [source].

Agentic workflows now permeate the engineering process. A Claude code review classifier runs on all pull requests, deciding whether human review is needed, how many reviewers, and which team should review; mechanical changes like SDK bumps or flaky-test fixes can be reviewed by another Claude and merged automatically. A Claude agent shadows the API oncall rotation and now categorizes alerts before a human is paged, with the long-term goal of handling incidents without waking anyone. New hires onboard by asking Claude, which is connected to the codebase and internal systems and can generate interactive tutorials [source].

Some things have not changed: planning and alignment across Inference, Research, Safety, and App teams still consume significant time, and teams remain two-pizza sized (5-8 people) because that size suits understanding complex systems and staffing oncall. Engineers increasingly build tooling to accelerate their own work, and deep language knowledge matters less. The team phased out its traditional coding interview after strong candidates failed it, and is experimenting with interviews conducted alongside coding agents, while design and project deepdive interviews remain. For promotions, time-to-completion is now meaningless, so impact metrics like CPU savings, latency reduction, and incidents avoided are used instead [source].

- Anthropic rewrote its Python Messages API in Rust in ~5 months without Rust experts, using Claude for learning and shadow traffic against the existing API as a test harness, with close review of only ~20% of generated code.
- A Claude code review classifier triages all PRs — deciding if human review is needed, how many reviewers, and which team — and a Claude agent categorizes oncall alerts before humans are paged.
- Onboarding is 'talk to Claude': new engineers query a Claude connected to the codebase and internal systems instead of relying on onboarding buddies.
- Planning, alignment, and two-pizza team ownership persist; engineers spend more time on tooling, and promotions are judged by impact (CPU, latency, incidents) rather than time-to-completion.
- Traditional coding interviews were phased out after strong candidates failed them; the team is experimenting with agent-assisted interviews while keeping design and deepdive interviews.