---
domain: ai-workflows
subdomain: cloud agent infrastructure
concept: cloud-agent-platform
title: The Agent Behind the Curtain: Building the Oz Cloud Agent Platform
sources:
  - title: "The Agent Behind the Curtain: Building the Oz Cloud Agent Platform"
    url: "https://www.youtube.com/watch?v=L173Z8DpaJg"
    author: "AI Engineer"
    date: "2026-08-22T17:30:13+00:00"
---

# The Agent Behind the Curtain: Building the Oz Cloud Agent Platform

Safia Abdalla presents the design philosophy behind Warp's Oz Cloud Agent Platform, emphasizing that great developer tools meet users where they are and adapt to their workflows. She draws on her 8 years of experience building developer tooling, from Jupyter Notebook to Microsoft APIs, to argue that platforms should absorb complexity before it reaches the user, allowing developers to focus on meaningful work.

The talk traces the evolution from local AI coding tools to cloud-based agents, highlighting the need for isolated sandboxes where agents can execute long-running tasks. Initially, Warp provided self-hosted sandboxes as an easy on-ramp, but they soon realized that serious teams managing their own infrastructure require the ability to run agent workloads on infrastructure they bring. This led to supporting both managed hosting and self-hosted sandboxes, hiding the underlying complexity while accommodating diverse security and deployment practices.

The presentation positions the cloud agent platform as a natural progression of developer tooling, where the terminal's familiar environment is extended with AI capabilities and scalable cloud execution, all while preserving user preference and workflow adaptability.

- Effective dev tools meet users in their existing workflows and grow with them, adapting to preferences like shell, language, and review process.
- Cloud agents require isolated sandboxes to run work, moving beyond local CPU constraints.
- A platform should support both managed and self-hosted sandboxes to serve teams with diverse infrastructure requirements.
- Platforms should take on complexity before it reaches the user, shielding them from infrastructure concerns.