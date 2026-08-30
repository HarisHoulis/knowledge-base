---
domain: ai-workflows
subdomain: ai-agent-testing
concept: test-deletion-loop
title: I Delete Tests Every Night (On Purpose)
sources:
  - title: "I Delete Tests Every Night (On Purpose)"
    url: "https://www.youtube.com/watch?v=5C0jTimK8V0"
    author: "Kent C. Dodds"
    date: "2026-08-04T18:05:35+00:00"
---

# I Delete Tests Every Night (On Purpose)

Kent C. Dodds explains his nightly practice of having an AI agent delete tests from his codebase, resulting in a PR that removes more lines than it adds every morning (Dodds, 2026). He stresses that while he is known as a testing advocate, he is highly intentional about tests and believes that more tests do not automatically mean better tests. Low-value tests—such as flaky, broken, or duplicate tests with tiny cases and wrappers—are a burden rather than a benefit.

The true expense of tests is not in creating them, since AI agents can generate them cheaply, but in the time it takes to run them and the friction they cause when AI agents make changes. AI agents tend to produce excessive tests, including tiny one-assertion tests, duplicates covering the same behavior elsewhere, assertions that pin down constant values by importing and re-checking them, and tests for edge cases that will never occur (Dodds, 2026).

The purpose of a good test suite is confidence that software will not break. Many green checks do not necessarily lead to more confidence; a bloated suite is slower, harder to change, and can still miss the actual user journey that matters. Dodds documents testing principles in a testing-principles.md file referenced from agents.md, but agents do not fully follow those principles, so he delegates nightly test deletion to an AI agent to keep the suite lean and maintain a healthy software factory (Dodds, 2026).

- More tests does not equal better tests; low-signal, duplicated, and overly specific tests reduce confidence.
- AI agents tend to generate excessive tests, including single-assertion cases, tautological constant checks, and tests for impossible edge cases.
- A healthy test suite is fast, easy to change, and focuses on validating actual user journeys.
- Automated nightly PRs that delete tests can counterbalance AI's tendency to add code and keep the codebase in tip-top shape.