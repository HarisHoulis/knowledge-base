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

Martin Fowler highlights Birgitta Böckeler's mental model for harness engineering, which expands a coding agent's harness with guides and sensors to improve output quality and enable self-correction before issues reach human review. The article focuses on the first part of Böckeler's experiences: using static analysis and basic code linting as sensors to keep a codebase maintainable. This approach treats tooling as an active filter that catches maintainability problems early in the agent-driven development loop.

By integrating static analysis into the agent harness, teams can automatically detect style violations, potential bugs, and structural issues, allowing the agent to iterate and fix them without human intervention. This reduces the risk of accumulating technical debt and ensures that the codebase remains clean as agents generate more code. The article suggests that such sensors are essential for scaling coding agent usage, as they provide feedback loops that maintain quality standards without overburdening human developers.

The discussion positions maintainability sensors as a practical extension of the harness, emphasizing that they are not just for validation but also for guidance. This aligns with the broader goal of making coding agents reliable partners in software development, capable of self-correcting and producing maintainable code (Martin Fowler, https://martinfowler.com/articles/sensors-for-coding-agents.html).

- Coding agent harnesses benefit from sensors that detect issues early, enabling self-correction before human review.
- Static analysis and basic code linting serve as initial maintainability sensors for agent-driven development.
- Sensors help prevent technical debt accumulation by catching style and structural problems in agent-generated code.
- The approach increases the probability of good agent outputs and reduces the need for human oversight.