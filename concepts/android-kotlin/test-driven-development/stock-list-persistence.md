---
domain: android-kotlin
subdomain: test-driven-development
concept: stock-list-persistence
title: Kotlin TDD - StockList
sources:
  - title: "Kotlin TDD - StockList"
    url: "https://www.youtube.com/watch?v=RXFJiJAhvZk"
    author: "Pairing with Duncan"
    date: "2021-12-14T21:30:37+00:00"
---

# Kotlin TDD - StockList

The video continues implementing a Gilded Rose stock control system in Kotlin using test-driven development. The current system loads items from a tab-separated file but does not track when the stock was last updated. Since the next story requires reducing each item's quality by one per day, the system needs to know the last update time. To address this, the author introduces a `StockList` data class containing a list of items and a `lastModified` timestamp of type `Instant` [1]. Initially, to keep existing tests passing, `StockList` implements `List<Item>` by delegating to its internal item list [1]. The first attempt to return a `StockList` from `loadItems` causes tests to fail because of the subtle difference between two `Instant.now()` calls made milliseconds apart, so the author introduces a configurable default `lastModified` parameter, allowing tests to inject a fixed time [1]. 

The author then plans to extend the save/load functions to write and read the `lastModified` date from the file itself. They rename the existing save/load methods to `saveLegacy`/`loadLegacy` to preserve behavior for files that do not contain a timestamp, and start adding a new version that handles the timestamp [1]. The approach highlights common TDD practices: using data classes to model domain concepts, leveraging Kotlin delegation to maintain API compatibility, and making time injectable for deterministic tests [1].

- A StockList data class wraps a list of items and a lastModified Instant to track when stock was updated.
- Implementing List<Item> via delegation allows StockList to replace List<Item> without breaking the rest of the app.
- TDD test failures revealed that using Instant.now() directly makes tests flaky; injecting a fixed time via a default parameter solves this.
- The next step is to persist lastModified in the file, with legacy load/save methods kept for backward compatibility.