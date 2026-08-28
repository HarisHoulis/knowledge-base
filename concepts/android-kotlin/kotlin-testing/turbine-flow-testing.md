---
domain: android-kotlin
subdomain: kotlin-testing
concept: turbine-flow-testing
title: Flow testing with Turbine
sources:
  - title: "Flow testing with Turbine"
    url: "https://code.cash.app/flow-testing-with-turbine"
    author: "Jake Wharton"
---

# Flow testing with Turbine

Turbine is a testing library for kotlinx.coroutines Flow, developed by Cash App. It transforms push-based Flows into pull-based suspend functions, allowing developers to write straightforward, sequential assertions. For example, the `test` function lets you call `awaitItem()` to suspend until the next value arrives and `awaitComplete()` to await the Flow's completion, with AssertionErrors thrown on unexpected events or timeouts.

The library also supports standalone Turbines, which adapt other push-based mechanisms like callbacks for testing. This is useful for custom classes, such as logger instances that push messages; the Turbine collects these messages and exposes the same await-based API for assertions. Beyond basic usage, Turbine provides utilities for managing multiple Turbines, multiple Flows, shared timeouts, and aggregated errors, making it a comprehensive tool for Flow and callback-based testing in Kotlin.

- Turbine converts push-based Flow events into pull-based suspend functions via `test` and await-style methods.
- Use `awaitItem()`, `awaitComplete()`, `awaitError()` to assert flow events and completion or failure.
- Standalone Turbine instances can adapt any push-based mechanism, such as callbacks, for testing.
- The library includes utilities for complex scenarios like multiple Turbines, multiple Flows, and timeouts.