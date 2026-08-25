---
domain: android-kotlin
subdomain: kotlin-testing
concept: uint-wrapping
title: Kotlin TDD - Degrading
sources:
  - title: "Kotlin TDD - Degrading"
    url: "https://www.youtube.com/watch?v=jefLQkZV-O8"
    author: "Pairing with Duncan"
    date: "2022-03-23T19:23:26+00:00"
---

# Kotlin TDD - Degrading

In this TDD session, the Gilded Rose team addresses a new requirement: item quality should never fall below zero. They start by writing tests for existing behavior—items decrease in quality by one per day—then add a failing test for a zero-quality item, expecting it to remain zero. The test fails unexpectedly: instead of a negative value, the quality becomes approximately 42 billion because Kotlin's UInt type wraps around on underflow, turning a subtraction from zero into a large positive bit pattern (Pairing with Duncan, 2022). This demonstrates that UInts in Kotlin behave more like raw bit patterns than true unsigned integers, and the team decides to eliminate them entirely. They replace all UInts with Ints, converting unsigned literals like 42u to plain integers, which resolves the compilation errors and makes the failing test pass. The video underscores the importance of testing edge cases and understanding language-specific numeric behavior in Kotlin.

- TDD: write tests for existing behavior before adding new functionality.
- Kotlin's UInt wraps on underflow, turning negative results into huge positive values.
- UInts in Kotlin are bit patterns, not integers with overflow protection.
- Replacing UInt with Int simplifies code and avoids hidden wraparound bugs.