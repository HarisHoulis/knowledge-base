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

Turbine is a library from Cash App for testing kotlinx.coroutines Flow and other push-based mechanisms. It transforms push-based flows into pull-based suspend functions, allowing testers to await specific events like items, completion, or errors in a sequential manner. The example demonstrates awaiting meal items and completion, with failures thrown as AssertionError if events don't match or time out. Turbine also supports standalone instances for adapting callbacks and other push-based APIs, as shown with a FakeLogger that receives log messages into a Turbine.

- Turbine converts Flow emissions into awaitable suspend functions, simplifying sequential assertions.
- Await functions throw AssertionError on unexpected events or timeouts, aiding deterministic tests.
- Standalone Turbines can adapt any push-based mechanism, such as callbacks, for testing.
- The library provides additional utilities for multiple flows, shared timeouts, and error aggregation.