---
domain: ai-workflows
subdomain: test-suite-curation
concept: nightly-test-deletion
title: I Delete Tests Every Night (On Purpose)
sources:
  - title: "I Delete Tests Every Night (On Purpose)"
    url: "https://www.youtube.com/watch?v=5C0jTimK8V0"
    author: "Kent C. Dodds"
    date: "2026-08-04T18:05:35+00:00"
---

# I Delete Tests Every Night (On Purpose)

Kent C. Dodds explains his personal practice of having an AI agent delete low-value tests every night, resulting in a morning PR that removes more lines than it adds. He argues that AI-generated tests tend to be numerous but low-signal: they pin constants, duplicate coverage, test impossible edge cases, and break into single-assertion micro-tests. This bloats the test suite, slows down CI, and hampers AI agents from making changes confidently (Dodds, 2026).

Dodds emphasizes that the purpose of a test suite is confidence, not volume. More tests can actually reduce confidence by adding maintenance burden and hiding missing user-journey coverage. To combat this, he maintains a 'testing principles.md' file referenced from agents.md, which guides AI agents in writing better tests. Still, agents are not yet good enough, so he deliberately schedules nightly deletion of tests that violate those principles. This is part of a larger 'software factory' loop that keeps the codebase improving daily with minimal human involvement (Dodds, 2026).

- AI agents generate many low-value tests: tiny, duplicative, or overly specific assertions.
- More tests do not equal more confidence; tests are expensive to run and maintain.
- A nightly AI-generated PR that deletes tests helps keep the suite focused and fast.
- Documenting testing principles for agents (e.g., in testing-principles.md) improves, but doesn't fully solve, test quality.
- The ultimate goal is a test suite that validates real user journeys and enables confident changes.