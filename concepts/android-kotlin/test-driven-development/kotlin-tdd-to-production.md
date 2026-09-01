---
domain: android-kotlin
subdomain: test-driven-development
concept: kotlin-tdd-to-production
title: Kotlin TDD - To Production At Last
sources:
  - title: "Kotlin TDD - To Production At Last"
    url: "https://www.youtube.com/watch?v=UH7_kYAG-TE"
    author: "Pairing with Duncan"
    date: "2022-03-05T20:10:25+00:00"
---

# Kotlin TDD - To Production At Last

In this video, the team completes a story about updating stock quantities when viewing stock in the browser. They begin by re-enabling a disabled test that outlines expected behavior, confirming it fails due to unimplemented wiring. The production class 'Stock' is moved from the test tree to the main tree, and route handlers are refactored to use this new class instead of directly loading from the stock file. A key challenge surfaces: the tests need to control time, so a 'clock' function parameter is introduced to abstract instant retrieval, allowing the tests to pass specific instants instead of using 'Instant.now()' inside the code. The team also converts test inputs from LocalDate to Instant to accurately represent points in time, and adjusts fixtures to derive one from the other to maintain consistency. They commit this progress as work in progress, acknowledging there are likely issues to fix as development continues.

- Re-enable a failing test to guide integration work.
- Move production code from test tree to main tree for reuse.
- Introduce a clock abstraction to make time controllable in tests.
- Use Instant instead of LocalDate for precise time handling.