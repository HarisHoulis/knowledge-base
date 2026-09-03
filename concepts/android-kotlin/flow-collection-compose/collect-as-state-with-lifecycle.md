---
domain: android-kotlin
subdomain: flow-collection-compose
concept: collect-as-state-with-lifecycle
title: Consuming flows safely in Jetpack Compose
sources:
  - title: "Consuming flows safely in Jetpack Compose"
    url: "https://medium.com/androiddevelopers/consuming-flows-safely-in-jetpack-compose-cde014d0d5a3?source=rss-3b5622dd813c------2"
    author: "Manuel Vivo"
    date: "Wed, 10 Aug 2022 17:01:35 GMT"
---

# Consuming flows safely in Jetpack Compose

The article explains the recommended way to collect flows in Android apps using Jetpack Compose: the `collectAsStateWithLifecycle` API. This composable function collects values from a flow and represents the latest value as Compose `State` in a lifecycle-aware manner, using `Lifecycle.State.STARTED` by default to start and stop collection. This prevents unnecessary resource usage (e.g., network updates, database connections) when the app is in the background, aligning with Android's lifecycle rather than just the Composition's lifecycle.

`collectAsStateWithLifecycle` is built on top of `repeatOnLifecycle`, the recommended pattern for collecting flows in the View system, and saves boilerplate. It is contrasted with `collectAsState`, which follows the Composition lifecycle and continues collecting even when the Android lifecycle is in the background. The article argues that while `collectAsState` is platform-agnostic, Android apps should use the lifecycle-aware variant to enable the rest of the app hierarchy to free resources. It also notes that the UI should not know how the ViewModel produces state, and the ViewModel should use `.stateIn(WhileSubscribed())` to stop upstream flows when there are no collectors.

- Use `collectAsStateWithLifecycle` for collecting flows in Android Jetpack Compose apps to respect the Android lifecycle and save resources.
- By default, it stops collecting when the lifecycle falls below STARTED, using `repeatOnLifecycle` under the hood.
- `collectAsState` is platform-agnostic and does not stop collecting when the app goes to the background, so it is not recommended for Android.
- Pair `collectAsStateWithLifecycle` with `stateIn(WhileSubscribed())` in the ViewModel to free up upstream resources when no collectors are active.
- Migration to `collectAsStateWithLifecycle` is straightforward and recommended.