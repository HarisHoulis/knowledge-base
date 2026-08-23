---
domain: android-kotlin
subdomain: testing-and-design
concept: strategy-pattern-with-function-parameters
title: Kotlin Concurrency - Parallel Execution
sources:
  - title: "Kotlin Concurrency - Para Exec llel ution"
    url: "https://www.youtube.com/watch?v=y4OqpW4EMDk"
    author: "Pairing with Duncan"
    date: "2022-02-27T14:45:26+00:00"
---

# Kotlin Concurrency - Parallel Execution

In this episode, Duncan and his pair refactor a stock update system in Kotlin. The goal is to reduce item quality by one each day. They start by inlining test data to improve readability, then create an `update` function that takes a list of items and a number of days, mapping each item to a copy with reduced quality. Since quality is a `uint`, they temporarily convert to `int` to allow subtraction, noting this as a design mistake to revisit. They then pass this update function as a strategy into the `Stock` class, avoiding hardcoding the update logic and keeping the class focused on determining when to update. The strategy is passed as a function argument, with parameters named for clarity. They also adjust the days calculation from `long` to `int` for convenience. Tests include one-day and two-day updates to verify correct behavior. The work is done incrementally with the new stock list kept in tests until finalized.

- Inline test data to see what you're testing; avoid unnecessary constructor copies.
- Use a function parameter (strategy pattern) to decouple update logic from the stock class.
- Be cautious with type choices: `uint` can't subtract `int`, so convert or redesign.
- Write tests for multiple scenarios (e.g., 1 day, 2 days) to validate logic.