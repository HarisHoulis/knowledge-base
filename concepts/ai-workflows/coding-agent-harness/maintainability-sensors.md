---
domain: ai-workflows
subdomain: coding-agent-harness
concept: maintainability-sensors
title: Maintainability sensors for coding agents
sources:
  - title: "Maintainability sensors for coding agents"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html"
    author: "Martin Fowler"
    date: "n.d."
---

# Maintainability sensors for coding agents

Birgitta Böckeler introduces a mental model for coding agent harnesses, distinguishing between guides and sensors. Guides are proactive instructions that steer agent behavior, while sensors are reactive checks that detect issues before they reach human review. This article focuses on one type of sensor: static analysis through basic code linting. Linting acts as an early warning system, catching style inconsistencies, potential bugs, and maintainability red flags in generated code. The underlying principle is that automated feedback loops increase the probability of good agent outputs and enable self-correction during the development process. Fowler presents this as part of an ongoing series, emphasizing the practical value of integrating such sensors into agent workflows to keep codebases maintainable.

- Coding agent harnesses require both guides (proactive instructions) and sensors (reactive checks) to ensure quality.
- Static analysis with basic code linting serves as an initial sensor for detecting maintainability issues.
- Sensors enable self-correction before issues reach human reviewers, increasing output reliability.
- The approach is part of a larger effort to systematically engineer agent workflows for code maintenance.