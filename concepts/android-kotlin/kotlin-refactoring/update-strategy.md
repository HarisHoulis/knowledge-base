---
domain: android-kotlin
subdomain: kotlin-refactoring
concept: update-strategy
title: Kotlin Concurrency - Para Exec llel ution
sources:
  - title: "Kotlin Concurrency - Para Exec llel ution"
    url: "https://www.youtube.com/watch?v=y4OqpW4EMDk"
    author: "Pairing with Duncan"
    date: "2022-02-27T14:45:26+00:00"
---

# Kotlin Concurrency - Para Exec llel ution

This video covers a refactoring session on a Kotlin stock management system. The existing code only updates the last modified timestamp but does not adjust item quality. To address the requirement of reducing item quality by one per day, the presenter first improves test readability by inlining the stock list. They then implement an `update` function that maps over items, copying each with quality reduced by the number of days, and integrate it as a strategy passed into the Stock class. A challenge with unsigned integers is handled by converting to int. Tests verify the strategy works for one and two days out of date, confirming the day-based reduction is correctly applied.

- The initial code only saves a new last-modified time without updating item quality.
- Tests are refactored to inline the stock list for better visibility.
- An update function maps items to new items with quality reduced by days, requiring conversion from unsigned to int.
- The update logic is passed as a function type (strategy) into the Stock class.
- Additional tests confirm behavior for multiple days out of date.