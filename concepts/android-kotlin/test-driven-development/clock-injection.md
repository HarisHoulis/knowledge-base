---
domain: android-kotlin
subdomain: test-driven-development
concept: clock-injection
title: Kotlin TDD - To Production At Last
sources:
  - title: "Kotlin TDD - To Production At Last"
    url: "https://www.youtube.com/watch?v=UH7_kYAG-TE"
    author: "Pairing with Duncan"
    date: "2022-03-05"
---

# Kotlin TDD - To Production At Last

The team re-enables a disabled test that represents the requirement to view and update stock quantities in the browser. They move a Stock class from the test tree into the main tree so it can be used in production routes, replacing the direct stock file loading with the Stock class's stockList method, which handles updating quantities. To make the feature testable, they introduce a functional parameter called 'clock' that returns an Instant, allowing tests to control the current time instead of relying on Instant.now(). They refactor test fixtures to use Instant instead of LocalDate, deriving the 'today' value from the now instant, and pass a consistent clock into the system. The changes are committed as work-in-progress, with known issues to be fixed as development continues.

- Re-enable a disabled test to drive integration of the stock update feature.
- Move the Stock class from test tree to main tree for production use.
- Introduce a clock function parameter to make time injectable and tests deterministic.
- Replace LocalDate with Instant in test fixtures to precisely control time.
- Commit the integration as work-in-progress to be refined further.