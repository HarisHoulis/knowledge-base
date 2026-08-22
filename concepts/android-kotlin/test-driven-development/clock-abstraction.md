---
domain: android-kotlin
subdomain: test-driven-development
concept: clock-abstraction
title: Kotlin TDD - To Production At Last
sources:
  - title: "Kotlin TDD - To Production At Last"
    url: "https://www.youtube.com/watch?v=UH7_kYAG-TE"
    author: "Pairing with Duncan"
    date: "2022-03-05T20:10:25+00:00"
---

# Kotlin TDD - To Production At Last

In this session, the team integrates a stock updating feature by moving a previously test-only class into the main source tree and wiring it into the application's routes. They re-enable a failing test that describes the expected behavior, then adapt the production code to use the new Stock class, which requires a zone and an update strategy. To make the code testable, they introduce a clock abstraction: a function parameter that returns an Instant, replacing direct calls to Instant.now() in production. This allows tests to control time precisely.

The team then refactors their test fixtures to provide an Instant instead of a LocalDate, aligning the tests with the new clock-based design. They parse specific instants for the end of the day and the start of the next day to validate the update logic. After adjusting all test call sites and ensuring they compile, they run the tests successfully and commit the changes as work in progress. This demonstrates a TDD workflow where testability concerns drive the introduction of a dependency injection point for time.

- Move production code from test tree to main source set to integrate features.
- Introduce a clock function parameter (returns Instant) to control time in tests.
- Replace LocalDate with Instant in test fixtures to match the new clock abstraction.
- Use dependency injection to make time-dependent code testable.
- Commit WIP after tests pass, acknowledging issues may remain.