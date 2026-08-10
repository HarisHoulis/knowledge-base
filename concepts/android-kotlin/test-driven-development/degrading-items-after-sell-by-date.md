---
domain: android-kotlin
subdomain: test-driven-development
concept: degrading-items-after-sell-by-date
title: Kotlin TDD - More Degrading
sources:
  - title: "Kotlin TDD - More Degrading"
    url: "https://www.youtube.com/watch?v=N_ArZ2yHEm8"
    author: "Pairing with Duncan"
    date: "2022-03-29T21:59:23+00:00"
---

# Kotlin TDD - More Degrading

In this TDD session, the team implements a requirement that items degrade quality twice as fast after their sell-by date. They begin by refactoring existing tests that operate on lists of items to test a single item directly, simplifying the test suite and removing unnecessary complexity. This refactor aligns with the principle of testing behavior rather than implementation details, as the list mapping is already covered indirectly (Pairing with Duncan, 2022).

Next, they introduce a failing test for the new behavior: an item past its sell-by date should lose two quality points per day. To make the function testable without relying on the current time, they add a `LocalDate` parameter to the update method, defaulting to the item's sell-by date in production code. This makes the function deterministic and allows tests to control the date explicitly. They then implement the logic by iterating over each day and conditionally degrading by either one or two points depending on whether the current day is past the sell-by date. The change is minimal and passes all tests, demonstrating a straightforward TDD cycle of refactor, write failing test, implement, and verify (Pairing with Duncan, 2022).

- Refactor tests to operate on single items rather than lists to reduce complexity and focus on behavior.
- Introduce a clock/date parameter to make functions deterministic and testable without global state.
- Write a failing test first to drive the implementation of the new degradation rule.
- Implement the rule by repeating daily degradation and choosing the degradation rate based on whether the item is past its sell-by date.