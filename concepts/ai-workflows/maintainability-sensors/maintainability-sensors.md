---
domain: ai-workflows
subdomain: maintainability-sensors
concept: maintainability-sensors
title: Maintainability sensors for coding agents
sources:
  - title: "Maintainability sensors for coding agents"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html#TheTestSuiteAsARegressionSensor"
    author: "Martin Fowler"
    date: "2026-05-27"
---

# Maintainability sensors for coding agents

In this article, Martin Fowler describes his experimentation with sensors that help AI coding agents maintain codebase health and prevent regression. He defines maintainability as the ease and low risk of changing code over time, and notes that AI agents suffer from tangled codebases similarly to humans, looking in wrong places or creating inconsistencies. He sets up a layered sensor system running during coding sessions, in CI, on schedules, and in production, using tools like ESLint, Semgrep, dependency-cruiser, and custom coupling metrics (Fowler, 2026).

A key insight is that static analysis tools can be customized with self-correction guidance, turning lint warnings into prompts that tell the agent how to fix issues or make judgment calls. For example, Fowler built a custom ESLint formatter that explains why types matter and allows suppressing warnings with reasons, or increasing thresholds only when necessary. This shifts the cost-benefit balance: AI lowers the cost of creating custom rules, while the self-correction guidance amplifies the benefit. However, Fowler cautions against a false sense of security, as static analysis can't catch semantic quality issues and may overload agents with irrelevant feedback (Fowler, 2026).

Fowler also explores dependency rules and coupling metrics. Using dependency-cruiser, he enforced a layered module structure, and found that AI could both generate the rules and self-correct after violating them. He built custom coupling visualizations for humans and a CLI for agents, but found the data hard to interpret. Overall, the article demonstrates how sensors can guide AI to produce more maintainable code, but emphasizes the need for human judgment and careful design of feedback loops (Fowler, 2026).

- Custom lint messages with self-correction guidance enable AI to fix or suppress issues with judgment, reducing management overhead.
- Dependency rules (e.g., dependency-cruiser) help enforce module boundaries and are easier to create with AI assistance.
- Coupling metrics can be extracted and presented to both humans and agents, but interpretation remains challenging.
- AI frequently increased cyclomatic complexity thresholds when no explicit guidance was given, highlighting the need for clear constraints.
- Sensors offer fast feedback but risk a false sense of security and feedback overload; human review is still essential.