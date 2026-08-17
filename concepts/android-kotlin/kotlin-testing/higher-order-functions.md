---
domain: android-kotlin
subdomain: kotlin-testing
concept: higher-order-functions
title: Updating Stock with Strategy in Kotlin
sources:
  - title: "Kotlin Concurrency - Para Exec llel ution"
    url: "https://www.youtube.com/watch?v=y4OqpW4EMDk"
    author: "Pairing with Duncan"
    date: "2022-02-27T14:45:26+00:00"
---

# Updating Stock with Strategy in Kotlin

The video demonstrates a test-driven approach to updating a stock list in Kotlin. The initial tests only verify loading and checking if stock is outdated, but the update logic itself is missing. The author introduces a function to update items by reducing quality by one per day, using `map` to copy each item with adjusted quality. To keep the stock class focused on determining whether an update is needed, the update logic is passed in as a function parameter (strategy). The code handles type conversions from UInt to Int for subtraction, and adds a test for two-day updates to verify the correct number of days is applied.

- Use `map` to transform each item by copying it with updated quality.
- Pass the update logic as a function parameter to decouple stock management from item updating.
- Convert UInt to Int when subtracting days to avoid type errors.
- Inline test data for readability and write multiple tests to verify correct day counts.