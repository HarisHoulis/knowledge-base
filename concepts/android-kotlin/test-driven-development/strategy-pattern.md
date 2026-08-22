---
domain: android-kotlin
subdomain: test-driven-development
concept: strategy-pattern
title: Refactoring Stock Update Strategy with Tests
sources:
  - title: "Kotlin Concurrency - Para Exec llel ution"
    url: "https://www.youtube.com/watch?v=y4OqpW4EMDk"
    author: "Pairing with Duncan"
    date: "2022-02-27T14:45:26+00:00"
---

# Refactoring Stock Update Strategy with Tests

In this coding session, Duncan continues work on a stock management system by refining the logic that updates item quality. The existing test verifies that when a stock list is loaded and its last modified date is old, the list is resaved with a new timestamp. However, the actual update behavior—reducing each item's quality by one per day—has not yet been implemented. To make the code clearer, Duncan inlines the stock list and expected result directly into the test, making it obvious what data is being used.

- Inline test data to improve readability and reveal what is being tested.
- Encapsulate update logic as a strategy (a function passed into the stock class) to separate concerns.
- Use test-driven development: write a failing test before implementing behavior.
- Handle type mismatches (e.g., subtracting an Int from a UInt) by converting explicitly.