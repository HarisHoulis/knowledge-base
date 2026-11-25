---
domain: ai-workflows
subdomain: llm-agent-architecture
concept: non-determinism-engineering-evals-grounding
title: Engineering Around Non-Determinism: Evals, Grounding, and Release Gates for AI-Drafted Suspicious Reports
sources:
  - title: "Engineering Around Non-Determinism: Evals, Grounding, and Release Gates for AI-Drafted Suspicious Reports"
    url: "https://www.infoq.com/articles/llm-agent-architecture-evals-grounding/"
    author: "Ritesh Modi, Sasidhar Gudala"
    date: "2026-11-24"
---

# Engineering Around Non-Determinism: Evals, Grounding, and Release Gates for AI-Drafted Suspicious Reports

Modi and Gudala argue that moving generative AI into high-stakes production requires treating non-determinism as an engineering problem rather than an unavoidable quirk. Their architectural blueprint targets agentic workflows that draft suspicious-activity reports, where compliance demands near-zero hallucination, and proposes grounding model output in knowledge graphs so that generated claims can be traced to authoritative data.

- Treat LLM non-determinism as an engineering problem to be controlled, not accepted
- Ground agent output in knowledge graphs to support zero-hallucination compliance
- Use dual-layer eval judges to assess generated drafts
- Enforce CI/CD release gates and regression tests against golden datasets before deployment