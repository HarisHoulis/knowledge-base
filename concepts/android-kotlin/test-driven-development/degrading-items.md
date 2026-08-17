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

In this session, the team works on a new requirement where items degrade twice as fast after their sell-by date. Previously, items decreased in quality by one per day; now, after the sell-by date, they must decrease by two per day. The team begins by refactoring existing tests to remove the list-level abstraction, testing the Item.updateBy method directly, which makes the test code simpler and more focused (Pairing with Duncan, 2022).

- Refactored tests to call Item.updateBy directly instead of mapping over a list, simplifying test setup.
- Introduced a LocalDate parameter to updateBy to explicitly pass the current date, avoiding reliance on the system clock and making time-dependent behavior testable.
- Refactored the update logic to loop over each day, applying a degradation rate of 2 when the item is past its sell-by date, otherwise 1.
- Followed a red-green-refactor TDD cycle: added a failing test for the new behavior, then implemented the minimal change to pass.