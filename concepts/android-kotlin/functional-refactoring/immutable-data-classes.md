---
domain: android-kotlin
subdomain: functional-refactoring
concept: immutable-data-classes
title: Java to Kotlin Gilded Rose - Part 3 Refactoring to Functions
sources:
  - title: "Java to Kotlin Gilded Rose - Part 3 Refactoring to Functions"
    url: "https://www.youtube.com/watch?v=y5ovdC3Wsko"
    author: "Pairing with Duncan"
    date: "2021-10-20T12:19:49+00:00"
---

# Java to Kotlin Gilded Rose - Part 3 Refactoring to Functions

The transcript describes refactoring the Gilded Rose kata from a procedural Java style to a functional Kotlin style. The primary obstacle is the mutability of the Item class, specifically its sellIn and quality fields. To eliminate this, the author introduces an `updated` method that returns a new Item instance with the aged and degraded values, rather than mutating the existing object. This effectively pushes mutation outward: the `updateQuality` method now replaces the items list with a mapped list of updated items, moving the side effect one level up from the data model to the service layer [1].

This change initially breaks the tests because the test fixture iterates over the original items array passed into the GildedRose constructor, rather than the current `items` property. After updating the test to iterate over `app.items`, all tests pass. The old mutating `update` method is then removed, the fields are changed to `val`, and Item is converted to a data class. This enables convenient use of the `copy` method for creating modified versions, bringing the code closer to a functional style where data is immutable and transformations return new instances [1].

- Replace mutating methods with functions that return new instances, pushing mutation to the outer layers.
- When replacing the items list, ensure tests (and consumers) read the current property, not the original reference.
- Making Item a data class with immutable `val` properties allows concise `copy` usage for transformations.
- The refactoring moves from procedural, to OOP, to functional style by systematically removing mutability.