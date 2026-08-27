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

Turbine is a library from Cash App for testing kotlinx.coroutines Flow and other push-based mechanisms. It converts push-based flows into pull-based suspend functions, simplifying asynchronous testing by allowing developers to await specific events like items, completion, or errors. The library's `test` function provides a concise API for asserting the sequence of events emitted by a Flow.

- Turbine transforms Flow testing into pull-based suspend functions, making tests linear and readable.
- awaitItem() and awaitComplete() suspend until the desired event occurs, throwing AssertionError on mismatch or timeout.
- Standalone Turbine instances can adapt other push-based mechanisms, such as callbacks, for testing.
- Turbine offers utilities for multiple flows, shared timeouts, and error aggregation for complex testing needs.