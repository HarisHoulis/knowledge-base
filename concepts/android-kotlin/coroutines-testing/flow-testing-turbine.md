---
domain: android-kotlin
subdomain: coroutines-testing
concept: flow-testing-turbine
title: Flow testing with Turbine
sources:
  - title: "Flow testing with Turbine"
    url: "https://code.cash.app/flow-testing-with-turbine"
    author: "Jake Wharton"
---

# Flow testing with Turbine

Turbine is a library from Cash App for testing kotlinx.coroutines Flow. It changes push-based Flows into pull-based suspend functions, enabling testers to await specific events like items, completion, or errors. The `test` function provides a concise DSL where `awaitItem()` suspends until the next emission, and `awaitComplete()` waits for the flow to finish; unexpected events or timeouts result in an `AssertionError` (source). Standalone `Turbine` instances can adapt other push-based mechanisms, such as callbacks, by adding values with the `+=` operator, making them testable with the same API. The library also includes utilities for managing multiple Turbines, multiple Flows, shared timeouts, and aggregated errors (source).

- Turbine converts push-based Flows into pull-based suspend functions for simpler testing.
- The `test` function lets you await items, completion, and errors; mismatches or timeouts throw AssertionError.
- Standalone Turbines adapt non-Flow push-based mechanisms like callbacks for testing.
- Utilities support multiple Flows/Turbines, shared timeouts, and error aggregation.