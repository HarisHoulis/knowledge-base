---
domain: ai-workflows
subdomain: static-analysis-sensors
concept: modularity-sensors
title: Three More Static Code Analysis Sensors
sources:
  - title: "Three More Static Code Analysis Sensors"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html#StaticCodeAnalysisDependencyRules"
    author: "Martin Fowler"
---

# Three More Static Code Analysis Sensors

Birgitta Böckeler discusses three more static code analysis sensors for coding agents, focusing on checking and enforcing better modularity (Fowler, https://martinfowler.com/articles/sensors-for-coding-agents.html#StaticCodeAnalysisDependencyRules). The discussion evaluates different sensor designs for understanding and improving code structure.

Computational sensors for dependency checks were effective at enforcing rules, but the rules themselves were limited in what they could express. Building a computational sensor specifically for coupling data proved lackluster, suggesting that simple metric-based approaches do not capture modularity well.

Prompting an inferential sensor to review modularity was more effective than the computational approaches. This indicates that for modularity analysis, inferential reasoning based on high-level prompts can outperform rule-based sensors, offering a practical path for coding agents to assess and maintain software architecture.

- Computational sensors for dependency checks were good at enforcing rules, but the rules were limited.
- Building a computational sensor for coupling data proved lackluster.
- Prompting an inferential sensor to review modularity was more effective than computational sensors.