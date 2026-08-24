---
domain: android-kotlin
subdomain: test-driven-development
concept: incremental-degradation
title: Kotlin TDD - More Degrading
sources:
  - title: "Kotlin TDD - More Degrading"
    url: "https://www.youtube.com/watch?v=N_ArZ2yHEm8"
    author: "Pairing with Duncan"
    date: "2022-03-29"
---

# Kotlin TDD - More Degrading

In this session, Duncan and the team tackle a new requirement: items degrade twice as fast after their sell-by date. The existing implementation reduces quality by one per day regardless of sell-by date, and the team needs to adjust behavior to degrade by two after the date passes. They begin by refactoring tests to remove the list-wrapping method, simplifying the test code to directly call the item update logic, which makes the tests clearer and less coupled to the map operation.

- Refactor test code to focus on the core update method rather than list mapping.
- Introduce a clock/date parameter to the update function to make behavior time-dependent.
- Incremental degradation: apply the daily quality reduction repeatedly for each day, with a larger reduction after sell-by date.
- Use TDD: write a failing test for the new behavior before implementing the logic.