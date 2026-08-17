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

Turbine is a library from Cash App for testing kotlinx.coroutines Flow, and it changes push-based Flows into pull-based suspend functions to simplify testing (source: https://code.cash.app/flow-testing-with-turbine). The primary API is the `test` block, where developers can call `awaitItem()`, `awaitComplete()`, and similar functions to assert on emitted values and completion. Each `awaitItem()` or `awaitComplete()` call suspends until the desired event arrives; if a different event occurs or a timeout is reached, the functions throw an `AssertionError` and fail the test (source: https://code.cash.app/flow-testing-with-turbine).

Beyond Flows, standalone `Turbine` instances can be created to adapt other push-based mechanisms, such as callbacks, for testing. For example, a `FakeLogger` can expose a `Turbine<String>` that captures log messages and allows assertions via the same API as the `test` function (source: https://code.cash.app/flow-testing-with-turbine). The library also includes utilities for managing multiple Turbines and Flows, sharing timeouts, aggregating errors, and other advanced testing needs (source: https://code.cash.app/flow-testing-with-turbine).

- Turbine converts push-based Flows into pull-based suspend functions, enabling straightforward sequential assertions.
- `awaitItem()` and `awaitComplete()` suspend until the expected event arrives, throwing `AssertionError` on mismatches or timeouts.
- Standalone Turbines can be used to test callback-based or other non-Flow push-based APIs.
- The library provides additional utilities for complex testing scenarios involving multiple Flows, shared timeouts, and error aggregation.