---
domain: android-kotlin
subdomain: functional-programming
concept: strategy-pattern
title: Kotlin Concurrency - Parallel Execution
sources:
  - title: "Kotlin Concurrency - Parallel Execution"
    url: "https://www.youtube.com/watch?v=y4OqpW4EMDk"
    author: "Pairing with Duncan"
    date: "2022-02-27T14:45:26+00:00"
---

# Kotlin Concurrency - Parallel Execution

In this episode, Duncan continues work on a stock class by implementing a strategy for updating item quality. He refactors tests to inline the stock list for clarity and writes a function that maps over items, reducing each item's quality by the number of days out of date. A type issue arises because quality is a uint and the days value is an int, so he temporarily converts it, noting this as a potential design mistake. ([source](https://www.youtube.com/watch?v=y4OqpW4EMDk))

To decouple the decision of *whether* to update from *how* to update, Duncan passes an `updateItems` function as a parameter to the stock class. This function type takes the items and days, returning a new list of items. The stock class then copies the loaded stock with the new last-modified date and applies the update function to its items when they are out of date. This strategy-pattern approach keeps the stock class focused on checking staleness while delegating the actual update logic. ([source](https://www.youtube.com/watch?v=y4OqpW4EMDk))

Finally, the developer verifies the solution with tests, including a scenario where the stock is two days out of date, expecting qualities reduced by two. The implementation passes the tests, showing that the strategy works for different day offsets. ([source](https://www.youtube.com/watch?v=y4OqpW4EMDk))

- Use a strategy function to separate the update algorithm from the stock's staleness check.
- Leverage Kotlin's `map` and data class copy to functionally update items.
- Be cautious with numeric types: converting between `uint` and `Int` can be a code smell.
- Write tests for both one-day and multi-day updates to verify the logic.