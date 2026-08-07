---
domain: android-kotlin
subdomain: jetpack-compose
concept: collect-as-state-with-lifecycle
title: Consuming flows safely in Jetpack Compose
sources:
  - title: "Consuming flows safely in Jetpack Compose"
    url: "https://medium.com/androiddevelopers/consuming-flows-safely-in-jetpack-compose-cde014d0d5a3"
    author: "Manuel Vivo"
    date: "2022-08-10"
---

# Consuming flows safely in Jetpack Compose

Manuel Vivo explains that the recommended way to collect flows in Android is in a lifecycle-aware manner, and for Jetpack Compose apps, this means using the `collectAsStateWithLifecycle` composable function (Vivo, 2022). This API collects values from a flow and represents the latest value as Compose `State`, updating on each emission. By default, it uses `Lifecycle.State.STARTED` to start and stop collecting, which can be customized via the `minActiveState` parameter. Under the hood, it uses the `repeatOnLifecycle` API, saving developers from boilerplate and ensuring resources are freed when the app is in the background.

- `collectAsStateWithLifecycle` is the recommended way to collect flows in Jetpack Compose for Android, as it respects the Android lifecycle and saves resources.
- The API defaults to collecting only when the lifecycle is at least STARTED, and can be configured via `minActiveState`.
- It is built on `repeatOnLifecycle`, reducing boilerplate compared to manual lifecycle-aware collection.
- `collectAsState` is platform-agnostic and follows the Composition lifecycle, while `collectAsStateWithLifecycle` is Android-specific and also respects the Android lifecycle.
- For a complete resource-saving architecture, ViewModels should produce UI state using `.stateIn(WhileSubscribed())` so upstream flows stop when there are no collectors.