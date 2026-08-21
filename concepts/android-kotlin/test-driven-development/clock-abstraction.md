---
domain: android-kotlin
subdomain: test-driven-development
concept: clock-abstraction
title: Kotlin TDD: To Production At Last
sources:
  - title: "Kotlin TDD - To Production At Last"
    url: "https://www.youtube.com/watch?v=UH7_kYAG-TE"
    author: "Pairing with Duncan"
    date: "2022-03-05T20:10:25+00:00"
---

# Kotlin TDD: To Production At Last

In this session, the team integrates a stock update feature into production, guided by a previously disabled test. They re-enable the test, confirm it fails, and then move the Stock class from the test tree into the main source tree. Dependencies such as time zone and update strategy are wired into the main routes, enabling the stock list to be resolved through the new Stock object (Pairing with Duncan, 2022).

To make the feature testable, the team replaces direct calls to Instant.now() with a clock strategy—a function parameter that returns an Instant. This requires updating test fixtures to pass an Instant rather than a LocalDate, and adjusting the update logic to derive the current date from this clock. They also rename a variable from 'now' to 'today' for clarity, and later plan to derive one from the other to keep test data consistent (Pairing with Duncan, 2022).

- Re-enable the disabled test to drive the integration work.
- Move production code from test tree to main tree for reusability.
- Abstract time behind a clock function to control instants in tests.
- Replace LocalDate with Instant in fixtures to capture precise timing.
- Derive test dates from the clock to maintain consistency.