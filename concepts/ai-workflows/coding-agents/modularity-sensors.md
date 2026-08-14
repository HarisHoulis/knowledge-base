---
domain: ai-workflows
subdomain: coding-agents
concept: modularity-sensors
title: Three More Static Code Analysis Sensors for Coding Agents
sources:
  - title: "Three more static code analysis sensors"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html#StaticCodeAnalysisDependencyRules"
    author: "Martin Fowler"
---

# Three More Static Code Analysis Sensors for Coding Agents

Prompting an inferential sensor to review modularity was more effective, as it could reason about the broader context and identify issues beyond simple rule violations. This suggests that combining computational checks with inferential analysis can yield better results for code quality.

- Computational sensors for dependency checks enforce rules well but are limited by the rule set.
- A sensor built for coupling data did not deliver meaningful value.
- Inferential sensors that review modularity perform better at identifying structural issues.
- Using inferential sensors for modularity reviews can complement or surpass computational rule-based sensors.