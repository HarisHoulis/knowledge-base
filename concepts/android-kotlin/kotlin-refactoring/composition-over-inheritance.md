---
domain: android-kotlin
subdomain: kotlin-refactoring
concept: composition-over-inheritance
title: Java to Kotlin Gilded Rose - Part 2: Refactoring to Composition
sources:
  - title: "Java to Kotlin Gilded Rose - Part 2 Refactoring to Composition"
    url: "https://www.youtube.com/watch?v=ajl3dpNTdM0"
    author: "Duncan"
    date: "2021-10-19T21:14:32+00:00"
---

# Java to Kotlin Gilded Rose - Part 2: Refactoring to Composition

The video continues the Java-to-Kotlin refactoring of the Gilded Rose kata, focusing on making the Item hierarchy more expressive and moving toward composition. After prior steps, the update logic is now in an Item base class with subclasses overriding specific behaviors (template method). In this part, Duncan examines protected methods like age() and degrade() which mutate state directly, making it hard to see what subclasses do. He refactors age() into a property 'aging' representing the amount to reduce sellIn, so the base class controls the meaning of aging while subclasses merely supply a numeric amount (Duncan, 2021).

- Replace mutating helper methods with value-returning functions to make base behavior explicit.
- Extract quantities like 'aging' as properties to separate what from how.
- Use test-driven refactoring with small steps and commits.
- Move toward composition by allowing subclasses to supply behavior parameters.