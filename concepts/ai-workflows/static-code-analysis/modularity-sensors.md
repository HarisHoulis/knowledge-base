---
domain: ai-workflows
subdomain: static-code-analysis
concept: modularity-sensors
title: Three More Static Code Analysis Sensors
sources:
  - title: "Three More Static Code Analysis Sensors"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html#StaticCodeAnalysisDependencyRules"
    author: "Birgitta Böckeler"
---

# Three More Static Code Analysis Sensors

The article discusses three additional sensors for static code analysis in the context of coding agents, focusing on checking and enforcing better modularity. Computational sensors for dependency checks were found to be effective at enforcing predefined rules, but the rules themselves were limited in scope. A computational sensor designed to analyze coupling data proved lackluster, failing to provide useful insights. In contrast, prompting an inferential sensor to review modularity was more effective, suggesting that a more flexible, AI-driven approach may be better suited for assessing architectural qualities like modularity.

- Computational dependency-rule sensors are good at enforcing explicit rules but limited by those rules.
- A computational sensor for coupling data was lackluster and ineffective.
- An inferential sensor prompted to review modularity proved more effective.
- The focus is on improving modularity through static code analysis sensors.