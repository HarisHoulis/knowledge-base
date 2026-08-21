---
domain: android-kotlin
subdomain: design-patterns
concept: strategy-pattern
title: Refactoring Stock Update with Strategy Pattern in Kotlin
sources:
  - title: "Kotlin Concurrency - Para Exec llel ution"
    url: "https://www.youtube.com/watch?v=y4OqpW4EMDk"
    author: "Pairing with Duncan"
    date: "2022-02-27T14:45:26+00:00"
---

# Refactoring Stock Update with Strategy Pattern in Kotlin

The video transcript follows a test-driven refactoring of a stock update system in Kotlin. Initially, the stock class has a method that checks if the stock is days out of date, but it does not actually update the items. The authors inline the stock list in tests to make the data explicit, then introduce an `update` function that maps over items and reduces each item's quality by the number of days (source). Since `quality` is a `uint`, they convert it to an `int` to allow subtraction (source). They then refactor the update function to be a strategy passed into the stock class constructor, decoupling the decision of whether to update from the logic of how to update (source). Tests are added for one and two days out of date, confirming the number of days is applied correctly (source).

- Implemented stock update logic with a function that maps items to reduce quality by days.
- Used strategy pattern by passing an update function into the stock class.
- Converted unsigned quality to int to allow subtraction.
- Added tests for one and two days out of date to verify the number of days applied.