---
domain: android-kotlin
subdomain: kotlin-testing
concept: flow-testing-with-turbine
title: Flow testing with Turbine
sources:
  - title: "Flow testing with Turbine"
    url: "https://code.cash.app/flow-testing-with-turbine"
    author: "Jake Wharton"
---

# Flow testing with Turbine

Turbine is a library from Cash App for testing kotlinx.coroutines Flow. It transforms push-based flows into pull-based suspend functions, enabling developers to write sequential assertions using awaitItem() and awaitComplete(). Each await call suspends until the desired event arrives, and throws an AssertionError when a different event occurs or a timeout is reached. This makes flow testing more predictable and readable (Jake Wharton, https://code.cash.app/flow-testing-with-turbine).

Beyond Flow, Turbine can be used as a standalone adapter for other push-based mechanisms like callbacks, allowing the same pull-based API to test custom interfaces. The library also includes utilities for handling multiple Turbines, multiple Flows, sharing timeouts, and aggregating errors, making it a comprehensive tool for asynchronous testing in Kotlin (Jake Wharton, https://code.cash.app/flow-testing-with-turbine).

- Turbine changes push-based Flow into pull-based suspend functions for simpler testing.
- awaitItem() and awaitComplete() suspend until events arrive, throwing AssertionError on mismatch or timeout.
- Standalone Turbine instances can adapt any push-based mechanism such as callbacks.
- The library includes advanced utilities for multiple Turbines, timeouts, and error aggregation.