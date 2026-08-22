---
domain: ai-workflows
subdomain: coding-agent-sensors
concept: maintainability-sensors
title: Maintainability sensors for coding agents
sources:
  - title: "Maintainability sensors for coding agents"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html#TheTestSuiteAsARegressionSensor"
    author: "Martin Fowler"
    date: "2026-05-27"
---

# Maintainability sensors for coding agents

Martin Fowler (2026) explores the use of sensors to maintain codebase maintainability when working with AI coding agents. He describes his experimentation with static code analysis tools such as ESLint, dependency-cruiser, and custom coupling metrics, emphasizing the importance of custom lint messages that provide self-correction guidance for agents. The article highlights how AI can manage warnings and threshold adjustments, and how dependency rules help preserve modular structure. Fowler also discusses the cost-benefit balance, noting that AI reduces the cost of creating custom rules while increasing the benefit of early feedback, but cautions against feedback overload and the illusion of quality from static analysis. The sensors are designed to run during coding sessions, in CI pipelines, and on a schedule to detect drift and maintainability issues before they reach human review.

- Custom ESLint messages with self-correction guidance allow AI to make judgment calls on warnings like 'no-explicit-any' and adjust thresholds only when necessary.
- Dependency rules via dependency-cruiser help enforce layered architecture and prevent agents from creating inconsistencies across file boundaries.
- Coupling metrics and visualizations are useful but tedious to interpret; providing them via CLI to agents enables automated feedback loops.
- Static analysis can cover common AI failure modes, but may create feedback overload and a false sense of security if not carefully managed.