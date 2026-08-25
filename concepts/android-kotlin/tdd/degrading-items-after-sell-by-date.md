---
domain: android-kotlin
subdomain: tdd
concept: degrading-items-after-sell-by-date
title: Kotlin TDD - More Degrading
sources:
  - title: "Kotlin TDD - More Degrading"
    url: "https://www.youtube.com/watch?v=N_ArZ2yHEm8"
    author: "Pairing with Duncan"
    date: "2022-03-29T21:59:23+00:00"
---

# Kotlin TDD - More Degrading

In this TDD session, the team implements a new requirement where items degrade twice as fast after their sell-by date. They start by refactoring existing tests to directly exercise the Item class's updatedBy method, removing unnecessary list-wrapping and simplifying the test structure (Pairing with Duncan, 2022). This makes the tests clearer and focuses them on the core behavior.

- Refactor tests to target the item's update method directly, removing list indirection.
- Add a failing test for quality decreasing by 2 per day after the sell-by date.
- Introduce a LocalDate parameter to the update method to know the current date.
- Implement behavior by iterating over days and degrading quality by 1 or 2 based on whether the current date is past sell-by.