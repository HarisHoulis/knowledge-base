---
domain: android-kotlin
subdomain: testing
concept: uint-wrap-around
title: Kotlin TDD: Degrading Item Quality and UInt Surprise
sources:
  - title: "Kotlin TDD - Degrading"
    url: "https://www.youtube.com/watch?v=jefLQkZV-O8"
    author: "Pairing with Duncan"
    date: "2022-03-23"
---

# Kotlin TDD: Degrading Item Quality and UInt Surprise

The Gilded Rose team receives a new requirement: quality should never fall below zero. They decide to implement this using TDD. First, they add a test that existing quality values are non-negative, then they write a failing test for an item with quality zero being updated by one day, expecting it to remain zero. To test the update logic, they extract the update function into a new package and write tests for it, covering the existing behavior of quality decreasing by one each day. When they run the new test for zero quality, it fails unexpectedly: instead of an assertion failure or a negative quality, the value becomes approximately 42 billion. The cause is that Kotlin's UInt is a bit pattern, not a true unsigned integer with overflow protection; subtracting 1 from 0 wraps to the maximum UInt value. Realizing this, they decide to replace UInt with Int throughout the codebase, fixing the immediate test and eliminating the risk of other wrap-around bugs.

- TDD was used to drive the new requirement that quality never goes negative.
- Existing update logic was untested except by approval tests, so they added unit tests for it first.
- Kotlin's UInt does not throw or fail on underflow—it wraps around to a huge positive value.
- The team chose to replace UInt with Int to avoid such surprising behavior.
- Simple find-and-replace of UInt wrappers (e.g., 42u) with plain integers is a quick way to migrate.