---
domain: ai-workflows
subdomain: coding-agents
concept: static-analysis-sensors
title: Three More Static Code Analysis Sensors
sources:
  - title: "Three more static code analysis sensors"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html#StaticCodeAnalysisDependencyRules"
    author: "Martin Fowler"
---

# Three More Static Code Analysis Sensors

Birgitta Böckeler discusses three additional sensors for static code analysis, focusing on checking and enforcing better modularity in codebases. Computational sensors for dependency checks proved effective at enforcing predefined rules, but the rules themselves were limited in scope and flexibility. A computational sensor for coupling data was attempted but yielded lackluster results, indicating that simple metrics may not capture the nuanced quality of modularity. In contrast, prompting an inferential sensor to review modularity was more effective, suggesting that AI-based reasoning can outperform rigid computational checks for architecture-level concerns. This highlights a shift toward using inferential sensors for higher-order code quality assessments.

- Computational dependency-rule sensors are good at enforcement but limited by rigid rules.
- A computational sensor for coupling data was ineffective at assessing modularity.
- An inferential sensor, prompted to review modularity, proved more effective.
- Inferential sensors may be better suited for architectural and design-level feedback.