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

Turbine is a library from Cash App for testing kotlinx.coroutines Flow and other push-based mechanisms. It transforms push-based flows into pull-based suspend functions, allowing tests to await specific items or completion events. The `test` function provides a concise way to assert expected emissions, and each await call suspends until the event arrives or fails the test if an unexpected event occurs or a timeout is reached.

- Turbine converts push-based Flows into pull-based suspend functions for easier testing.
- The `test` function lets you await items, completion, errors, skip items, cancel the Flow, and more.
- Standalone Turbines can adapt other push-based mechanisms like callbacks for testing.
- Turbine provides utilities for multiple Turbines, multiple Flows, shared timeouts, and aggregating errors.