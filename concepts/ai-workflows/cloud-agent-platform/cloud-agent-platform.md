---
domain: ai-workflows
subdomain: cloud-agent-platform
concept: cloud-agent-platform
title: The Agent Behind the Curtain: Building the Oz Cloud Agent Platform
sources:
  - title: "The Agent Behind the Curtain: Building the Oz Cloud Agent Platform"
    url: "https://www.youtube.com/watch?v=L173Z8DpaJg"
    author: "Safia Abdalla"
    date: "2026-08-22T17:30:13+00:00"
---

# The Agent Behind the Curtain: Building the Oz Cloud Agent Platform

In this talk, Safia Abdalla from Warp discusses the design philosophy behind building the Oz Cloud Agent Platform, a system that brings AI agents to the cloud. She emphasizes that great developer tools meet developers where they are and grow with them, adapting to individual workflows and preferences. The platform's core principle is to absorb complexity before it reaches the user, ensuring a seamless experience by hiding the messy infrastructure concerns that arise when moving agent workloads to the cloud (Abdalla, 2026).

Abdalla explains how this philosophy translates into concrete architectural decisions. The first major component is the sandbox—an isolated environment where agents execute tasks. Initially, Warp provided self-hosted (managed) sandboxes for easy onboarding, but they soon realized that serious teams often need to run agents on their own infrastructure, such as dev boxes, to meet security and deployment requirements. As a result, the platform supports both managed and bring-your-own infrastructure, abstracting away the complexity of where compute lives (Abdalla, 2026).

Another critical aspect is accommodating user preferences for the harness—the tooling that shapes how agents interact with code. By acknowledging that people are passionate about their tools, the platform is designed to be flexible, allowing teams to integrate their existing workflows rather than forcing them into a rigid model. This adaptability is key to making the platform enjoyable and effective for real-world development (Abdalla, 2026).

- Good developer tools meet developers where they are and grow with them, adapting to their workflows and preferences.
- Platforms should absorb complexity before it reaches the user, hiding leaky infrastructure concerns.
- Cloud agent platforms need to support both managed and self-hosted sandboxes to accommodate teams with existing infrastructure.
- User choice of harness is important; the platform should adapt to existing tools and workflows rather than impose a fixed model.