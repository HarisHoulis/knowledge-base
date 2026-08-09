---
domain: engineering-culture
subdomain: coding-agents
concept: modularity-sensors
title: Three more static code analysis sensors
sources:
  - title: "Three more static code analysis sensors"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html#StaticCodeAnalysisDependencyRules"
    author: "Martin Fowler (martin@martinfowler.com)"
---

# Three more static code analysis sensors

Birgitta Böckeler extends the discussion of sensors for coding agents by adding three more static code analysis sensors, focusing on checking and enforcing better modularity. The first sensor, a computational sensor for dependency checks, was effective at enforcing rules but limited by the expressiveness of those rules. The second sensor, a computational sensor for coupling data, proved lackluster in its results, suggesting that simple data-driven metrics may not capture modularity well. The third, an inferential sensor prompted to review modularity, was more effective, indicating that AI-based review can outperform rigid computational checks in assessing architectural quality. Overall, the article argues for a mix of sensor types, where inferential sensors can complement computational ones to improve modularity enforcement.

- Computational dependency-check sensors are good at enforcing explicit rules but the rules themselves are limited.
- A computational sensor for coupling data performed poorly, suggesting raw metrics are insufficient.
- An inferential sensor prompted to review modularity was more effective than the computational coupling approach.
- Inferential sensors may offer a better path for assessing modularity in codebases where explicit rules are hard to define.