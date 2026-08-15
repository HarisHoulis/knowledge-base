---
domain: android-kotlin
subdomain: kotlin-testing
concept: kotlin-uint-pitfall
title: Kotlin TDD: The UInt Underflow Surprise
sources:
  - title: "Kotlin TDD - Degrading"
    url: "https://www.youtube.com/watch?v=jefLQkZV-O8"
    author: "Pairing with Duncan"
    date: "2022-03-23T19:23:26+00:00"
---

# Kotlin TDD: The UInt Underflow Surprise

In this video, the Gilded Rose team faces a new requirement: item quality must never fall below zero. Tempted to rely on Kotlin's UInt type as a safeguard, they write a test to verify that an item with zero quality does not become negative after one update. Surprisingly, the test fails because subtracting 1 from a UInt value of 0 wraps around to 4294967295 (42 billion), revealing that UInt operations in Kotlin are bitwise and do not automatically prevent underflow. This demonstrates that UInt does not guarantee the intended invariant of non-negativity; it merely changes the failure mode into a wrap-around.

To fix the issue, the team refactors the code from UInt to Int, systematically replacing all unsigned integer literals and parameters. After updating the code to compile with Int, the same test passes, ensuring quality stays at zero instead of underflowing. Along the way, they extract the update function to make it testable and add unit tests for the existing behavior (items degrade by one per day), as that logic was only covered by approval tests before. The session underscores the value of TDD in exposing surprising type behaviors and guiding developers toward simpler, more appropriate types when their semantics don't match the domain constraints.

- Kotlin's UInt does not prevent negative arithmetic results; underflow wraps to a large positive value.
- A failing test written first exposed the UInt underflow issue, demonstrating TDD's power to reveal unexpected behavior.
- Refactoring from UInt to Int fixed the bug and simplified the codebase after a global find-and-replace.
- Adding unit tests for existing update logic improved coverage beyond the previous approval-only tests.