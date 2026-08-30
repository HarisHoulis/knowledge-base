---
domain: android-kotlin
subdomain: test-driven-development
concept: time-aware-degradation
title: Kotlin TDD - More Degrading
sources:
  - title: "Kotlin TDD - More Degrading"
    url: "https://www.youtube.com/watch?v=N_ArZ2yHEm8"
    author: "Duncan"
    date: "2022-03-29T21:59:23+00:00"
---

# Kotlin TDD - More Degrading

The video demonstrates a Kotlin TDD session implementing a new requirement: items degrade faster after their sell-by date. Previously, item quality decreased by 1 per day before the sell-by date; now it must decrease by 2 per day after that date. The session begins by refactoring existing tests to remove unnecessary list handling, changing `updateItems` to directly call `item.updatedBy(days)` [1].

- Use TDD: add a failing test for the new degradation behavior before implementing.
- Refactor tests to focus on single item behavior rather than list mapping.
- Introduce a time parameter (`LocalDate`) to make the function testable.
- Implement degradation as a per-day loop with conditional rate (2 after sell-by, 1 before).