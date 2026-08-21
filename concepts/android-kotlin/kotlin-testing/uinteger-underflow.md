---
domain: android-kotlin
subdomain: kotlin-testing
concept: uinteger-underflow
title: Kotlin TDD: Avoiding Negative Quality with UInt Wrap-Around
sources:
  - title: "Kotlin TDD - Degrading"
    url: "https://www.youtube.com/watch?v=jefLQkZV-O8"
    author: "Pairing with Duncan"
    date: "2022-03-23T19:23:26+00:00"
---

# Kotlin TDD: Avoiding Negative Quality with UInt Wrap-Around

This video from Pairing with Duncan demonstrates a test-driven development (TDD) approach to a new requirement for the Gilded Rose inventory system: item quality should never fall below zero. The code currently uses Kotlin's UInt type for quality, which the team initially believes prevents negative values. They begin by adding tests that assert quality is non-negative, then write a failing test for an item with zero quality being updated by one day, expecting it to remain zero.

Instead, the test fails unexpectedly: the item's quality becomes an enormous positive number (over 4 billion) because UInt underflow wraps around to the maximum value. This reveals that UInt does not guard against arithmetic results below zero—it simply wraps around. The team then decides to remove UInt and replace it with Int across the codebase, fixing the compile errors and the failing test. The experience highlights a key lesson: TDD can uncover subtle assumptions about primitive types, and type choices must be validated against actual runtime behavior.

- Kotlin's UInt wraps on underflow rather than throwing an exception, turning a negative result into a huge positive number.
- TDD exposed the unexpected wrapping behavior, which a type-based assumption had masked.
- The design decision to use UInt to prevent negative quality was flawed in practice; switching to Int enabled proper validation.
- The example illustrates the importance of verifying language-specific behavior through tests.