---
domain: android-kotlin
subdomain: test-driven-development
concept: injectable-clock
title: Kotlin TDD: Integrating Stock Update with Injectable Clock
sources:
  - title: "Kotlin TDD - To Production At Last"
    url: "https://www.youtube.com/watch?v=UH7_kYAG-TE"
    author: "Pairing with Duncan"
    date: "2022-03-05T20:10:25+00:00"
---

# Kotlin TDD: Integrating Stock Update with Injectable Clock

The session focuses on completing a story where viewing stock in the browser should update quantities. The team re-enables a previously disabled test that fails because the system isn't wired together. They move the stock class from the test tree into the main tree, making it available for production use. The main routes are updated to use the stock class instead of directly loading items, and a clock dependency is introduced as a functional parameter to control time in tests, replacing the hard-coded Instant.now(). The test fixture is refactored to include an instant property, and tests are updated to use instants rather than local dates, ensuring the system is testable and time-dependent logic can be verified.

- Move code from test tree to main tree when it's ready for production integration.
- Introduce a functional parameter (e.g., a clock) to inject time dependencies, making tests deterministic.
- Replace Instant.now() with an injected clock to control time in tests.
- Refactor test fixtures to use instants instead of local dates to accurately represent time-dependent behavior.