---
domain: engineering-culture
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

In this session, the team continues a Test-Driven Development (TDD) kata in Kotlin, working on the Gilded Rose problem. The requirement is to make items degrade twice as fast after their sell-by date: previously items degraded by 1 per day, but after the sell-by date they should degrade by 2 every day. The existing code had an `Item` class with an `updateBy(days)` method that reduced quality by the number of days, capping at zero. The tests were written against a list-level method that mapped `updateBy` over an entire list, making them longer and more complicated than necessary. The developer refactors the tests to directly target `Item.updateBy`, removing the list wrapper and simplifying the test setup (Duncan, 2022).

- Refactor tests to focus on the unit under test, avoiding unnecessary list-level abstractions.
- Introduce a `LocalDate` parameter to `updateBy` to model the current date, enabling time-dependent behavior without injecting a clock.
- Write a failing test first that asserts quality drops by 2 after the sell-by date.
- Implement the logic by looping over each day and applying a degradation rate that depends on whether the current date is after the sell-by date.
- Keep production code compiling during refactoring by passing a placeholder date (the sell-by date) where needed.