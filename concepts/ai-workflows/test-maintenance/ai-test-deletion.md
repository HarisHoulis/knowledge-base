---
domain: ai-workflows
subdomain: test-maintenance
concept: ai-test-deletion
title: I Delete Tests Every Night (On Purpose)
sources:
  - title: "I Delete Tests Every Night (On Purpose)"
    url: "https://www.youtube.com/watch?v=5C0jTimK8V0"
    author: "Kent C. Dodds"
    date: "2026-08-04T18:05:35+00:00"
---

# I Delete Tests Every Night (On Purpose)

Kent C. Dodds shares his practice of having an AI agent delete tests every night, resulting in a PR that removes more lines than it adds. He argues that more tests do not necessarily mean better tests, and that AI-generated tests often add low-value, redundant, or trivial cases that increase maintenance and runtime costs without improving confidence. The core purpose of a test suite is to provide confidence, and bloated suites can undermine that by being slower and harder to change (Dodds, 2026).

To guide AI agents toward better testing behavior, Dodds maintains a testing principles file referenced by the agents file in his repository. This file documents principles such as testing user journeys, avoiding trivial assertions, and combining related assertions. Despite this, agents still produce tests that need pruning, so he runs a nightly cleanup cycle to keep the codebase in tip-top shape. This practice highlights a durable skill: being intentional about what makes tests valuable, which remains important even as AI capabilities improve (Dodds, 2026).

- AI agents tend to generate many tiny, low-signal tests, such as importing a constant and asserting its own value.
- Tests are expensive to run and maintain; more tests can reduce confidence if they make the suite slower and harder to change.
- A deliberate nightly test-deletion loop helps counterbalance AI's natural tendency to add code.
- Documenting testing principles for AI agents improves their output, but human oversight is still necessary.
- The ultimate goal of a test suite is confidence in the software, not a high test count.