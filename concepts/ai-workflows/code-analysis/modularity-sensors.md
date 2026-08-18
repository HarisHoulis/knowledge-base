---
domain: ai-workflows
subdomain: code-analysis
concept: modularity-sensors
title: Three more static code analysis sensors
sources:
  - title: "Three more static code analysis sensors"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html#StaticCodeAnalysisDependencyRules"
    author: "Martin Fowler"
---

# Three more static code analysis sensors

The article discusses three additional sensors for static code analysis in coding agents, focusing on measuring and enforcing modularity. Computational sensors that check dependency rules are effective for enforcing predefined constraints but are limited in the scope of rules they can express (https://martinfowler.com/articles/sensors-for-coding-agents.html#StaticCodeAnalysisDependencyRules). A computational sensor designed to measure coupling data proved lackluster, as it did not provide actionable insights. In contrast, prompting an inferential sensor to review modularity was more effective, suggesting that AI-based review can outperform rigid computational metrics for this task.

- Computational sensors for dependency checks are good at enforcing rules, but the rules themselves are limited.
- A computational sensor for coupling data was lackluster in practice.
- Prompting an inferential sensor to review modularity yielded better results.