---
domain: android-kotlin
subdomain: test-driven-development
concept: degrading-items
title: Kotlin TDD - More Degrading
sources:
  - title: "Kotlin TDD - More Degrading"
    url: "https://www.youtube.com/watch?v=N_ArZ2yHEm8"
    author: "Pairing with Duncan"
    date: "2022-03-29T21:59:23+00:00"
---

# Kotlin TDD - More Degrading

In this pair-programming session, the team implements a requirement where items degrade in quality twice as fast after their sell-by date. Previously, items lost one quality per day before and after the sell-by date. The new behavior requires a loss of two per day once the date has passed. The work begins by refactoring existing tests to call the `updatedBy` method directly instead of testing a list-mapping wrapper, simplifying the test suite and focusing on the core behavior (Pairing with Duncan, 2022).

To express the concept of "after sell-by date," the team adds a `LocalDate` parameter to the `updatedBy` method, representing the current date when the update is called. This allows tests to specify a concrete date and assert expected quality changes without relying on a clock. Initial production code passes the item's sell-by date as a temporary placeholder to keep compilation intact, then the implementation is reworked to loop over each day, applying a quality reduction of one per day normally and two per day after the sell-by date (Pairing with Duncan, 2022).

The final implementation computes a degradation factor based on whether the current date is after the sell-by date, then repeats the daily degradation for the number of days updated. This keeps the logic explicit and testable, and aligns with test-driven development by first adding a failing test for the new behavior (Pairing with Duncan, 2022).

- Refactor tests to target the core method directly, removing unnecessary list-mapping wrappers.
- Introduce a `LocalDate` parameter to `updatedBy` so tests can control the current date and define 'after sell-by date'.
- Implement degradation as a loop over days, reducing quality by one normally and two after the sell-by date.
- Use a breaking test first to drive the implementation, following a TDD red-green-refactor cycle.