---
domain: android-kotlin
subdomain: test-driven-development
concept: clock-strategy
title: Kotlin TDD - To Production At Last
sources:
  - title: "Kotlin TDD - To Production At Last"
    url: "https://www.youtube.com/watch?v=UH7_kYAG-TE"
    author: "Pairing with Duncan"
    date: "2022-03-05T20:10:25+00:00"
---

# Kotlin TDD - To Production At Last

The video covers the final integration of a stock update feature into a Kotlin application. The team re-enables a disabled test and moves the `Stock` class from the test tree into the main source tree, wiring it into the route handler. The stock list now updates via the `Stock` class, which relies on a time zone and an update strategy copied from tests.

- Move tested code from test tree to main tree when ready for production.
- Introduce a clock function (returning an `Instant`) to make tests deterministic by controlling time.
- Prefer `Instant` over `LocalDate` when precise timing matters, such as end-of-day stock updates.
- Derive related fixture values (e.g., date from instant) to keep test data consistent.
- Commit work in progress to checkpoint progress during integration.