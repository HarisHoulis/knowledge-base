---
domain: android-kotlin
subdomain: kotlin
concept: unsigned-integer-underflow
title: Kotlin TDD - Degrading: Unsigned Integer Pitfalls
sources:
  - title: "Kotlin TDD - Degrading"
    url: "https://www.youtube.com/watch?v=jefLQkZV-O8"
    author: "Pairing with Duncan"
    date: "2022-03-23T19:23:26+00:00"
---

# Kotlin TDD - Degrading: Unsigned Integer Pitfalls

In a TDD session on the Gilded Rose kata, the team adds a requirement that item quality should not fall below zero. They write tests for existing behavior and then a test for a zero-quality item updated by one day. The test fails unexpectedly: instead of a negative value or an assertion error, the quality becomes 42 billion. The root cause is that Kotlin's UInt type wraps around on underflow; subtracting 1 from 0 yields a massive positive number. This demonstrates that UInt does not prevent negative values but silently creates them. The team decides to replace UInt with Int throughout the codebase, which fixes the issue and allows the tests to pass. The episode highlights the importance of understanding integer semantics and the value of TDD in surfacing subtle bugs.

- Kotlin UInt wraps around on underflow, so subtracting 1 from 0 produces a huge positive number (around 42 billion).
- Using UInt for quality does not enforce non-negativity; it only changes the failure mode to silent overflow.
- TDD helped reveal the unexpected behavior through a failing test.
- Replacing UInt with Int resolved the issue and allowed the code to compile and tests to pass.