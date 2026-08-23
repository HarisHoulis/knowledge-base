---
domain: android-kotlin
subdomain: test-driven-development
concept: degrading-items-tdd
title: Kotlin TDD - More Degrading
sources:
  - title: "Kotlin TDD - More Degrading"
    url: "https://www.youtube.com/watch?v=N_ArZ2yHEm8"
    author: "Pairing with Duncan"
    date: "2022-03-29T21:59:23+00:00"
---

# Kotlin TDD - More Degrading

In this session, Duncan and the team on Guilded Rose implement a new requirement: items degrade twice as fast after their sell-by date. Previously, items lost one quality per day before the sell-by date and one after; now they should lose two per day after the sell-by date. The work begins by refactoring existing tests to directly test the item update method rather than going through a list mapping, which simplifies the test structure and focuses on the core behavior.

- Refactored tests to call the item update method directly, removing unnecessary list mapping overhead.
- Introduced a LocalDate parameter to the update method so the current date is explicitly passed, avoiding reliance on system time.
- Implemented faster degradation by repeating daily updates, with a degradation amount of 2 after the sell-by date and 1 before.
- Used TDD by adding a failing test for the new behavior before updating the production code.