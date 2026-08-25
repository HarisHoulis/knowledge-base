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

The video demonstrates a TDD workflow for delivering a story that updates stock quantities in the browser. The team re-enables a disabled test to confirm expected behavior, then moves the Stock class from the test tree into the main source tree to integrate it. They wire the Stock class into the route handler, replacing the previous direct stock file loading, and introduce a function parameter for the clock to return an Instant instead of using Instant.now() directly, making time control possible in tests. The test fixtures are updated to pass an Instant rather than a LocalDate, and the date is derived from the instant to maintain consistency. After running the tests, they pass, and the work is committed as a work-in-progress (WIP).

- Re-enable failing tests to drive integration work
- Move code from test tree to main tree for production use
- Inject a clock function (returning Instant) to make time testable
- Replace LocalDate with Instant for time-sensitive operations
- Derive fixture date from instant to keep test data consistent