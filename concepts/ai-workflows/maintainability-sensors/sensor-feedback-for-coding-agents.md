---
domain: ai-workflows
subdomain: maintainability-sensors
concept: sensor-feedback-for-coding-agents
title: The test suite as a regression sensor
sources:
  - title: "Maintainability sensors for coding agents"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html#TheTestSuiteAsARegressionSensor"
    author: "Martin Fowler"
    date: "27 May 2026"
---

# The test suite as a regression sensor

Martin Fowler's article explores using maintainability sensors as feedback loops for coding agents, arguing that agents can self-correct when given the right signals. The author describes building an internal analytics dashboard with AI-driven development and setting up sensors that run during coding sessions, in CI, and on a schedule. These sensors include static analysis tools like ESLint and Semgrep, structural rules via dependency-cruiser, mutation testing, and inferential reviews. The key insight is that custom guidance embedded in sensor messages (e.g., lint rule explanations) acts as 'good prompt injection,' helping agents make nuanced decisions like when to suppress a warning with a reason or increase a threshold slightly rather than ignore it.

- Custom lint messages that explain rules and offer guidance enable agents to self-correct, e.g., by suppressing warnings with explicit reasons or slightly increasing thresholds only when justified.
- AI dramatically reduces the setup cost for structural tools like dependency-cruiser, making it feasible to enforce architectural layers and see agents comply with and self-correct against these rules.
- Coupling metrics give mixed results: human-oriented visualizations are hard to interpret, but a CLI interface can feed the same metrics to agents for actionable feedback.
- Static analysis can catch common AI failure modes, but should be tuned to avoid feedback overload and the illusion of quality—many fine-grained rules produce noise and may trigger over-engineering.
- Human review of AI-generated exceptions (suppressed warnings, threshold changes) is a valuable entry point for code review and reveals where guidance is missing.