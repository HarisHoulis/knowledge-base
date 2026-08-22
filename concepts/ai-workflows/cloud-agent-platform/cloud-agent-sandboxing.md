---
domain: ai-workflows
subdomain: cloud-agent-platform
concept: cloud-agent-sandboxing
title: The Agent Behind the Curtain: Building the Oz Cloud Agent Platform
sources:
  - title: "The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp"
    url: "https://www.youtube.com/watch?v=L173Z8DpaJg"
    author: "AI Engineer"
    date: "2026-08-22T17:30:13+00:00"
---

# The Agent Behind the Curtain: Building the Oz Cloud Agent Platform

In this talk, Safia Abdalla from Warp discusses the design principles and infrastructure behind Warp's cloud agent platform. She emphasizes that good developer tools meet developers where they are and grow with them, accommodating personal workflows and preferences. The progression from a terminal, to local AI coding tools, to cloud-based agents is framed as a natural evolution for handling long-running and more complex tasks. A core philosophy is that platforms should take on complexity before it reaches the user, so that the underlying infrastructure messiness is hidden from developers. For the cloud agent platform, this means providing sandboxes where agents execute tasks. Initially, Warp offered self-hosted sandboxes for an easy on-ramp, but serious teams often manage their own infrastructure and need to run agent workloads on infrastructure they bring. Therefore, the platform supports both managed hosting and self-hosting, abstracting away the complexity of infrastructure concerns while adapting to team security and deployment practices.

- Good dev tools meet users where they are and grow with them, adapting to workflows and preferences.
- Cloud agents require sandboxes—isolated environments—to do their work, introducing significant infrastructure complexity.
- A platform should take on complexity before it reaches the user, hiding leaky abstractions.
- Supporting both managed and self-hosted sandboxes is necessary for teams with existing infrastructure needs.