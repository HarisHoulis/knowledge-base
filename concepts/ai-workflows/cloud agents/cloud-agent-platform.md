---
domain: ai-workflows
subdomain: cloud agents
concept: cloud-agent-platform
title: The Agent Behind the Curtain: Building the Oz Cloud Agent Platform
sources:
  - title: "The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp"
    url: "https://www.youtube.com/watch?v=L173Z8DpaJg"
    author: "AI Engineer"
    date: "2026-08-22T17:30:13+00:00"
---

# The Agent Behind the Curtain: Building the Oz Cloud Agent Platform

Safia Abdalla from Warp discusses the rationale and architecture behind Warp's cloud agent platform. The talk emphasizes that good developer tools meet developers where they are and grow with them, adapting to existing workflows and preferences. As AI agentic coding patterns moved from local laptops to the cloud, Warp recognized the need for long-running, infrastructure-adaptive agent workloads, which introduced significant complexity in cloud execution. The core philosophy is that platforms should absorb complexity before it reaches the user, hiding the messy infrastructure stack so developers can focus on meaningful work.

The platform's design models this philosophy through primitives like sandboxes. Initially, Warp provided self-hosted sandboxes for an easy on-ramp, but real teams often manage their own infrastructure and need agents to run on their existing dev boxes. Therefore, the platform supports both managed and self-hosted environments, abstracting away the differences to present a unified experience. This adaptability extends to the harness and other tooling, ensuring the platform aligns with team security, deployment practices, and personal preferences.

- Warp built a cloud agent platform to move AI agents from local laptops to the cloud for long-running and infrastructure-adaptive tasks.
- The central design principle is that platforms should take on complexity before it reaches the user, hiding messy infrastructure concerns.
- Sandboxes are a key primitive, supporting both managed hosting and self-hosted environments to match team workflows.
- Good developer tools meet developers where they are, accommodating their preferences for shell, language, harness, and review processes.