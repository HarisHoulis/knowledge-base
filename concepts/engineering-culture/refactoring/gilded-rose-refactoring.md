---
domain: engineering-culture
subdomain: refactoring
concept: gilded-rose-refactoring
title: Gilded Rose Refactoring in Kotlin
sources:
  - title: "Tidy First Gilded Rose Refactoring in Kotlin"
    url: "https://www.youtube.com/watch?v=5-PNIKc1clQ"
    author: "Pairing with Duncan"
    date: "2021-10-21"
---

# Gilded Rose Refactoring in Kotlin

The video presents a refactoring session on the Gilded Rose kata in Kotlin, following a stricter interpretation of the constraints: no changes to the Item class and no subclassing. The author decides to work entirely within the GildedRose class, using the existing 10-day test as sufficient coverage for refactoring, arguing that additional tests wouldn't have changed the final design since it's refactoring-driven [source]. 

The refactoring starts by converting to Kotlin, then extracting helper methods like isBrie, isBackstagePasses, and isSulfuras to reduce duplication. Conditions are inverted to improve readability, and methods are moved to static scope to ensure no hidden state. The author then explores creating an ItemType enum to categorize item behavior, while still not modifying Item itself. 

Key takeaways include the importance of having a safety net of tests, the ability to refactor procedural code into more expressive helpers, and the trade-offs of different interpretations of kata constraints.

- The existing 10-day fixture test provides sufficient coverage for refactoring, without necessarily guiding the final design.
- Avoid subclassing Item; instead, refactor within the GildedRose class using procedural techniques.
- Extract boolean helper methods like isBrie to reduce duplication and make item type checks clearer.
- Invert negative conditions to improve code readability and simplify control flow.
- Consider introducing an ItemType enum to centralize item behavior, while preserving the original Item class.