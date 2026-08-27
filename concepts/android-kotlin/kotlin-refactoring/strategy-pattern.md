---
domain: android-kotlin
subdomain: kotlin-refactoring
concept: strategy-pattern
title: Updating Stock with a Strategy Pattern in Kotlin
sources:
  - title: "Kotlin Concurrency - Para Exec llel ution"
    url: "https://www.youtube.com/watch?v=y4OqpW4EMDk"
    author: "Duncan"
    date: "2022-02-27T14:45:26+00:00"
---

# Updating Stock with a Strategy Pattern in Kotlin

Duncan from the Gilded Rose development team continues work on the stock class, leveraging earlier time-utility code to trigger updates based on how many days have passed since the stock was last modified. Existing tests load a stock list from file and check that the file is resaved with a new last modified time when the stock is outdated, but the actual update logic was missing. To make the testing clearer, they inline the stock list in the test code, and then they implement an update function that maps over items, reducing each item's quality by the number of days out of date (with a temporary conversion because quality is a UInt). (Duncan, 2022)

The team decides to pass the update behavior as a strategy into the Stock class rather than hard-coding it, keeping the Stock class focused on deciding when to update rather than how. The strategy is a function type `(List<Item>, Int) -> List<Item>`, named `updateItems`. The Stock class uses this function to copy the loaded list with updated items when it is days out of date. A second test is added to verify that two days out of date reduces quality by two, confirming the days parameter is properly propagated. (Duncan, 2022)

- Use a strategy function to decouple the update logic from the Stock class, making it easier to change behavior without modifying Stock.
- Inline test data to make test scenarios more readable and explicit.
- Be cautious when doing arithmetic with unsigned types (UInt) and convert to Int when necessary.
- Add targeted tests for multiple days to ensure the days-out-of-date value is correctly used.