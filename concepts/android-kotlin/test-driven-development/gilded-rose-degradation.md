---
domain: android-kotlin
subdomain: test-driven-development
concept: gilded-rose-degradation
title: Kotlin TDD - More Degrading
sources:
  - title: "Kotlin TDD - More Degrading"
    url: "https://www.youtube.com/watch?v=N_ArZ2yHEm8"
    author: "Pairing with Duncan"
    date: "2022-03-29T21:59:23+00:00"
---

# Kotlin TDD - More Degrading

Pairing with Duncan continues the Gilded Rose kata in Kotlin using TDD. The team refactors existing tests to operate on a single item rather than a list, simplifying the test suite by removing an unnecessary mapping layer. They then address a new requirement: items degrade twice as fast after their sell-by date. To make time-dependent behavior testable without depending on a system clock, they add an explicit `on: LocalDate` parameter to the `updateBy` method. A failing test drives the implementation, which uses a loop to apply daily degradation, choosing a degradation rate of 1 or 2 depending on whether the date is after the sell-by date. The session demonstrates incremental refactoring and test-driven design.

- Refactored tests to exercise `updateBy` directly, removing list indirection and simplifying assertions.
- Introduced a `LocalDate` parameter to make the current date explicit, enabling deterministic tests for time-based behavior.
- Implemented degradation as repeated daily updates, with a rate of 2 after sell-by date and 1 before it.
- Followed TDD: added a failing test for the new requirement, then made the minimal code change to pass.