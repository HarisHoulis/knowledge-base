---
domain: android-kotlin
subdomain: test-driven-development
concept: clock-injection
title: Kotlin TDD - To Production At Last
sources:
  - title: "Kotlin TDD - To Production At Last"
    url: "https://www.youtube.com/watch?v=UH7_kYAG-TE"
    author: "Pairing with Duncan"
    date: "2022-03-05T20:10:25+00:00"
---

# Kotlin TDD - To Production At Last

In this TDD session, the team integrates a stock update feature into a Kotlin web application. They re-enable a previously disabled test that verifies stock quantities update when viewed in the browser, then move the Stock class from test code to production code and wire it into the route handler. Initially, the update logic uses Instant.now(), making it impossible to control time in tests. To solve this, they introduce a clock as a functional parameter (() -> Instant) injected into Stock, allowing tests to supply a fixed instant. They refactor test fixtures from LocalDate to Instant, deriving dates from the same instant to maintain consistency. This change makes the tests pass deterministically and demonstrates a key strategy for testing time-dependent behavior. The session ends with a work-in-progress commit, acknowledging further cleanup is needed, but the core integration is successfully completed (Pairing with Duncan, 2022).

- Re-enable disabled tests to drive the implementation and confirm expected behavior.
- Move production code from test tree to main tree to make it reusable.
- Inject a clock function (() -> Instant) instead of relying on Instant.now() for testability.
- Refactor test fixtures to use Instant and derive dates from the same instant to keep tests coherent.
- Use TDD to guide refactoring and commit work-in-progress after passing tests.