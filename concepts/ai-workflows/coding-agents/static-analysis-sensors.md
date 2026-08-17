---
domain: ai-workflows
subdomain: coding-agents
concept: static-analysis-sensors
title: Three More Static Code Analysis Sensors
sources:
  - title: "Three more static code analysis sensors"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html#StaticCodeAnalysisDependencyRules"
    author: "Birgitta Böckeler"
---

# Three More Static Code Analysis Sensors

Birgitta Böckeler discusses three additional sensors for static code analysis in the context of coding agents, focusing on checking and enforcing better modularity. Computational sensors for dependency checks were effective at enforcing predefined rules but limited in scope, as the rules themselves were constrained and could not capture broader architectural concerns.

- Dependency-check sensors enforce modularity rules well, but the rules are inherently limited.
- A computational sensor for coupling data proved lackluster and not particularly useful.
- Prompting an inferential sensor to review modularity was more effective than computational alternatives.
- Sensor design for coding agents should consider the trade-off between rule-based enforcement and inferential review.