---
domain: android-kotlin
subdomain: kotlin-coroutines-testing
concept: flow-testing-turbine
title: Flow testing with Turbine
sources:
  - title: "Flow testing with Turbine"
    url: "https://code.cash.app/flow-testing-with-turbine"
    author: "Jake Wharton"
---

# Flow testing with Turbine

Turbine 1.0 is a library for testing kotlinx.coroutines Flow, introduced by Cash App. It transforms push-based Flow streams into pull-based suspend functions, simplifying test assertions. The primary API is the `test` block, where developers call `awaitItem()` and `awaitComplete()` to expect specific emissions and completion. If an unexpected event occurs or a timeout is reached, an `AssertionError` is thrown, failing the test. This makes Flow testing deterministic and straightforward. See https://code.cash.app/flow-testing-with-turbine.

- Turbine converts Flow's push-based emissions into pull-based suspend functions for easier testing.
- The `test` block provides `awaitItem()`, `awaitComplete()`, and other methods to assert expected events.
- Standalone Turbines can adapt other push-based mechanisms, such as callbacks, for testing.
- The library includes utilities for handling multiple flows, timeouts, and error aggregation.
- This work is part of Cash App's Summer of Kotlin Multiplatform series.