---
domain: android-kotlin
subdomain: test-driven-development
concept: uint-underflow
title: Kotlin TDD - Degrading
sources:
  - title: "Kotlin TDD - Degrading"
    url: "https://www.youtube.com/watch?v=jefLQkZV-O8"
    author: "Pairing with Duncan"
    date: "2022-03-23T19:23:26+00:00"
---

# Kotlin TDD - Degrading

The Gilded Rose team receives a new requirement that quality should not fall below zero. They initially assume the use of UInt for quality guarantees non-negativity, so they add a test to verify that degrading an item with zero quality for one day keeps quality at zero. (Pairing with Duncan, 2022)

To test the update logic, they extract it into a separate function and write unit tests covering existing behavior. When they run the new test, they are surprised to find that subtracting one from zero UInt results in approximately 42 billion, not zero or a negative number. This reveals that Kotlin's UInt is just a bit pattern and underflows by wrapping to a large positive value. (Pairing with Duncan, 2022)

The team decides that UInt is misleading and not suitable for enforcing the quality invariant. They replace all UInt occurrences with Int, fix the resulting compile errors, and rerun the tests. The TDD cycle successfully exposed a fundamental issue with the chosen type and guided them toward a more appropriate solution. (Pairing with Duncan, 2022)

- Using UInt for a non-negative invariant can hide logic errors because UInt subtraction wraps around to a large positive number on underflow.
- TDD exposed the underlying type issue: the test expecting quality to stay at zero when decrementing failed with 42 billion instead of negative.
- The team replaced UInt with Int throughout the codebase to correctly handle the domain rule 'quality never goes below zero'.
- Refactoring code to make update logic public and testable helped isolate and verify behavior.