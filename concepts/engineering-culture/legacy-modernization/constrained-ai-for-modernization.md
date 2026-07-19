---
domain: engineering-culture
subdomain: legacy-modernization
concept: constrained-ai-for-modernization
title: The Archaeologist’s Copilot
sources:
  - title: "The Archaeologist’s Copilot"
    url: "https://martinfowler.com/articles/archaeologist-copilot.html"
    author: "Martin Fowler"
---

# The Archaeologist’s Copilot

Nik Malykhin faced the challenge of modernizing a Java 1.5 codebase to run on Java 8 with today's hardware. Early attempts using LLMs produced plausible but incorrect answers. Progress came by grounding AI in evidence: using generative AI to support analysis, validating in a stable Docker environment, and gradually refactoring with test protection. The key insight is that AI is most useful when constrained by evidence, clear roles, and a step-by-step strategy.

- Initial LLM use gave plausible but unreliable results for legacy code analysis.
- Grounding AI in evidence and validation (e.g., Docker environment) improved outcomes.
- Gradual refactoring protected by tests was essential for safe modernization.
- AI's role is best as a supportive tool, not a decision-maker, within a constrained process.