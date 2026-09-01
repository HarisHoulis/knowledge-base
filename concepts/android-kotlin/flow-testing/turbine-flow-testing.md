---
domain: android-kotlin
subdomain: flow-testing
concept: turbine-flow-testing
title: Flow testing with Turbine
sources:
  - title: "Flow testing with Turbine"
    url: "https://code.cash.app/flow-testing-with-turbine"
    author: "Jake Wharton"
---

# Flow testing with Turbine

Turbine is a library from Cash App for testing kotlinx.coroutines Flow. It transforms push-based Flows into pull-based suspend functions, simplifying assertions by letting developers await specific items, completions, or errors. The `test` function provides a concise API, as shown in the mealsFlow example, where each `awaitItem()` suspends until the next event arrives; mismatched events or timeouts cause AssertionError. Turbine can also be used as a standalone object to adapt other push-based mechanisms like callbacks, demonstrated through a FakeLogger that records log messages into a Turbine for later assertion. The library offers additional utilities for handling multiple Turbines, multiple Flows, shared timeouts, and aggregated errors, catering to growing testing needs.

- Turbine changes push-based Flows into pull-based suspend functions to simplify testing.
- `awaitItem()` and `awaitComplete()` suspend until the desired event arrives, throwing AssertionError on mismatch or timeout.
- Standalone Turbines can adapt other push-based mechanisms like callbacks for testing.
- Utilities support multiple Turbines, multiple Flows, shared timeouts, and aggregated errors.