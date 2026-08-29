---
domain: android-kotlin
subdomain: test-driven-development
concept: clock-dependency-injection
title: Kotlin TDD - To Production At Last
sources:
  - title: "Kotlin TDD - To Production At Last"
    url: "https://www.youtube.com/watch?v=UH7_kYAG-TE"
    author: "Pairing with Duncan"
    date: "2022-03-05T20:10:25+00:00"
---

# Kotlin TDD - To Production At Last

The video demonstrates integrating a stock update feature into production using TDD. The team re-enables a previously disabled test that defines the expected behavior, watches it fail, and moves the stock class from the test tree into the main source tree to make it usable. To make the feature testable, they introduce a clock strategy—a functional parameter that returns an Instant—instead of directly calling Instant.now() in the production code. This allows tests to control time precisely, leading them to change fixtures from LocalDate to Instant for accurate end-of-day boundary testing.

- Re-enabling a failing test guides the integration effort.
- Moving code from test tree to main tree enables production use.
- Injecting a clock function decouples time-dependent logic from the system clock.
- Switching from LocalDate to Instant allows precise control over time boundaries in tests.