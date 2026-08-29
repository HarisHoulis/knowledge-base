---
domain: android-kotlin
subdomain: kotlin-flow-testing
concept: turbine-flow-testing
title: Flow testing with Turbine
sources:
  - title: "Flow testing with Turbine"
    url: "https://code.cash.app/flow-testing-with-turbine"
    author: "Jake Wharton"
---

# Flow testing with Turbine

According to the article "Flow testing with Turbine" (https://code.cash.app/flow-testing-with-turbine), JetBrains' Kotlin coroutines library introduces Flow, a push-based streaming API. Testing such flows traditionally requires collecting values into a list and then asserting, which is cumbersome. Turbine 1.0, a library by Cash App (authored by Jake Wharton), changes push-based Flows into pull-based suspend functions to simplify testing. This approach allows test code to await specific events one at a time in a natural, sequential manner.

The article demonstrates Turbine's core API with an example: `mealsFlow.test { assertEquals(Meal.Breakfast, awaitItem()); assertEquals(Meal.Lunch, awaitItem()); assertEquals(Meal.Dinner, awaitItem()); awaitComplete() }`. Each `awaitItem()` or `awaitComplete()` suspends until the desired event arrives. If a different event occurs or a timeout is reached, these functions throw an `AssertionError` and fail the test. Beyond basic item/complete waiting, Turbine supports waiting for errors, skipping items, cancelling the Flow, and more.

Beyond Flow, standalone `Turbine` instances can be created to adapt other push-based mechanisms, such as callbacks, for testing. The article shows a `FakeLogger` that uses a `Turbine<String>` to capture log messages. Later, test code can pull these messages out using the same API (`awaitItem()`). This makes Turbine a versatile testing utility for asynchronous code.

For more complex scenarios, Turbine provides utilities for managing multiple Turbines and Flows, sharing timeouts across tests, and aggregating errors. The library is part of Cash App's Summer of Kotlin Multiplatform series.

- Turbine transforms push-based Flow into pull-based suspend functions, enabling straightforward linear test assertions.
- Core functions `awaitItem()` and `awaitComplete()` suspend until the expected event, throwing `AssertionError` on mismatch or timeout.
- Standalone Turbine instances can adapt callbacks and other push-based mechanisms, providing the same familiar API.
- Utilities support multiple Turbines/Flows, shared timeouts, and aggregated error handling for complex test suites.