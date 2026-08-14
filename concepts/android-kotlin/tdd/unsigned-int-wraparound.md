---
domain: android-kotlin
subdomain: tdd
concept: unsigned-int-wraparound
title: Kotlin TDD: Unsigned Int Wraparound
sources:
  - title: "Kotlin TDD - Degrading"
    url: "https://www.youtube.com/watch?v=jefLQkZV-O8"
    author: "Pairing with Duncan"
    date: "2022-03-23"
---

# Kotlin TDD: Unsigned Int Wraparound

The video demonstrates a TDD approach to a new requirement: item quality should never fall below zero. The existing code uses UInt for quality, assuming it prevents negatives. The team first adds a test to verify that quality never degrades past zero, then writes a failing test where an item with quality 0 is updated by one day. Instead of failing with a negative value, the code produces a quality of approximately 42 billion, revealing that UInt subtraction wraps around when going below zero. This unexpected behavior calls into question the entire use of UInt in the codebase (Pairing with Duncan, 2022).

- UInt in Kotlin is just a bit pattern, not a non-negative integer with overflow protection; subtracting 1 from 0 wraps to a huge positive number.
- TDD helps surface hidden assumptions about type behavior.
- After discovering the issue, the team removes UInt and replaces it with Int throughout the codebase.
- Testing existing functionality before adding new requirements ensures a safety net for refactoring.