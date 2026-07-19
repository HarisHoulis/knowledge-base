---
domain: android-kotlin
subdomain: functional-programming
concept: removing-mutability
title: Java to Kotlin Gilded Rose - Part 3 Refactoring to Functions
sources:
  - title: "Java to Kotlin Gilded Rose - Part 3 Refactoring to Functions"
    url: "https://www.youtube.com/watch?v=y5ovdC3Wsko"
    author: "Pairing with Duncan"
    date: "2021-10-20T12:19:49+00:00"
---

# Java to Kotlin Gilded Rose - Part 3 Refactoring to Functions

In this video, the presenter continues refactoring the Gilded Rose code from Java to Kotlin, moving from an object-oriented to a functional solution. The main obstacle is the mutability of the Item class (sellIn and quality fields). To remove mutability, they create a new method `updated()` that returns a new Item with the updated values instead of modifying the original. This pushes mutation outward: in the `updateQuality` method, they replace the mutable `items` list with a mapped version using `items.map { it.updated() }`, which returns a new immutable list. The test initially fails because the test iterates over the original list passed to GildedRose, not the new list; fixing this by iterating over `app.items` resolves it. With Item now immutable, it can be made a data class, enabling easy copying via `copy()`. The refactoring demonstrates a common strategy of pushing mutability to the boundaries of the system (entry points) and using immutable data structures for the core logic.

- To remove mutability, create a method that returns a new copy of the object with updated values rather than mutating in place.
- Push mutability outward by replacing mutable collections with mapped immutable ones at the entry point.
- When replacing a mutable list, ensure all references are updated (e.g., iterating over the new list, not the old one).
- After removing mutability, the class can be refactored to a data class, leveraging `copy()` for easy creation of modified instances.