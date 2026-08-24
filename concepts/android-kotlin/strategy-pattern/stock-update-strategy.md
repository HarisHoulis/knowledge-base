---
domain: android-kotlin
subdomain: strategy-pattern
concept: stock-update-strategy
title: Kotlin Concurrency - Parallel Execution
sources:
  - title: "Kotlin Concurrency - Para Exec llel ution"
    url: "https://www.youtube.com/watch?v=y4OqpW4EMDk"
    author: "Duncan"
    date: "2022-02-27T14:45:26+00:00"
---

# Kotlin Concurrency - Parallel Execution

In this session, Duncan works on a stock management system where the requirement is to reduce the quality of each item by one every day. He refactors the existing test to make the stock list explicit, then introduces a function that updates items by mapping over them and subtracting the number of days from their quality. Since quality is stored as a uint, he notes a potential issue with subtraction and temporarily converts to int. He then decides to inject this update logic as a strategy into the Stock class, allowing the class to focus on deciding whether an update is needed while delegating the actual update behavior. The strategy is passed as a function parameter, and the stock class applies it to the items when the last modified date is out of date. He also adds a second test to verify that an item updated two days ago gets its quality reduced by two, confirming the function uses the correct number of days. The session highlights the use of higher-order functions and test-driven development in Kotlin, as well as a careful approach to numeric types.

- Use a strategy function parameter to decouple the decision to update from the update logic.
- Implement item updates by mapping over the list and copying items with modified quality.
- Write tests for different numbers of days to verify the update strategy uses the correct day count.
- Be mindful of numeric types like uint when performing arithmetic operations in Kotlin.