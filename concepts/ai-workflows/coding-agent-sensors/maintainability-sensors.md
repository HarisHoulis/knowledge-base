---
domain: ai-workflows
subdomain: coding-agent-sensors
concept: maintainability-sensors
title: Maintainability sensors for coding agents
sources:
  - title: "Maintainability sensors for coding agents"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html"
    author: "Martin Fowler"
    date: "2026-05-27"
---

# Maintainability sensors for coding agents

Martin Fowler's article explores how to maintain codebase quality when working with AI coding agents, proposing a 'sensor' approach that provides feedback and enables self-correction before issues reach human eyes. He defines maintainability as internal quality that makes changes easy and low-risk over time, and notes that AI agents are affected by tangled codebases similarly to human developers, often looking in wrong places or creating inconsistencies. The article argues that sensors—ranging from static analysis to test suites—are essential for catching regression and maintaining architectural fitness (Fowler, 2026).

Fowler describes experiments with static analysis tools like ESLint and dependency-cruiser, where he configured custom rules and self-correction guidance. For example, he added custom ESLint messages that instruct agents to make judgment calls about warnings like 'no-explicit-any', allowing suppression with reasons or threshold increases only as exceptions. This shifted the cost-benefit balance of static analysis, making it more feasible to maintain a 'clean house' with AI. However, he cautions about a false sense of security and feedback overload, as activating new rule sets often surfaced irrelevant issues alongside meaningful ones (Fowler, 2026).

The article also covers coupling metrics and modularity reviews. Fowler had an agent build a custom tool to visualize coupling data and provide it to coding agents via CLI, but found the visualizations tedious to interpret. Dependency rules proved useful for enforcing layered module structures, and agents self-corrected based on feedback. Yet, such tools are limited to what is expressible via imports and file structure, leaving semantic quality aspects to be filled by AI collaboration. Overall, sensors act as a practical guide for keeping AI-generated code maintainable, but they must be carefully tuned to avoid over-engineering (Fowler, 2026).

- Maintainability is critical for AI-generated codebases; sensors provide feedback that enables agents to self-correct before human review.
- Custom ESLint rules with self-correction guidance help manage AI failure modes like excessive function length, cyclomatic complexity, and type issues.
- Dependency rules (via dependency-cruiser) enforce module boundaries and layering, reducing haphazard code structure and guiding agents to follow architecture.
- Coupling metrics and modularity reviews add insight but are limited to structural aspects; semantic quality still requires human or AI judgment.
- The cost-benefit of static analysis improves with AI, but there is a risk of false confidence and feedback overload—sensor rules must be curated carefully.