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

In this video, the team integrates a previously developed stock update feature into production code using test-driven development. They start by re-enabling a disabled test that defines the expected behavior, then move the stock class from the test tree into the main source tree. The implementation requires passing a clock function into the stock logic so that the current time can be injected, making tests deterministic. They refactor the test fixture to use an Instant instead of a LocalDate to accurately capture time-based updates, and adjust all tests accordingly. After wiring everything together, they commit a work-in-progress checkpoint as a safe stopping point.

- Re-enable the failing test to guide production integration.
- Move production code from test tree to main tree for actual use.
- Introduce a clock function parameter to allow time control in tests.
- Use Instant instead of LocalDate for precise time-based assertions.
- Commit work-in-progress after completing a coherent step.