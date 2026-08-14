---
domain: android-kotlin
subdomain: testing
concept: flow-testing-turbine
title: Flow testing with Turbine
sources:
  - title: "Flow testing with Turbine"
    url: "https://code.cash.app/flow-testing-with-turbine"
    author: "Jake Wharton"
---

# Flow testing with Turbine

Turbine 1.0 is a library from Cash App for testing kotlinx.coroutines Flow. It converts push-based Flows into pull-based suspend functions, simplifying test code. The `test` function allows developers to await items, completion, errors, skip items, cancel the Flow, and more, with assertions failing on unexpected events or timeouts. Standalone Turbine instances can adapt other push-based mechanisms like callbacks for testing, offering the same API as the test function. The library includes utilities for handling multiple Turbines, multiple Flows, shared timeouts, and aggregated errors.

- Turbine changes push-based Flow into pull-based suspend functions for easier testing.
- Use `awaitItem()` and `awaitComplete()` to assert on Flow emissions and completion.
- Standalone Turbines can adapt non-Flow push-based mechanisms like callbacks.
- The library provides utilities for multiple turbines, timeouts, and error aggregation.