---
domain: ai-workflows
subdomain: maintainability-sensors
concept: sensor-feedback-for-coding-agents
title: Maintainability sensors for coding agents
sources:
  - title: "Maintainability sensors for coding agents"
    url: "https://martinfowler.com/articles/sensors-for-coding-agents.html"
    author: "Martin Fowler"
    date: "2026-05-27"
---

# Maintainability sensors for coding agents

In his article "Maintainability sensors for coding agents," Martin Fowler describes his experimentation with using automated sensors to help AI coding agents keep a codebase maintainable. He defines maintainability as the ease and safety of making future changes, and notes that AI agents hitting tangled code tend to look in wrong places, create inconsistencies, or require excessive context. He distinguishes between computational sensors (e.g., type checker, ESLint, dependency-cruiser, tests) and inferential sensors (e.g., AI-generated security or data-handling reviews) that run during coding sessions, in CI, and repeatedly to detect drift. Fowler emphasizes that these sensors provide feedback for agents to self-correct, especially when messages include contextual guidance—a form of prompt injection (Fowler, 2026).

Fowler highlights several practical findings. Basic linting rules like max arguments, file length, and cyclomatic complexity are not in ESLint's default preset, but adding them—with custom formatter messages that explain the rationale and allow suppression with justification—helped AI avoid common failure modes and kept violations manageable. He also used dependency-cruiser to enforce a layered module structure, which helped the agent clean up haphazard folder organization and self-correct when it violated import rules. For coupling metrics, he had an agent build custom tools that output dependency structure matrices for humans and CLI data for agents; while the visualizations were tedious to interpret, the data was valuable. Fowler observed that AI could handle and manage warnings, but also warned about false security and feedback overload, and noted that more semantic aspects of quality remain uncovered (Fowler, 2026).

- Custom lint messages with self-correction guidance enable AI agents to fix maintainability issues while maintaining human oversight.
- Dependency rules (e.g., via dependency-cruiser) can enforce modularity and layering, and AI can absorb the configuration cost.
- Sensors run at different stages—during coding, in CI, and repeatedly—to catch both immediate errors and long-term drift.
- AI agents can help create static analysis tools and custom scripts, lowering the cost of setting up enforceable constraints.
- Static analysis can create an illusion of quality; semantic issues and trade-offs between rules require human judgment.