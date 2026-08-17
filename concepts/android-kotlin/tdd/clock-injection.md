---
domain: android-kotlin
subdomain: tdd
concept: clock-injection
title: Kotlin TDD - To Production At Last
sources:
  - title: "Kotlin TDD - To Production At Last"
    url: "https://www.youtube.com/watch?v=UH7_kYAG-TE"
    author: "Pairing with Duncan"
    date: "2022-03-05T20:10:25+00:00"
---

# Kotlin TDD - To Production At Last

The team is integrating a story where viewing stock in the browser updates quantities. They re-enable a disabled test that specifies the required behavior, then move the `Stock` class from the test tree into the main source tree to wire it into the routes. Initially, `Stock` uses `Instant.now()` to update, which makes testing problematic because the current time cannot be controlled (source: https://www.youtube.com/watch?v=UH7_kYAG-TE).

To resolve this, they introduce a `clock` function parameter that returns an `Instant`, allowing tests to provide a fixed time. This requires updating test fixtures to use `Instant` instead of `LocalDate`, and they derive the date from the instant to keep consistency across test data. The changes are committed as work-in-progress, acknowledging that further fixes will follow (source: https://www.youtube.com/watch?v=UH7_kYAG-TE).

The key technical insight is the use of dependency injection for time to make code testable and deterministic in TDD workflows, enabling integration of time-dependent features without flaky tests (source: https://www.youtube.com/watch?v=UH7_kYAG-TE).

- Re-enable a failing integration test to guide the wiring of the Stock class.
- Move production code from test tree to main tree for integration.
- Introduce a clock function parameter to inject time and make tests deterministic.
- Prefer Instant over LocalDate for precise time control in update logic.
- Refactor test fixtures to derive dates from the injected instant to avoid inconsistency.