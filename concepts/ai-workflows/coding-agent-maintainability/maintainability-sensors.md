---
domain: ai-workflows
subdomain: coding-agent-maintainability
concept: maintainability-sensors
title: Maintainability sensors for coding agents
sources:
  - title: "Maintainability sensors for coding agents"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html#TheTestSuiteAsARegressionSensor"
    author: "Martin Fowler"
    date: "27 May 2026"
---

# Maintainability sensors for coding agents

In this article, Martin Fowler describes his experiments with using sensors to help AI coding agents keep a codebase maintainable. He argues that beyond functional correctness, maintainability (internal quality) is critical for low-risk future changes, and that AI agents suffer from tangled codebases similarly to humans. He set up a system of computational and inferential sensors that run during the coding session, in CI, and on a schedule, providing feedback for agents to self-correct before issues reach human eyes (Fowler, 2026).

For static analysis, Fowler customized ESLint with self-correction guidance embedded in lint messages, targeting common AI failure modes like excessive arguments, file length, and complexity. He found that agents can manage warnings by making judgment calls, suppressing with reasons, or occasionally increasing thresholds, which keeps the baseline clean and makes exceptions visible for review. He also used dependency-cruiser to enforce a layered module structure, which helped the agent avoid crossing architectural boundaries and even self-correct when violations occurred (Fowler, 2026).

He explored coupling metrics via custom tooling, but found visualizations like DSM tedious to interpret, suggesting that coupling data requires significant context and may be less immediately useful. Overall, he observes that AI lowers the cost of creating and maintaining such sensors, but warns of potential feedback overload and a false sense of security, since these tools cannot capture semantic quality. He recommends using sensors as a complement to human review, not a replacement (Fowler, 2026).

- Custom lint rules with embedded guidance help agents self-correct on maintainability issues.
- Dependency rules (e.g., dependency-cruiser) are a cheap way to enforce layered architecture and prevent structural drift.
- AI reduces the cost of building sensor tooling, but may generate too much noise and require curation.
- Coupling metrics are hard to interpret and need more experimentation before proving useful.
- Sensors should complement human review, not replace it, to avoid a false sense of quality.