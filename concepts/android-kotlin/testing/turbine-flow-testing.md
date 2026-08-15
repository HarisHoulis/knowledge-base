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

Turbine is a library from Cash App for testing kotlinx.coroutines Flow. It transforms push-based Flow streams into pull-based suspend functions, enabling developers to write sequential assertions using `awaitItem()` and `awaitComplete()` within a `test { }` block. Each call suspends until the desired event arrives, and if a different event occurs or a timeout is reached, an `AssertionError` is thrown to fail the test. This approach simplifies testing flows by making them behave like synchronous collections.

- Turbine changes push-based Flow into pull-based suspend functions for easier testing.
- The `test { }` block allows asserting emitted items, completion, errors, skipping items, and cancellation.
- Standalone Turbine instances can adapt other push-based mechanisms like callbacks for testing.
- Turbine includes utilities for multiple flows, multiple turbines, shared timeouts, and error aggregation.
- This library is part of Cash App's Summer of Kotlin Multiplatform series.