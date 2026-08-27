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

The Gilded Rose team receives a new requirement that item quality should not fall below zero. Using TDD, they write tests to verify this behavior. When they test an item with zero quality and update it by one day, they expect the quality to remain zero, but instead, it jumps to roughly 42 billion. The root cause is Kotlin's UInt type: it wraps around on underflow rather than clamping or erroring. The team realizes UInt is unsuitable for values that can conceptually become negative, so they refactor the codebase to use Int instead. This involves changing the item class and replacing all unsigned integer literals. The failing test highlights the hidden dangers of unsigned types and reinforces the value of TDD in exposing unintended behavior.

- TDD guides the implementation of a quality floor by writing a failing test first.
- Kotlin's UInt wraps around when decremented below zero, producing a huge positive number.
- Unsigned types are not a safeguard against negative logic; they only affect the bit pattern.
- Switching from UInt to Int resolves the underflow and aligns with domain semantics.
- The team uses a simple find-and-replace to migrate unsigned literals to signed ones.