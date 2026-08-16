---
domain: ai-workflows
subdomain: code-analysis-sensors
concept: static-analysis-sensors
title: Three More Static Code Analysis Sensors
sources:
  - title: "Three more static code analysis sensors"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html#StaticCodeAnalysisDependencyRules"
    author: "Martin Fowler"
---

# Three More Static Code Analysis Sensors

The article, based on analysis by Birgitta Böckeler, explores additional sensors for static code analysis in the context of coding agents, specifically targeting modularity. Computational sensors that enforce dependency rules are effective at enforcing those rules, but the rules themselves are limited in scope, making them insufficient for comprehensive modularity assessment. A sensor built around coupling data was tried but proved lackluster, as raw metrics do not capture the subtleties of good modular design. In contrast, prompting an inferential sensor to review modularity turned out to be markedly more effective, suggesting that AI-based qualitative review can outperform purely computational metrics for this kind of architectural concern.

- Dependency-rule sensors enforce modularity constraints well but only within a limited rule set.
- A computational sensor based on coupling data was not effective for assessing modularity.
- An inferential sensor that reviews modularity qualitatively proved more effective than computational sensors.
- For modularity, AI-driven review offers better insights than simple static metrics.