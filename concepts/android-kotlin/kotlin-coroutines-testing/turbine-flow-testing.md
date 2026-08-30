---
domain: android-kotlin
subdomain: kotlin-coroutines-testing
concept: turbine-flow-testing
title: Flow testing with Turbine
sources:
  - title: "Flow testing with Turbine"
    url: "https://code.cash.app/flow-testing-with-turbine"
    author: "Jake Wharton"
---

# Flow testing with Turbine

Turbine is a library from Cash App for testing kotlinx.coroutines Flow. It converts push-based Flow events into pull-based suspend functions, allowing tests to await specific items, completion, or errors in a linear, readable manner. The `test` function provides methods like `awaitItem()`, `awaitComplete()`, and `awaitError()`, each suspending until the expected event occurs or throwing an `AssertionError` on timeout or unexpected events.

In addition to testing Flow, Turbine can be used as a standalone utility to adapt other push-based mechanisms, such as callbacks, for testing. A `Turbine` instance can be created and events added via `plus` assignment, then consumed with the same await-based API. This makes it easy to verify callback sequences in tests.

The library also offers advanced utilities for handling multiple turbines and flows, sharing timeout configurations, and aggregating errors, making it a comprehensive testing solution for asynchronous Kotlin code.

- Turbine converts push-based Flow into pull-based suspend functions for simpler testing.
- `awaitItem()` and `awaitComplete()` suspend until events arrive, throwing on mismatch or timeout.
- Supports awaiting errors, skipping items, and cancelling the Flow during tests.
- Standalone Turbines can adapt callback-based APIs for testing.
- Includes utilities for multiple turbines/flows, shared timeouts, and error aggregation.