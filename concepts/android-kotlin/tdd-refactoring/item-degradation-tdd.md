---
domain: android-kotlin
subdomain: tdd-refactoring
concept: item-degradation-tdd
title: Kotlin TDD - More Degrading
sources:
  - title: "Kotlin TDD - More Degrading"
    url: "https://www.youtube.com/watch?v=N_ArZ2yHEm8"
    author: "Pairing with Duncan"
    date: "2022-03-29T21:59:23+00:00"
---

# Kotlin TDD - More Degrading

The video demonstrates a Test-Driven Development (TDD) session implementing a new requirement for an item degradation system: after the sell-by date, item quality should decrease by two per day instead of one. The developers begin by refactoring existing tests to directly test the `updatedBy` method, removing the list wrapper that previously made tests longer and more complicated. This simplifies the test suite and focuses verification on the core logic.

- Refactoring tests to directly test the core method improves clarity and reduces unnecessary complexity.
- Injecting the current date as a parameter keeps tests deterministic and avoids relying on system time.
- Following TDD, a failing test for the new behavior is written first, then minimal production code is added to satisfy it.
- The implementation loops over each day and applies a daily degradation, using a factor of 2 when the date is past sell-by, otherwise 1.