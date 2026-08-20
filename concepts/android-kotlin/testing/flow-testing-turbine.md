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

Turbine 1.0 is a library from Cash App for testing kotlinx.coroutines Flow and other push-based mechanisms. It transforms push-based Flows into pull-based suspend functions, allowing tests to await specific items or completion using functions like awaitItem() and awaitComplete(). These functions suspend until the desired event arrives, throwing AssertionError if a different event occurs or a timeout is reached, which makes Flow tests more deterministic and readable.

The library also provides standalone Turbines that can adapt other push-based mechanisms such as callbacks for testing. For example, a custom logger can push messages into a Turbine, and tests can then pull those messages with the same API as the Flow test function. Turbine includes additional utilities for managing multiple Turbines, multiple Flows, shared timeouts, and error aggregation, making it a comprehensive solution for event-stream testing.

- Turbine converts push-based Flows into pull-based suspend functions for easier testing.
- awaitItem() and awaitComplete() suspend until the expected event, throwing AssertionError on mismatch or timeout.
- Standalone Turbines can adapt callbacks and other push sources for testing.
- The library offers utilities for multiple Turbines, multiple Flows, shared timeouts, and error aggregation.