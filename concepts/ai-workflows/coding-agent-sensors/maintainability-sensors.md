---
domain: ai-workflows
subdomain: coding-agent-sensors
concept: maintainability-sensors
title: Maintainability sensors for coding agents
sources:
  - title: "Maintainability sensors for coding agents"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html#TheTestSuiteAsARegressionSensor"
    author: "Martin Fowler"
    date: "27 May 2026"
---

# Maintainability sensors for coding agents

Martin Fowler explores how coding agents can be guided and self-corrected using a system of 'sensors' that monitor codebase maintainability. He argues that internal quality problems affect AI agents similarly to human developers, leading to misplaced lookups, inconsistencies, and excessive context loading. The article categorizes sensors into those that run during coding sessions, in CI pipelines, and on a repeated schedule, covering computational tools (type checkers, linters, dependency rules) and inferential reviews (security, data handling, modularity).

Fowler's key insight is that static analysis tools like ESLint can be repurposed for AI by customizing messages to include self-correction guidance, allowing the agent to make judgment calls (e.g., suppressing warnings with reasons or slightly adjusting thresholds). He observes that AI frequently increased cyclomatic complexity thresholds when guidance was absent, indicating the importance of explicit instructions to treat threshold changes as exceptions. He also found value in dependency rules (via dependency-cruiser) to enforce layered architecture, which the agent violated and then corrected based on feedback.

For coupling metrics, Fowler built custom tooling to visualize dependencies for humans and provide CLI metrics to agents. He found the visualizations tedious to interpret, but still useful for identifying architectural drift. The article concludes by questioning whether these sensors create a false sense of security, since they only capture certain aspects of quality and risk feedback overload that could lead to over-engineering.

- Sensors provide fast, iterative feedback that lets coding agents self-correct before human review, improving maintainability and reducing risk.
- Custom lint messages with self-correction guidance are more effective than default warnings; agents make better judgment calls when told to consider trade-offs and document suppressions.
- Enforcing layered architecture via dependency rules (e.g., dependency-cruiser) is a practical alternative to markdown guides, and AI can write the rules itself.
- Coupling metrics are useful for spotting drift, but raw data is hard to interpret; agents can consume the same data via CLI for automated analysis.
- Sensor feedback can lead to over-engineering if not carefully calibrated, and static analysis has semantic limits that AI must complement.