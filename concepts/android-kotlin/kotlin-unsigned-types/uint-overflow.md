---
domain: android-kotlin
subdomain: kotlin-unsigned-types
concept: uint-overflow
title: Kotlin TDD: Degrading Quality with UInt Overflows
sources:
  - title: "Kotlin TDD - Degrading"
    url: "https://www.youtube.com/watch?v=jefLQkZV-O8"
    author: "Pairing with Duncan"
    date: "2022-03-23T19:23:26+00:00"
---

# Kotlin TDD: Degrading Quality with UInt Overflows

In this session, Duncan demonstrates test-driven development (TDD) to implement a requirement that item quality should not fall below zero. The codebase uses Kotlin's UInt for quality, and the team writes a test expecting that an item starting at quality 0 remains at 0 after one day. To make the update logic testable, they extract it into a separate function and add tests for existing behavior, such as quality decreasing by 1 per day. (source: Pairing with Duncan, 2022).

The test for zero quality reveals a surprising bug: instead of failing with a negative value, the UInt wraps around to 42 billion when subtracting 1 from 0. Duncan explains that Kotlin's UInt is not a safe integer type—it's a bit pattern with modular arithmetic, so underflow produces a huge positive number. This discovery calls into question the use of UInt throughout the codebase, and they decide to replace all UInt usages with Int. The fix involves changing type declarations, removing the 'u' suffix from literals, and updating constructors to accept Int. (source: Pairing with Duncan, 2022).

The session highlights how TDD can expose unexpected behavior, and the importance of choosing appropriate primitive types. Using Int for quantities that should not underflow avoids the silent wrap-around issue, making the code more predictable and easier to reason about.

- Kotlin's UInt is not a safe, bounded integer; subtract 1 from 0 wraps to 4294967295 (42 billion).
- TDD helped expose the underflow bug by writing a failing test for the non-negative quality requirement.
- Extracting update logic into a testable function allowed targeted unit tests rather than relying solely on approval tests.
- When a domain quantity must not go below zero, using Int is simpler and avoids surprising modular arithmetic.