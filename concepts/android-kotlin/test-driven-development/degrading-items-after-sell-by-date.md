---
domain: android-kotlin
subdomain: test-driven-development
concept: degrading-items-after-sell-by-date
title: Kotlin TDD: More Degrading
sources:
  - title: "Kotlin TDD - More Degrading"
    url: "https://www.youtube.com/watch?v=N_ArZ2yHEm8"
    author: "Pairing with Duncan"
    date: "2022-03-29"
---

# Kotlin TDD: More Degrading

In this Kotlin TDD session, Duncan and the Guilded Rose team refactor their existing tests for item quality degradation. They remove the list-based test wrapper to directly test the item's update method, avoiding unnecessary testing of the map function (source). This sets the stage for the new requirement: items should degrade twice as fast after their sell-by date.

They add a failing test for the new behavior, which requires knowing when the update is being called. To support this, the update method now takes a LocalDate parameter. In production code, they temporarily pass the item's sellByDate to keep everything compiling while they implement the logic (source). The implementation uses a loop over the number of days, reducing quality by 1 each day normally, but by 2 if the date is after the sell-by date (source).

- Refactor tests to focus on the item's update method instead of the list wrapper.
- Introduce a LocalDate parameter to the update method to know when the update is happening.
- Add a failing test for degrading quality by 2 after the sell-by date.
- Implement daily degradation with a rate of 2 when after sell-by date, 1 otherwise.
- Keep production code compiling by temporarily passing the item's sell-by date as the current date.