---
domain: android-kotlin
subdomain: test-driven-development
concept: degrading-items-after-sell-by
title: Kotlin TDD: More Degrading
sources:
  - title: "Kotlin TDD - More Degrading"
    url: "https://www.youtube.com/watch?v=N_ArZ2yHEm8"
    author: "Pairing with Duncan"
    date: "2022-03-29"
---

# Kotlin TDD: More Degrading

In this session, the team continues working on a Gilded Rose-style item quality system. The new requirement is that items degrade twice as fast after their sell-by date: quality drops by 2 per day after the sell-by date instead of 1 before it. They begin by simplifying existing tests, replacing list-level tests with direct tests on `item.updatedBy`, making the tests shorter and more focused (Pairing with Duncan, 2022).

To handle the concept of "after sell-by date," they add a `LocalDate` parameter to `updatedBy` so the function knows the current date instead of relying on a system clock. Tests are updated with a fixed date, and a failing test is added for the new behavior. Initially, production code passes the item's sell-by date to keep everything compiling (Pairing with Duncan, 2022).

The implementation is then refactored to apply quality changes day by day. A loop repeats the daily degradation, and the decrement is set to 2 when the provided date is after the sell-by date, otherwise 1. This makes the failing test pass while preserving all previous behavior (Pairing with Duncan, 2022).

- Refactored tests to call `item.updatedBy` directly instead of testing through a list wrapper.
- Added a `LocalDate` parameter to `updatedBy` to make time-dependent behavior testable.
- Wrote a failing test for quality decreasing by 2 per day after the sell-by date.
- Implemented the behavior by looping over each day and using a decrement of 2 after sell-by date, 1 otherwise.