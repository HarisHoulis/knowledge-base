---
domain: ai-workflows
subdomain: coding-agents
concept: static-analysis-sensors
title: Three more static code analysis sensors
sources:
  - title: "Three more static code analysis sensors"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html#StaticCodeAnalysisDependencyRules"
    author: "Martin Fowler"
---

# Three more static code analysis sensors

The article discusses three additional sensors for static code analysis in the context of coding agents, focusing on improving modularity. Dependency check sensors are effective at enforcing rules but are limited by the expressiveness of the rules themselves. A sensor for coupling data proved ineffective. In contrast, prompting an inferential sensor to review modularity yielded better results, suggesting that a more flexible approach can outperform rigid computational checks.

- Dependency checks as computational sensors are good at enforcing rules but have limited rule expressiveness.
- A computational sensor for coupling data proved lackluster.
- An inferential sensor prompted to review modularity was more effective.
- The focus is on checking and enforcing better modularity in code.