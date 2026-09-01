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

Turbine is a library by Cash App for testing kotlinx.coroutines Flow. It transforms push-based flows into pull-based suspend functions, enabling developers to assert on emitted items, completion, errors, and cancellation in a straightforward manner. The `test` extension suspends on `awaitItem()` and `awaitComplete()` calls, throwing `AssertionError` on mismatched events or timeouts. Standalone `Turbine` instances can also adapt other push-based mechanisms such as callbacks for testing, as demonstrated with a `FakeLogger` class. Turbine also offers utilities for handling multiple flows, aggregated errors, and shared timeouts. This post is part of Cash App's Summer of Kotlin Multiplatform series.

- Turbine converts push-based Flow into pull-based suspend functions for easier testing
- Provides `awaitItem()`, `awaitComplete()`, and error handling with AssertionError on failures
- Standalone Turbine can be used to test callback-based APIs
- Includes utilities for multiple Turbines, multiple Flows, sharing timeouts, and aggregating errors