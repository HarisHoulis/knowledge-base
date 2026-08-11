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

Turbine is a library from Cash App for testing kotlinx.coroutines Flow and other push-based mechanisms. It changes push-based Flows into pull-based suspend functions, allowing testers to write straightforward sequential assertions using awaitItem(), awaitComplete(), and related methods. Each await call suspends until the expected event arrives; if a different event occurs or a timeout is reached, it throws an AssertionError to fail the test (source: 'Flow testing with Turbine').

Beyond Flows, Turbine can be used standalone to adapt other push-based mechanisms like callbacks. For example, a FakeLogger can add messages to a Turbine<String>, and tests can then pull those messages with the same API. As testing needs grow, Turbine provides utilities for handling multiple Turbines, multiple Flows, shared timeouts, and error aggregation.

- Turbine converts push-based Flow events into pull-based suspend functions for easier testing.
- awaitItem() and awaitComplete() suspend until the expected event or completion; mismatches and timeouts throw AssertionError.
- Standalone Turbine instances can be used to test other push-based mechanisms, such as callbacks.
- Utilities are available for more complex scenarios: multiple Flows, multiple Turbines, shared timeouts, and aggregated errors.