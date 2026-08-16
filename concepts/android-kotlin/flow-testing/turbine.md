---
domain: android-kotlin
subdomain: flow-testing
concept: turbine
title: Flow testing with Turbine
sources:
  - title: "Flow testing with Turbine"
    url: "https://code.cash.app/flow-testing-with-turbine"
    author: "Jake Wharton"
---

# Flow testing with Turbine

Turbine 1.0, a library by Cash App, simplifies testing of kotlinx.coroutines Flow by converting push-based flows into pull-based suspend functions. As described in the article, developers can use a `test` block to sequentially await expected emissions with `awaitItem()`, wait for completion with `awaitComplete()`, or handle errors and cancellations (source: Flow testing with Turbine, https://code.cash.app/flow-testing-with-turbine). Each await call suspends until the desired event arrives, and if a different event occurs or a timeout is reached, the functions throw an AssertionError to fail the test.

Beyond `Flow`, standalone `Turbine` instances can adapt other push-based mechanisms like callbacks for testing. For example, a fake logger can add messages to a `Turbine`, and tests can pull them out using the same API as the `test` function. This allows consistent, readable testing for asynchronous event streams (source: Flow testing with Turbine, https://code.cash.app/flow-testing-with-turbine).

The library also offers utilities for managing multiple `Turbine`s, coordinating multiple `Flow`s, sharing timeouts, and aggregating errors, catering to more complex testing scenarios (source: Flow testing with Turbine, https://code.cash.app/flow-testing-with-turbine).

- Turbine 1.0 makes Flow testing pull-based and sequential, using suspend functions like `awaitItem()` and `awaitComplete()`.
- Test assertions automatically throw `AssertionError` on unexpected events or timeouts, failing tests clearly.
- Standalone `Turbine`s can wrap callback-based APIs, enabling consistent testing patterns beyond `Flow`.
- Utilities for multiple turbines, shared timeouts, and error aggregation support complex asynchronous testing.