---
domain: android-kotlin
subdomain: test-driven-development
concept: tdd-unsigned-overflow
title: Kotlin TDD - Degrading
sources:
  - title: "Kotlin TDD - Degrading"
    url: "https://www.youtube.com/watch?v=jefLQkZV-O8"
    author: "Pairing with Duncan"
    date: "2022-03-23T19:23:26+00:00"
---

# Kotlin TDD - Degrading

In this TDD session, the Gilded Rose development team attempts to implement a new requirement: quality should never drop below zero. They start by adding a test for an existing item, expecting quality to decrement by one per day. Then they add a test for an item with quality zero to ensure it remains zero after a day. Instead of passing, this test exposes surprising behavior in Kotlin's unsigned integer type: subtracting 1 from 0 as a UInt wraps around to 4,294,967,295 (42 billion), not a negative number. The team realizes that UInt does not prevent negative values; it simply wraps around on underflow, which is useless for their invariant (source: https://www.youtube.com/watch?v=jefLQkZV-O8).

After discovering the unexpected wrapping, they decide to abandon UInt in favor of Int throughout the codebase. This requires replacing all UInt constructors and fixing compilation errors. The failing test drives the change, and the team is able to proceed with the requirement once the type is corrected. The video highlights the importance of testing edge cases and not trusting type names to enforce domain rules without verification (source: https://www.youtube.com/watch?v=jefLQkZV-O8).

- Writing a test for the requirement 'quality should not fall below zero' revealed a bug in the existing implementation.
- Kotlin's UInt type does not reject negative results; it wraps around on underflow, turning 0 - 1 into 4,294,967,295.
- The team refactored from UInt to Int across the codebase to fix the issue, guided by the failing test.
- TDD helped uncover an assumption about unsigned integers that was incorrect in Kotlin.