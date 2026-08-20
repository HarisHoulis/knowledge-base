---
domain: android-kotlin
subdomain: TDD and Type Safety
concept: unsigned-integer-wraparound
title: Kotlin TDD: Quality Should Not Fall Below Zero
sources:
  - title: "Kotlin TDD - Degrading"
    url: "https://www.youtube.com/watch?v=jefLQkZV-O8"
    author: "Pairing with Duncan"
    date: "2022-03-23T19:23:26+00:00"
---

# Kotlin TDD: Quality Should Not Fall Below Zero

The Gilded Rose development team, working remotely, receives a new requirement: item quality should never fall below zero. They decide to use TDD to implement this. They first add an assertion to their existing test that quality is non-negative, then write a test for an item with quality 0 that is updated by one day, expecting the quality to remain 0. However, the test fails unexpectedly, revealing that quality becomes 42 billion instead of -1 or 0.

- UInt in Kotlin does not prevent negative values; it wraps around to a large positive number when underflowing.
- Using UInt for a domain value like quality can lead to subtle and surprising bugs.
- TDD helped uncover the issue quickly through a failing test.
- The team resolved the issue by replacing all UInt usages with Int, simplifying the codebase.
- When adding constraints, it's important to test edge cases like the minimum value (0).