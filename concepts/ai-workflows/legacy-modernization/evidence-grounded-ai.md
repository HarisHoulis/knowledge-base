---
domain: ai-workflows
subdomain: legacy-modernization
concept: evidence-grounded-ai
title: The Archaeologist's Copilot
sources:
  - title: "The Archaeologist's Copilot"
    url: "https://martinfowler.com/articles/archaeologist-copilot.html"
    author: "Martin Fowler"
---

# The Archaeologist's Copilot

This article by Martin Fowler describes how Nik Malykhin tackled the modernization of a Java 1.5 codebase to run on Java 8 and modern hardware. Initial uses of LLMs produced plausible but incorrect answers because they were not grounded in the actual codebase. The turning point came when the process was restructured around evidence, with AI used to support analysis rather than as a primary source of truth.

A stable Docker environment provided a consistent platform for validation, while gradual refactoring protected by tests allowed changes to be made incrementally. The key insight is that AI is most effective when constrained by evidence, clear roles, and a step-by-step modernization strategy. This practical approach transformed the AI from a speculative generator into a reliable copilot for the modernization effort.

- LLMs alone provide plausible but unreliable answers for legacy code; grounding in evidence is essential.
- A stable Docker environment enables consistent validation of AI-suggested changes.
- Gradual refactoring with test protection reduces risk and improves outcomes.
- AI is most effective when constrained by clear roles and a step-by-step modernization strategy.