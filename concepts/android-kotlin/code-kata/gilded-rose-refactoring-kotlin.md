---
domain: android-kotlin
subdomain: code-kata
concept: gilded-rose-refactoring-kotlin
title: Tidy First Gilded Rose Refactoring in Kotlin
sources:
  - title: "Tidy First Gilded Rose Refactoring in Kotlin"
    url: "https://www.youtube.com/watch?v=5-PNIKc1clQ"
    author: "Pairing with Duncan"
    date: "2021-10-21"
---

# Tidy First Gilded Rose Refactoring in Kotlin

In this video, the speaker continues exploring the Gilded Rose refactoring kata in Kotlin, this time imposing the constraint of not subclassing the Item class or changing its properties. Starting from an existing test suite that runs over 10 days, the refactoring proceeds entirely within the GildedRose class by first converting the loop to a for-each and extracting the update logic into a method called `updateSplendid`. The speaker then inverts conditionals to simplify logic and extracts three helper functions: `isBrie`, `isPasses`, and `isSulfurous` (spelled 'fierce' in the transcript). These functions are pulled into static scope, demonstrating that the refactoring does not rely on any state in GildedRose (source: transcript).

- The refactoring avoids creating new subtypes of Item, working only in the GildedRose class.
- The approach uses procedural decomposition: extracting methods and inverting conditionals to reduce duplication.
- Three item-type detection functions (isBrie, isPasses, isSulfurous) are extracted as static methods.
- The final design introduces a new class (likely an enum) for item types, moving toward a more object-oriented structure without altering Item.
- The test suite (10 days of coverage) is deemed sufficient for guiding the refactoring; adding unit tests is considered unnecessary for the design goal.