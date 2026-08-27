---
domain: android-kotlin
subdomain: test-driven-development
concept: clock-abstraction
title: Kotlin TDD - To Production At Last
sources:
  - title: "Kotlin TDD - To Production At Last"
    url: "https://www.youtube.com/watch?v=UH7_kYAG-TE"
    author: "Pairing with Duncan"
    date: "2022-03-05T20:10:25+00:00"
---

# Kotlin TDD - To Production At Last

In this session, the team works on integrating a stock-viewing feature into production. They move the Stock class from the test tree to the main tree and wire it into the routes, replacing the previous direct file loading. This is part of a TDD workflow where a previously disabled test is re-enabled and drives the integration (YouTube, 2022).

To make the feature testable while still using the current time in production, they introduce a clock abstraction: a functional parameter that returns an Instant. This allows tests to control time instead of relying on Instant.now(). They also refactor their test fixture to use Instant rather than LocalDate, deriving dates from instants to avoid inconsistency between the date and time values (Pairing with Duncan, 2022).

- Move the Stock class from the test tree to the main source tree and integrate it into the route handler.
- Re-enable a previously disabled test to drive the integration.
- Introduce a clock strategy (function returning Instant) instead of directly calling Instant.now() for testability.
- Change test fixtures from LocalDate to Instant to accurately represent moments in time.
- Derive LocalDate from Instant in fixtures to keep date and time consistent.