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

In this video, the team integrates the stock update feature into the main application by moving the `Stock` class from the test tree to the main source set. They re-enable a previously disabled test that describes the expected behavior, and then wire up the routes to use the `Stock` class instead of directly loading items from the stock file. The initial integration fails because the code uses `Instant.now()` directly, which makes it untestable. To fix this, they introduce a `clock` functional parameter that returns an `Instant`, allowing tests to control time. They refactor the test fixture to include an `instant` property, and change the update logic to accept an `Instant` instead of a `LocalDate`, since time zone information is needed for correct updating. They derive the date and time from the same source to keep consistency, and make a work-in-progress commit before continuing.

- Move production code from test tree to main tree to make it usable.
- Inject a clock function to control time in tests and make the system testable.
- Replace `LocalDate` with `Instant` for time-aware stock updates.
- Derive date and time from the same fixture value to avoid inconsistencies.
- Use a disabled test as a specification to drive the integration.