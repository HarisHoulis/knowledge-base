---
domain: android-kotlin
subdomain: kotlin-testing
concept: strategy-pattern
title: Kotlin Concurrency - Para Exec llel ution
sources:
  - title: "Kotlin Concurrency - Para Exec llel ution"
    url: "https://www.youtube.com/watch?v=y4OqpW4EMDk"
    author: "Pairing with Duncan"
    date: "2022-02-27T14:45:26+00:00"
---

# Kotlin Concurrency - Para Exec llel ution

This video covers implementing a stock update feature in Kotlin. The author writes tests to drive the implementation, inlining test data for clarity, and introduces a function parameter to the Stock class to act as a strategy for updating items. The update function reduces each item's quality by one per day, and the code handles type conversions between UInt, Long, and Int. The strategy pattern decouples the update logic from the stock management logic, allowing flexible updates based on the number of days since last modification.

- Write failing tests first to guide implementation.
- Inline test data to make tests more readable and self-contained.
- Pass a function as a strategy to decouple update logic from the Stock class.
- Handle type mismatches (UInt, Long) when performing arithmetic operations.
- Verify update behavior for different numbers of days.