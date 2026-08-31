---
domain: android-kotlin
subdomain: tdd
concept: uint-overflow
title: Kotlin TDD: Quality Degradation and UInt Overflow
sources:
  - title: "Kotlin TDD - Degrading"
    url: "https://www.youtube.com/watch?v=jefLQkZV-O8"
    author: "Pairing with Duncan"
    date: "2022-03-23T19:23:26+00:00"
---

# Kotlin TDD: Quality Degradation and UInt Overflow

In this TDD session, the Gilded Rose team adds a requirement that item quality should never fall below zero. They introduce a unit test to verify that an item with quality zero, when updated, remains zero. The current implementation uses Kotlin's UInt for quality, and the update subtracts one. Instead of failing an assertion or producing a negative value, the test reveals that UInt subtraction underflows: zero minus one becomes a 42-billion value. This happens because Kotlin's UInt is just a bit pattern and does not enforce non-negativity; arithmetic wraps around. The team decides to replace all UInt usages with Int across the codebase, which fixes the tests and highlights a flaw in the original design. They also note that existing behavior was only covered by approval tests, so they added direct unit tests for the update logic.

- Kotlin's UInt does not saturate; subtracting from zero wraps to a large positive number.
- TDD helped uncover unexpected UInt behavior through a failing test.
- The team concluded that UInt was not suitable for the quality field and replaced it with Int.
- Existing update logic had no unit tests, only approval tests, so targeted tests were added.
- The change from UInt to Int required removing the 'u' suffixes from numeric literals.