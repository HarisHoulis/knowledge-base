---
domain: ai-workflows
subdomain: coding-agent-harness
concept: maintainability-sensors
title: Maintainability sensors for coding agents
sources:
  - title: "Maintainability sensors for coding agents"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html"
    author: "Martin Fowler"
---

# Maintainability sensors for coding agents

The article introduces the concept of harness engineering for coding agent users, as articulated by Birgitta Böckeler, which involves building a system of guides and sensors. These components work together to increase the probability of good agent outputs and enable self-correction before problems reach human eyes. According to Fowler, this approach expands the coding agent harness to proactively manage code quality. The current installment focuses on using sensors to keep a codebase maintainable, specifically through static analysis and basic code linting. This represents a foundational layer of automated checks that provide continuous feedback to both the agent and the human developer.

- Coding agent harnesses combine guides and sensors to improve output quality.
- Sensors enable self-correction by catching issues before human review.
- Static analysis and code linting are early examples of maintainability sensors.
- Maintainability sensors help preserve codebase health when using AI-driven development tools.