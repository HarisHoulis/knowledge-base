---
domain: ai-workflows
subdomain: static-analysis-sensors
concept: modularity-review-sensors
title: Three More Static Code Analysis Sensors
sources:
  - title: "Three more static code analysis sensors"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html#StaticCodeAnalysisDependencyRules"
    author: "Martin Fowler"
---

# Three More Static Code Analysis Sensors

The most promising approach was an inferential sensor that prompted an AI agent to review modularity qualitatively. This method outperformed the computational sensors by leveraging context and reasoning to identify architectural issues that static rules or metrics might miss. The findings suggest that for abstract and emergent qualities like modularity, inferential sensors are a more effective tool for AI-driven code analysis, while computational sensors remain useful for explicit, well-defined constraints (Martin Fowler, https://martinfowler.com/articles/sensors-for-coding-agents.html#StaticCodeAnalysisDependencyRules).

- Three additional static code analysis sensors were introduced focusing on modularity enforcement and review.
- Computational dependency-rule sensors enforce rules well but are limited by the rules' expressiveness.
- A computational sensor for coupling data was ineffective, failing to yield actionable insights.
- An inferential sensor that reviews modularity via prompting proved more effective than computational counterparts.
- For qualitative architectural concerns, inferential sensors are preferable, while computational sensors suit explicit rules.