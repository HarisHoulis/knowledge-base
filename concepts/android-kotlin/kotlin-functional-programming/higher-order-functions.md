---
domain: android-kotlin
subdomain: kotlin-functional-programming
concept: higher-order-functions
title: Kotlin Concurrency: Updating Stock with Higher-Order Functions
sources:
  - title: "Kotlin Concurrency - Para Exec llel ution"
    url: "https://www.youtube.com/watch?v=y4OqpW4EMDk"
    author: "Pairing with Duncan"
    date: "2022-02-27T14:45:26+00:00"
---

# Kotlin Concurrency: Updating Stock with Higher-Order Functions

In this session, the team works on a stock management class in Kotlin, focusing on updating item quality based on the number of days since the stock was last modified. They write tests to verify that quality decreases by one per day, inlining test data for clarity and moving the stock list into a separate test file to avoid production code changes prematurely (source: https://www.youtube.com/watch?v=y4OqpW4EMDk).

To keep the stock class focused on whether an update is needed rather than how to update, they introduce a higher-order function as a strategy. The function takes a list of items and a number of days, mapping each item to a copy with quality reduced by days. They pass this function into the stock class, using named parameters in the function type to improve readability. The implementation handles type conversions carefully (e.g., from UInt to Int) to avoid compilation issues (source: https://www.youtube.com/watch?v=y4OqpW4EMDk).

The session also emphasizes writing comprehensive tests, including verifying updates over multiple days, and the importance of making code changes incrementally with tests as a safety net. The result is a clean separation of concerns, allowing the update strategy to be easily replaced or extended in the future (source: https://www.youtube.com/watch?v=y4OqpW4EMDk).

- Use higher-order functions to inject behavior, enabling a strategy pattern in Kotlin.
- Name function type parameters (e.g., items, days) for better code clarity.
- Be mindful of type constraints (UInt vs Int) when performing arithmetic operations.
- Inline test data and move it to test files to improve readability and avoid premature production changes.
- Write tests for multiple day offsets to ensure correctness of logic.