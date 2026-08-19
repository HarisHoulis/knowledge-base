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

Turbine is a library by Cash App for testing kotlinx.coroutines Flow. It transforms push-based Flows into pull-based suspend functions, simplifying tests by allowing developers to await specific items, completion, or errors with methods like `awaitItem()`, `awaitComplete()`, and `awaitError()`. This approach makes Flow tests more deterministic and readable. The library also provides standalone `Turbine` instances that can adapt other push-based mechanisms, such as callbacks, to the same testing API. For example, a `FakeLogger` can collect log messages into a `Turbine` and assert them sequentially. Additionally, Turbine offers utilities for managing multiple Turbines, multiple Flows, shared timeouts, and error aggregation to support more complex testing scenarios.

- Turbine converts push-based Flow events into pull-based suspend functions, enabling straightforward assertion of each emitted value.
- The `test` function allows awaiting items, completion, and errors; mismatches or timeouts throw `AssertionError`.
- Standalone `Turbine` objects can adapt other callback-driven APIs for testing.
- Utilities exist for handling multiple Flows/Turbines, sharing timeouts, and aggregating errors.