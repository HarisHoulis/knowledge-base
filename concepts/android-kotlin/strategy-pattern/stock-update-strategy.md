---
domain: android-kotlin
subdomain: strategy-pattern
concept: stock-update-strategy
title: Refactoring Stock Update with Strategy Pattern
sources:
  - title: "Kotlin Concurrency - Para Exec llel ution"
    url: "https://www.youtube.com/watch?v=y4OqpW4EMDk"
    author: "Pairing with Duncan"
    date: "2022-02-27T14:45:26+00:00"
---

# Refactoring Stock Update with Strategy Pattern

The session focuses on updating a stock management system in Kotlin. Initially, the code only updates the last-modified timestamp when the stock is old, but does not modify the quality of items. The developers refactor the tests to inline the stock list for clarity and then write a new function that maps over items, reducing quality by the number of days since last update, while noting a UInt subtraction issue that requires conversion to Int. They then introduce a strategy parameter to the Stock class, allowing the caller to supply an `updateItems` function with type `(List<Item>, Int) -> List<Item>`, which is used to apply the quality reduction when the stock is out of date. An additional test verifies that updating by two days reduces quality by two, ensuring the correct number of days is passed. The approach separates the decision of when to update from the strategy of how to update, improving flexibility and testability.

- The initial implementation only refreshed the last-modified timestamp without updating item quality.
- A new update function uses `items.map` to reduce each item's quality by the number of days, but requires converting UInt to Int for subtraction.
- The update logic is injected as a strategy into the Stock class, parameterized as a function type.
- Tests are refactored to inline expected data and include cases for one and two days to ensure correct day-count handling.