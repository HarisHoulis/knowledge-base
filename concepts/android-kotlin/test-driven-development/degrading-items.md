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

In this Kotlin TDD session, the team implements a new requirement: items degrade twice as quickly after their sell-by date. Previously, item quality decreased by one per day; now, once past the sell-by date, quality should decrease by two each day. The video starts by refactoring existing tests to call the Item.updatedBy method directly, removing the indirection of a list-updating helper (Pairing with Duncan, 2022).

To make the behavior depend on whether the item is past its sell-by date, the updatedBy method is given a LocalDate parameter representing the current date. This allows tests to set an explicit date without requiring a clock. The production caller temporarily passes the item's sellByDate to keep the code compiling while the tests are updated (Pairing with Duncan, 2022).

The implementation is changed from a single subtraction to a repeated daily degradation loop. A degradation factor is chosen based on whether the provided date is after the sell-by date: 2 if after, 1 otherwise. This satisfies the new failing test while keeping existing tests green (Pairing with Duncan, 2022).

- Simplify tests by testing Item.updatedBy directly rather than through list-level update code.
- Add a LocalDate parameter to updatedBy to make degradation rate depend on the current date.
- Use a repeat loop to apply daily degradation instead of computing total quality in one subtraction.
- Set degradation factor to 2 after the sell-by date and 1 before it.