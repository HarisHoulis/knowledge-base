---
domain: android-kotlin
subdomain: unit-testing
concept: unsigned-int-overflow
title: Kotlin TDD: Degrading Quality
sources:
  - title: "Kotlin TDD - Degrading"
    url: "https://www.youtube.com/watch?v=jefLQkZV-O8"
    author: "Pairing with Duncan"
    date: "2022-03-23T19:23:26+00:00"
---

# Kotlin TDD: Degrading Quality

The team decides to replace all UInt usages with Int, removing the 'U' suffix from numeric literals and adjusting constructors. After fixing compilation errors, the new test passes, and the existing behavior remains verified. The session highlights how test-driven development can surface subtle type-related bugs early and how a simple failing test led to a broader design correction (Pairing with Duncan, 2022).

- UInt in Kotlin wraps on overflow; subtracting 1 from 0 yields a very large number instead of a negative value.
- TDD characterization tests helped expose the unsafe assumption that UInt prevents negative quality.
- The team replaced UInt with Int throughout the codebase, removing unsigned literals and fixing compilation errors.
- Writing a failing test for the new requirement forced a valuable design change, not just a workaround.