---
domain: android-kotlin
subdomain: kotlin-patterns
concept: strategy-pattern-update
title: Updating Stock Items with Strategy Pattern in Kotlin
sources:
  - title: "Kotlin Concurrency - Para Exec llel ution"
    url: "https://www.youtube.com/watch?v=y4OqpW4EMDk"
    author: "Duncan"
    date: "2022-02-27"
---

# Updating Stock Items with Strategy Pattern in Kotlin

The video segment focuses on implementing a stock update feature in Kotlin. The current stock class loads from a file and checks if it's out of date by comparing last modified time to now. If the file is outdated, it saves a new last modified time but does not yet update the item qualities. The goal is to reduce the quality of each item by one per day. (Source: Duncan, 2022)

To implement this, they define a function that maps over items and copies each item with a quality reduced by the number of days. Because quality is a uint and days is an int, they convert as needed. They then pass this update logic into the stock class as a strategy, using a function type. This keeps the stock class responsible for deciding when to update, while delegating how to update to the strategy. (Source: Duncan, 2022)

Tests are written inline initially to make the stock list visible. They test updating by one day (quality 41 and 100) and by two days (quality 40 and 99). They move the stock class to its own file under tests to avoid using production code prematurely. The strategy pattern allows flexible updates and easier testing. (Source: Duncan, 2022)

- Update logic is passed as a strategy into the stock class, separating 'when to update' from 'how to update'.
- Quality is stored as uint, requiring conversion to int to compute reductions.
- Tests verify that quality decreases by one per day; two days result in double the reduction.
- The stock class copies the loaded data with a new last modified time and applies the update strategy to items.