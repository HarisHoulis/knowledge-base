---
domain: android-kotlin
subdomain: higher-order-functions
concept: strategy-function
title: Kotlin Concurrency - Para Exec llel ution
sources:
  - title: "Kotlin Concurrency - Para Exec llel ution"
    url: "https://www.youtube.com/watch?v=y4OqpW4EMDk"
    author: "Duncan"
    date: "2022-02-27T14:45:26+00:00"
---

# Kotlin Concurrency - Para Exec llel ution

The session demonstrates a test-driven approach to implementing a stock update strategy in Kotlin. Initially, the stock loading test and a test verifying that a stock last modified yesterday triggers an update are shown, but the code only saves a new last modified time without altering item qualities (Duncan, 2022). To meet the requirement of decreasing each item's quality by one per day, the developer writes an `update(items, days)` function that maps over items and copies each with quality reduced by the number of days. A type issue arises because quality is `UInt`, and subtracting an `Int` is invalid, so a conversion is needed. This update function is then injected into the `Stock` class as a higher-order function parameter, allowing the stock class to focus on determining when to update rather than how to update (Duncan, 2022).

Tests are improved by inlining stock list data for better visibility and moving test stock to its own file to avoid accidental use in production. A second test is added for a stock two days out of date, expecting qualities reduced by two, which validates that the days argument is correctly passed through. The session highlights practical Kotlin patterns such as passing functions as parameters and the importance of explicit multi-day test cases (Duncan, 2022).

- Use higher-order functions to inject update strategies, separating the decision of when to update from the logic of how to update.
- Inline test data to improve readability and move shared test fixtures to separate files to keep production code clean.
- Be cautious with unsigned types like `UInt`; subtracting an `Int` requires a conversion or a different type design.
- Write tests for multiple days out-of-date to ensure the days parameter is correctly propagated and applied.