---
domain: android-kotlin
subdomain: tdd
concept: uint-underflow
title: Kotlin TDD - Degrading
sources:
  - title: "Kotlin TDD - Degrading"
    url: "https://www.youtube.com/watch?v=jefLQkZV-O8"
    author: "Pairing with Duncan"
    date: "2022-03-23T19:23:26+00:00"
---

# Kotlin TDD - Degrading

The team then refactors the code to use regular Int instead of UInt, replacing all UInt literals and fixing compilation errors. This incident highlights the importance of testing edge cases and not relying solely on type-system assumptions. It also demonstrates a TDD approach: writing a failing test first, observing the surprising failure, and then making the minimal changes to pass the test while improving the design. The session underscores that unsigned types are not a safety net for negative values and that explicit validation or domain modeling may be necessary.

- UInt in Kotlin wraps around on subtraction, so 0 - 1 results in a huge positive number (4.2 billion), not a negative value.
- Using UInt to enforce non-negativity is insufficient because it does not prevent underflow; explicit checks or a different type (e.g., Int) are needed.
- TDD helped surface the unexpected behavior through a failing test, prompting a refactor from UInt to Int across the codebase.
- Existing code was largely untested except for approval tests, so adding unit tests for update functionality was a valuable improvement.