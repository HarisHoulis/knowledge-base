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

In this coding session, the team implements a new requirement: items degrade twice as fast after their sell-by date, with quality decreasing by two per day rather than one (Pairing with Duncan, 2022). The work begins by cleaning up existing tests so they directly target the `updatedBy` method instead of wrapping it in a list operation, making tests simpler and more focused.

To handle the temporal behavior, a `LocalDate` parameter is added to `updatedBy` so tests can specify the current date; existing tests are updated with a default date of October 29th. The production code initially passes the item's sell-by date to keep it compiling.

The logic is then reworked to apply a daily degradation loop, where the degradation rate is two if the current date is after the sell-by date, otherwise one. This makes the failing test pass while preserving existing behavior.

- Refactored tests to test the `updatedBy` method directly rather than through a list mapping.
- Added a `LocalDate` parameter to `updatedBy` to make the behavior testable based on the current date.
- Implemented degradation as a repeated daily update, with rate 2 after sell-by date and 1 before.
- All tests pass, including the new test for faster degradation after sell-by date.