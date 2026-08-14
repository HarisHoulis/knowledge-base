---
domain: android-kotlin
subdomain: test-driven-development
concept: clock-injection
title: Kotlin TDD - To Production At Last
sources:
  - title: "Kotlin TDD - To Production At Last"
    url: "https://www.youtube.com/watch?v=UH7_kYAG-TE"
    author: "Pairing with Duncan"
    date: "2022-03-05T20:10:25+00:00"
---

# Kotlin TDD - To Production At Last

The video demonstrates the final integration of a feature in a Kotlin project using TDD. The team re-enables a previously disabled test that specifies the requirement: when viewing stock in the browser, quantities should update. The test fails initially because the production code is not wired together. To fix this, the Stock class, originally written in the test tree, is moved to the main source tree. The route handler is then updated to call Stock instead of directly loading items from a stock file, and a strategy for updating stock is introduced.

- Move production code from test tree to main tree when ready for integration.
- Use dependency injection for time (a 'clock' function returning Instant) to make tests deterministic.
- Prefer Instant over LocalDate when precise timing is needed for stock updates.
- Incrementally commit work-in-progress to checkpoint progress during refactoring.