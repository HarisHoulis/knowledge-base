---
domain: android-kotlin
subdomain: test-driven-development
concept: clock-abstraction-tdd
title: Kotlin TDD - To Production At Last
sources:
  - title: "Kotlin TDD - To Production At Last"
    url: "https://www.youtube.com/watch?v=UH7_kYAG-TE"
    author: "Pairing with Duncan"
    date: "2022-03-05T20:10:25+00:00"
---

# Kotlin TDD - To Production At Last

In this Kotlin TDD pairing session, Duncan and his partner work to integrate a stock update feature into production by re-enabling a previously disabled test that fails. They move the Stock class from the test tree into the main tree, allowing the application routes to use it instead of directly loading items from a stock file. To enable the stock to update based on the current time, they introduce a clock as a functional parameter that returns an Instant, replacing the previously used Instant.now() call directly in main code. This allows tests to control time precisely by passing specific Instant values. The session also highlights the shift from LocalDate to Instant in test fixtures, ensuring that date and time are consistent. The team commits the work in progress as a demonstration of an incremental TDD workflow (Duncan, 2022).

- Re-enable a failing test to drive the integration of new functionality into production code.
- Move production code from test sources to main sources to make it usable by the application.
- Inject a clock function (returning Instant) instead of calling Instant.now() directly to control time in tests.
- Refactor test fixtures to derive dates from Instants, maintaining consistency between time and date.
- Use WIP commits to checkpoint progress during a TDD flow.