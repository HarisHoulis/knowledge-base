---
domain: engineering-culture
subdomain: static-analysis
concept: static-analysis-sensors
title: Three more static code analysis sensors
sources:
  - title: "Three more static code analysis sensors"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html#StaticCodeAnalysisDependencyRules"
    author: "Martin Fowler"
---

# Three more static code analysis sensors

The article discusses three additional sensors for static code analysis, specifically aimed at checking and enforcing better modularity in codebases. These sensors are part of a broader effort to use automated tooling to guide coding agents and developers toward improved software architecture.

Computational sensors that enforce dependency rules were found to be effective for enforcing existing constraints, but they are limited by the expressiveness of the rules themselves. A computational sensor designed to measure coupling data proved to be lackluster, as it did not provide meaningful insights beyond what simple metrics already offered.

In contrast, an inferential sensor that uses prompting to review modularity was more effective. By leveraging an AI model to reason about the code's structure, this approach could identify modularity issues that rule-based computational sensors could not capture. This suggests that a hybrid approach, combining precise computational checks with inferential AI analysis, may be more robust for modularity assessment.

- Three new static analysis sensors focus on modularity checking and enforcement.
- Computational dependency-rule sensors are good at enforcing existing rules but limited in rule expressiveness.
- A computational coupling-data sensor underperformed, providing little value.
- An inferential sensor prompted to review modularity was more effective than the computational alternatives.