---
domain: android-kotlin
subdomain: testing
concept: turbine-flow-testing
title: Flow testing with Turbine
sources:
  - title: "Flow testing with Turbine"
    url: "https://code.cash.app/flow-testing-with-turbine"
    author: "Jake Wharton"
---

# Flow testing with Turbine

Turbine is a library from Cash App for testing kotlinx.coroutines Flow, converting push-based flows into pull-based suspend functions. This allows developers to write deterministic tests by awaiting specific emissions with `awaitItem()` and completion with `awaitComplete()`, which throw AssertionError on unexpected events or timeouts. The library also supports standalone Turbine instances to test other push-based mechanisms like callbacks, making it versatile beyond Flow testing.

- Turbine simplifies Flow testing by enabling pull-based assertions on emissions and completion.
- The `test` function allows sequential `awaitItem()` and `awaitComplete()` calls that fail tests on unexpected events.
- Standalone Turbines can adapt callbacks or other push-based sources for testing.
- The library provides utilities for multiple turbines, shared timeouts, and error aggregation.