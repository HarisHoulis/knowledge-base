---
domain: ai-workflows
subdomain: code-analysis
concept: static-code-analysis-sensors
title: Three More Static Code Analysis Sensors
sources:
  - title: "Three more static code analysis sensors"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html#StaticCodeAnalysisDependencyRules"
    author: "Birgitta Böckeler"
---

# Three More Static Code Analysis Sensors

Birgitta Böckeler discusses three additional sensors for static code analysis, focusing on checking and enforcing better modularity in codebases. The first sensor uses computational dependency checks to enforce rules, but these rules are inherently limited in scope. The second sensor, which computes coupling data, proved lackluster for improving modularity. The third sensor, an inferential approach that prompts a review of modularity, was more effective.

- Dependency-check sensors can enforce modularity rules but are limited by the rules' expressiveness.
- Coupling-data sensors were less effective at guiding modularity improvements.
- Inferential sensors that review modularity through prompts outperformed computational approaches.
- Static code analysis sensors can be categorized as computational or inferential, with inferential often better for subjective quality goals.