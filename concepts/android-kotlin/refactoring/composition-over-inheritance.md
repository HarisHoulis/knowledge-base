---
domain: android-kotlin
subdomain: refactoring
concept: composition-over-inheritance
title: Java to Kotlin Gilded Rose - Part 2 Refactoring to Composition
sources:
  - title: "Java to Kotlin Gilded Rose - Part 2 Refactoring to Composition"
    url: "https://www.youtube.com/watch?v=ajl3dpNTdM0"
    author: "Pairing with Duncan"
    date: "2021-10-19T21:14:32+00:00"
---

# Java to Kotlin Gilded Rose - Part 2 Refactoring to Composition

This session continues the refactoring of the Gilded Rose kata from Java to Kotlin, focusing on moving from inheritance-based template methods to a more compositional approach. The host, Duncan, refactors the `Item` class hierarchy by replacing mutable methods like `age()` and `degrade()` with functions that return computed values (e.g., `aging` returns a delta, `degradation` returns new quality). This eliminates direct mutation in subclasses and centralizes the update logic in the base class. By inlining these functions and making them open, subclasses can override only the specific calculations they need, reducing coupling and improving readability. The result is a more declarative design where the base class controls the update flow, and subclasses provide only the varying parts, making the overall algorithm easier to understand and test.

- Replaced mutating functions with functions that return computed values, reducing side effects and making intent clearer.
- Converted 'age' from a method that modifies sellIn to a property or function that returns the amount of aging, allowing subclasses to vary aging without changing the aging logic.
- Refactored 'degrade' to return the new quality instead of modifying it directly, then inlined the call to make the base class responsible for applying the result.
- Improved testability by making the quality and sellIn calculations pure functions of their inputs.
- Shifted from inheritance-based template method to composition of simple functions, reducing subclass complexity.