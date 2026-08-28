---
domain: ai-workflows
subdomain: coding-agent-harness
concept: maintainability-sensors
title: Maintainability sensors for coding agents
sources:
  - title: "Maintainability sensors for coding agents"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html#TheTestSuiteAsARegressionSensor"
    author: "Martin Fowler"
    date: "2026-05-27"
---

# Maintainability sensors for coding agents

Martin Fowler's article explores how coding agents can be guided and corrected through a system of sensors that monitor codebase maintainability. He defines maintainability as the ease and low risk of changing code over time, and argues that AI agents suffer from tangled codebases in similar ways to humans—they may look in the wrong places, create inconsistencies, or need excessive context. To experiment, Fowler rebuilt an internal analytics dashboard (TypeScript, NextJS, React) entirely with AI, deliberately skipping guide files and relying only on sensor feedback.

The sensor architecture spans the development lifecycle: in-session tools (type checker, ESLint, Semgrep, dependency-cruiser, test suite, mutation testing, GitLeaks), CI pipeline checks, and scheduled reviews (security, data handling, dependency freshness, modularity). A key innovation is embedding self-correction guidance directly into sensor messages—for example, a custom ESLint formatter tells the agent when it can suppress warnings or adjust thresholds, turning the tool into a prompt injection mechanism that shapes agent behavior. Fowler found that static analysis rules targeting AI failure modes (argument count, file/function length, complexity) require explicit configuration and custom guidance to be effective.

Dependency rules, created with dependency-cruiser, proved valuable for enforcing a layered architecture; Fowler noted that AI absorbed the tool's steep configuration overhead and self-corrected when rules were violated. Coupling metrics, generated via a custom TypeScript compiler-based tool, offered detailed DSM visualizations but were tedious and difficult to interpret, even for humans. Fowler concludes that sensors reduce the cost and increase the benefit of static analysis, but warns of feedback overload, false confidence, and the risk of AI over-engineering when rules are too aggressive.

- Sensors give coding agents fast, actionable feedback for self-correction before human code review, with custom messages acting as guidance for judgment calls.
- ESLint and similar tools need explicit rule configuration and AI-aware custom messages to target common AI failure modes (e.g., excessive args, complexity, file length).
- dependency-cruiser rules effectively enforce modular boundaries and layered architecture; AI can generate these rules and self-correct based on their feedback.
- Coupling metrics provide deep structural insight but are hard to interpret, suggesting deterministic tools need pairing with inferential, AI-generated analysis.
- The cost-benefit balance of static analysis improves with AI: cheaper rule creation and higher benefit, but risk of feedback overload and false sense of quality remains.