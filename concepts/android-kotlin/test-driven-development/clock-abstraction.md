---
domain: android-kotlin
subdomain: test-driven-development
concept: clock-abstraction
title: Kotlin TDD - To Production At Last
sources:
  - title: "Kotlin TDD - To Production At Last"
    url: "https://www.youtube.com/watch?v=UH7_kYAG-TE"
    author: "Pairing with Duncan"
    date: "2022-03-05"
---

# Kotlin TDD - To Production At Last

The team integrates a stock updating feature using Kotlin and TDD. They start by re-enabling a disabled test that captures the expected behavior, then move the Stock class from the test tree to the main source set so it can be used in production. To make time-dependent behavior testable, they introduce a clock functional parameter that returns an Instant, replacing direct calls to Instant.now(). This allows tests to control time deterministically. They then refactor their test fixtures to use Instant instead of LocalDate for precise timing, deriving dates from instants, and commit the work as a work-in-progress.

- Re-enable a failing test to drive the integration of new functionality.
- Move production code from the test tree into the main source set.
- Introduce a clock function parameter to inject time, avoiding direct Instant.now() calls.
- Refactor test fixtures to use Instant for precise time control and derive LocalDate from it.
- Commit work-in-progress to checkpoint progress during TDD.