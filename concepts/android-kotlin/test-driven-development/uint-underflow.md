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

In this episode, Duncan and the Gilded Rose development team tackle a new requirement: item quality should never fall below zero. They adopt a TDD approach, first writing a test to verify that an item with quality zero stays at zero after a day's update. Running the test reveals surprising behavior: instead of failing with a negative value or an exception, the quality jumps to a massive number like 42 billion. This occurs because the codebase uses Kotlin's UInt type, and subtracting 1 from 0 underflows, wrapping around to a huge positive value. The test failure exposes that UInt does not enforce non-negativity; it merely wraps on overflow, which is unintuitive and dangerous for this domain.

Realizing the issue, the team decides to abandon UInt in favor of Int for all quality fields. This change requires updating the type declarations and removing the unsigned integer literals across the codebase, causing many compilation errors that are fixed systematically. Once switched to Int, the tests pass, confirming that quality now correctly clamps at zero instead of wrapping. The video highlights how TDD can uncover hidden assumptions about data types and forces a reconsideration of implementation choices early in the process.

- UInt in Kotlin wraps on underflow, so subtracting 1 from 0 produces a very large positive number, not a negative or error.
- TDD helped reveal the unexpected UInt behavior by writing a failing test for the 'quality not below zero' requirement.
- Using UInt as a type does not guarantee non-negative values; it only changes the memory representation and wrap-around semantics.
- The team refactored from UInt to Int, making the code more intuitive and ensuring the quality floor is enforced correctly.