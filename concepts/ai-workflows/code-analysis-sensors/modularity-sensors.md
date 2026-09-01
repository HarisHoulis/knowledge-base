---
domain: ai-workflows
subdomain: code-analysis-sensors
concept: modularity-sensors
title: Three More Static Code Analysis Sensors
sources:
  - title: "Three more static code analysis sensors"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html#StaticCodeAnalysisDependencyRules"
    author: "Martin Fowler"
---

# Three More Static Code Analysis Sensors

The article, contributed by Birgitta Böckeler and published by Martin Fowler, explores three additional sensors for static code analysis that aim to improve modularity assessment in codebases. Computational sensors for dependency checks proved effective at enforcing predefined rules but were limited in their expressiveness, failing to capture more nuanced architectural concerns. Building a computational sensor to analyze coupling data was lackluster, yielding poor insights that did not justify the effort. In contrast, prompting an inferential sensor—likely an AI-based reviewer—to assess modularity was more effective, suggesting that inferred analysis can complement or even surpass computational metrics for evaluating architectural quality. This highlights the growing value of AI-driven approaches in code analysis workflows (source: https://martinfowler.com/articles/sensors-for-coding-agents.html#StaticCodeAnalysisDependencyRules).

- Dependency-check computational sensors enforce modularity rules but are limited in what they can express.
- A computational sensor for coupling data performed poorly, providing little actionable insight.
- Prompting an inferential sensor to review modularity proved more effective, indicating AI's potential in code quality analysis.