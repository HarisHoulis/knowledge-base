---
domain: android-kotlin
subdomain: tdd
concept: degrading-items
title: Kotlin TDD - More Degrading
sources:
  - title: "Kotlin TDD - More Degrading"
    url: "https://www.youtube.com/watch?v=N_ArZ2yHEm8"
    author: "Pairing with Duncan"
    date: "2022-03-29T21:59:23+00:00"
---

# Kotlin TDD - More Degrading

The session continues work on an item degradation system in Kotlin. The presenter refactors existing tests to remove unnecessary list wrapping, directly testing the item's update method. This simplifies the test suite and prepares for adding new behavior: items degrade twice as fast after their sell-by date. (source: Pairing with Duncan, 2022-03-29, https://www.youtube.com/watch?v=N_ArZ2yHEm8)

To handle the 'after sell-by date' condition, a LocalDate parameter is introduced to the update method, allowing tests to specify the current date. This seems more sensible than injecting a clock into the item. The production code initially passes the item's own sell-by date to keep compiling. The implementation then models daily updates by repeating a step that reduces quality, with the degradation rate set to 2 if the current date is after sell-by, otherwise 1. This satisfies the new test and preserves existing behavior. (source: Pairing with Duncan, 2022-03-29, https://www.youtube.com/watch?v=N_ArZ2yHEm8)

- Refactored tests to call item.updateBy directly, removing list-based indirection that bloated tests.
- Added a LocalDate parameter to updateBy so the method can determine whether the sell-by date has passed.
- Implemented faster degradation after sell-by date by repeating daily updates, using a degradation rate of 2 after sell-by and 1 before.
- Kept production code compiling by passing the item's sellBy date as a temporary argument, to be revisited later.