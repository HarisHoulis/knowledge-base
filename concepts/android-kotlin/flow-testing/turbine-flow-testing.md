---
domain: android-kotlin
subdomain: flow-testing
concept: turbine-flow-testing
title: Flow testing with Turbine
sources:
  - title: "Flow testing with Turbine"
    url: "https://code.cash.app/flow-testing-with-turbine"
    author: "Jake Wharton"
---

# Flow testing with Turbine

Turbine is a library from Cash App for testing kotlinx.coroutines Flow, and it transforms push-based flows into pull-based suspend functions to simplify test code. As demonstrated by Jake Wharton, you can use `awaitItem()` and `awaitComplete()` to suspend until expected events arrive, and the library throws `AssertionError` on unexpected events or timeouts (Jake Wharton, "Flow testing with Turbine").

Beyond Flows, standalone `Turbine` instances can adapt other push-based mechanisms like callbacks. The example shows a `FakeLogger` that adds messages to a `Turbine`, which is then used to assert expected log output in tests. This approach reuses the same API as the `test` function, making it versatile for various asynchronous testing scenarios.

The library also provides utilities for handling multiple Turbines and Flows, sharing timeouts, and aggregating errors, which helps as testing needs grow.

- Turbine converts push-based Flows into pull-based suspend functions for easier testing.
- `awaitItem()`, `awaitComplete()`, and similar functions suspend until events arrive, failing on mismatches or timeouts.
- Standalone Turbines can adapt callbacks and other push-based sources for testing.
- Additional utilities support multiple Turbines/Flows, shared timeouts, and error aggregation.