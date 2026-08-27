---
domain: ai-workflows
subdomain: cloud-agent-platform
concept: cloud-agent-complexity-hiding
title: The Agent Behind the Curtain: Building the Oz Cloud Agent Platform
sources:
  - title: "The Agent Behind the Curtain: Building the Oz Cloud Agent Platform"
    url: "https://www.youtube.com/watch?v=L173Z8DpaJg"
    author: "Safia Abdalla"
    date: "2026-08-22"
---

# The Agent Behind the Curtain: Building the Oz Cloud Agent Platform

Safia Abdalla, an engineer at Warp, discusses the design philosophy behind building a cloud agent platform. She emphasizes that good developer tools meet developers where they are and grow with them, adapting to workflows and preferences. In the context of AI agents, this means supporting a progression from local terminal tools to cloud-based agents that can handle long-running, infrastructure-aware tasks. A core principle is that platforms should absorb complexity before it reaches the user, so the experience remains focused on the work at hand (Abdalla, 2026).

The talk details key components of the cloud agent platform, starting with the sandbox environment where agents execute tasks. While the initial intuition was to provide fully managed sandboxes for easy onboarding, real teams often need to integrate with their own infrastructure, security policies, and deployment practices. Therefore, the platform supports both managed hosting and self-hosted sandboxes, abstracting that choice from the user while still accommodating enterprise needs. This reflects the broader theme of hiding complexity while remaining flexible to varying constraints (Abdalla, 2026).

- Developer tools should meet users in their existing workflows and evolve with them.
- Platforms should hide infrastructure complexity from users to let them focus on high-value work.
- Cloud agents require sandboxed execution environments; managed sandboxes are easy to start with but self-hosted options are necessary for teams with existing infrastructure.
- Supporting both managed and self-hosted sandboxes allows the platform to adapt to diverse security and deployment requirements.