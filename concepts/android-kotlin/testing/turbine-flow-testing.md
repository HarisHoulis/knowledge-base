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

Turbine is a testing library from Cash App for kotlinx.coroutines Flow, designed to simplify verification of asynchronous data streams. Instead of using push-based collectors that require manual synchronization, Turbine transforms a Flow into a pull-based sequence of suspend functions, making tests more sequential and readable. The core API is the `test` extension, which provides suspend functions like `awaitItem()` and `awaitComplete()` to assert emissions and completion events, throwing `AssertionError` on unexpected events or timeouts. This approach allows developers to write straightforward, failure-safe tests for reactive code. One key example from the article shows a flow of meals (Breakfast, Lunch, Dinner) being asserted in order, demonstrating the intuitive syntax that Turbine enables.

- Turbine converts push-based Flows into pull-based suspend functions, simplifying Flow testing.
- The `test` function provides `awaitItem()`, `awaitComplete()`, and other functions that suspend until the desired event arrives or throw an `AssertionError`.
- Standalone `Turbine` instances can adapt non-Flow push-based mechanisms like callbacks for testing.
- Turbine includes utilities for managing multiple Turbines, multiple Flows, shared timeouts, and aggregated errors.
- Turbine is part of Cash App's Summer of Kotlin Multiplatform series.