---
domain: ai-workflows
subdomain: ai-test-maintenance
concept: nightly-test-deletion
title: I Delete Tests Every Night (On Purpose)
sources:
  - title: "I Delete Tests Every Night (On Purpose)"
    url: "https://www.youtube.com/watch?v=5C0jTimK8V0"
    author: "Kent C. Dodds"
    date: "2026-08-04T18:05:35+00:00"
---

# I Delete Tests Every Night (On Purpose)

Kent C. Dodds describes his nightly ritual of having an AI agent create a PR that deletes more lines than it adds, specifically targeting tests. He argues that more tests do not mean better tests: he intentionally removes flaky, broken, or low-signal tests that have tiny cases, wrappers, or duplicates. The purpose of a test suite is to provide confidence, and many green checks do not necessarily increase confidence; they can make the suite slower and harder to change.

Tests are expensive not to create—AI agents generate them cheaply during implementation—but to run and to maintain. They slow down AI agents making localized changes because duplicate coverage may exist elsewhere, and agents often write tiny, low-value tests such as importing a constant and asserting its value, pinning every error string, testing edge cases that never happen, or splitting one behavior into many single-assertion tests.

To guide agents, Kent documents testing principles in a testing-principles.md file referenced by agents.md. However, agents don't fully follow it, so he compensates by deleting tests nightly. He emphasizes that a good test suite should validate user journeys, not just pin implementation details, and that intentional curation is necessary even as AI improves.

- More tests do not equal better tests; the goal of a test suite is confidence, not quantity.
- AI agents tend to generate low-signal tests: tiny single-assertion tests, duplicate coverage, impossible edge cases, and tests that pin implementation details.
- Tests have ongoing costs: they increase CI time and make it harder for AI agents to make changes.
- Documenting testing principles for agents (e.g., in testing-principles.md) helps but is insufficient; nightly deletion enforces test quality.
- A healthy test suite focuses on validating user journeys and avoids 'green check theater' from a bloated suite.