---
domain: ai-workflows
subdomain: coding-agents
concept: maintainability-sensors
title: Maintainability sensors for coding agents
sources:
  - title: "Maintainability sensors for coding agents"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html"
    author: "Martin Fowler"
---

# Maintainability sensors for coding agents

The article introduces the concept of a harness for coding agents, expanding on Birgitta Böckeler's mental model that includes guides and sensors to increase the probability of good agent outputs and enable self-correction before issues reach human eyes. The focus is on using sensors to keep a codebase maintainable, starting with static analysis through basic code linting. This is part of a series where Böckeler shares her experiences with implementing such sensors in practice.

- Coding agent harnesses consist of guides and sensors that improve output quality and enable self-correction.
- Sensors are designed to catch maintainability issues early, before human review.
- Static analysis with basic code linting is the first type of sensor explored.
- The approach is based on real experiences by Birgitta Böckeler, highlighted by Martin Fowler.