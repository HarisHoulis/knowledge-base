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

Turbine is a library from Cash App for testing kotlinx.coroutines Flow and other push-based mechanisms. It transforms push-based flows into pull-based suspend functions, allowing developers to write straightforward sequential assertions. The library's core `test` function lets you await emitted items, completion, or errors, with failures throwing AssertionError on unexpected events or timeouts (Jake Wharton).

Turbine can also be used as a standalone object to adapt callbacks and other push-based patterns for testing. For example, a fake logger can add messages to a Turbine, which can then be awaited upon in tests. The library provides additional utilities for handling multiple turbines, flows, timeouts, and error aggregation, making it a comprehensive testing tool for asynchronous code (Jake Wharton).

- Turbine changes push-based Flows into pull-based suspend functions for simplified testing.
- Use `test` to await items, completion, or errors sequentially; unexpected events or timeouts throw AssertionError.
- Standalone Turbines can adapt any push-based mechanism, such as callbacks, into testable queues.
- The library includes utilities for multiple turbines, multiple flows, shared timeouts, and error aggregation.