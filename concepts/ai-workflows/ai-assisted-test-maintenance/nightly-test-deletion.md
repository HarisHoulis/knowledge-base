---
domain: ai-workflows
subdomain: ai-assisted-test-maintenance
concept: nightly-test-deletion
title: I Delete Tests Every Night (On Purpose)
sources:
  - title: "I Delete Tests Every Night (On Purpose)"
    url: "https://www.youtube.com/watch?v=5C0jTimK8V0"
    author: "Kent C. Dodds"
    date: "2026-08-04T18:05:35+00:00"
---

# I Delete Tests Every Night (On Purpose)

Kent C. Dodds explains his nightly routine where an AI agent deletes tests from his codebase, producing a PR that removes more lines than it adds. He argues that while AI has made test creation cheap, tests carry ongoing costs: they slow down CI, make changes harder for AI agents, and often provide low signal. The purpose of a test suite is confidence, not sheer volume, and many AI-generated tests fail to meaningfully validate user journeys (Dodds, 2026).

Dodds identifies common low-value patterns in AI-written tests: tiny tests that import a constant and assert its value, tests that pin exact error strings, tests for edge cases that can never occur, and many single-assertion tests that duplicate the same coverage. These bloat the suite and increase maintenance burden without improving confidence. He notes that agents often don't realize coverage already exists elsewhere, leading to redundant tests.

To counter this, Dodds maintains a testing-principles.md file referenced by his AI agent, but he still finds nightly deletion necessary because current agents are not yet capable of self-curating their tests. He emphasizes that being intentional about tests—removing flaky, broken, or low-signal tests—is a durable skill that remains valuable even as AI improves (Dodds, 2026).

- AI-generated tests often produce low-value assertions that duplicate coverage or pin trivial constants.
- Tests are expensive to maintain because they slow CI and complicate AI-driven code changes.
- A good test suite is about confidence in user journeys, not the number of green checks.
- Deleting tests nightly is an AI workflow that keeps the codebase healthy without manual overhead.
- Documenting testing principles helps, but agents still need human-curated cleanup.