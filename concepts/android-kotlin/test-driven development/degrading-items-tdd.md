---
domain: android-kotlin
subdomain: test-driven development
concept: degrading-items-tdd
title: Kotlin TDD - More Degrading
sources:
  - title: "Kotlin TDD - More Degrading"
    url: "https://www.youtube.com/watch?v=N_ArZ2yHEm8"
    author: "Pairing with Duncan"
    date: "2022-03-29T21:59:23+00:00"
---

# Kotlin TDD - More Degrading

In this pair programming session, Duncan continues work on an item degradation system. The team implements a requirement that items degrade twice as fast after their sell-by date. To make the behavior testable, they introduce a `LocalDate` parameter to the `updateBy` method, allowing tests to specify the current date rather than relying on a clock. This change exposes the core logic and enables a new test case for post-sell-by-date degradation, starting at a quality of 43 and expecting a reduction to 42 after one day.

- Refactored tests to operate on a single item rather than a list, simplifying the test suite and focusing on the unit under test.
- Introduced a `LocalDate` parameter to the update method to make degradation behavior dependent on the current date explicit and testable.
- Implemented faster degradation by applying a reduction of 2 per day when the current date is after the sell-by date, while still reducing by 1 per day before that.
- Used a loop-based approach to repeatedly apply daily degradation, making the logic flexible and easy to adjust.