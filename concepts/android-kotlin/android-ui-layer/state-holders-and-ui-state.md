---
domain: android-kotlin
subdomain: android-ui-layer
concept: state-holders-and-ui-state
title: Crash Course on the Android UI Layer Part 2: State Holders and UI State
sources:
  - title: "Crash course on the Android UI layer | Part 2"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-2-2335171467e0"
    author: "Manuel Vivo"
    date: "Tue, 19 Dec 2023"
---

# Crash Course on the Android UI Layer Part 2: State Holders and UI State

According to the article by Manuel Vivo (2023), the Android UI layer organizes logic into business logic and UI logic. Business logic, which implements product requirements, should be handled by a screen-level state holder—normally an androidx.ViewModel—to survive configuration changes and integrate with Jetpack libraries. UI logic, which dictates how state changes are displayed, can remain in the UI for simple cases or be delegated to a plain state holder class when complexity grows.

Vivo explains that ViewModels are scoped to Activity, Fragment, or Navigation destinations, so the same instance persists across configuration changes and data remains instantly available when navigating the back stack. However, plain state holders are scoped to the Composition and follow the UI lifecycle, allowing safe references to Context or Resources. The article recommends introducing a state holder when the UI starts growing in complexity and naming it with the `State` suffix in Compose.

Regarding state placement, Vivo advises placing state in the lowest common ancestor that reads or writes it. If the state is required by business logic, it should be hoisted in the screen-level ViewModel; otherwise it belongs in the appropriate node of the UI tree. The article also distinguishes between SavedState APIs, which preserve state through configuration changes and system-initiated process death, and persistent storage for surviving unexpected app dismissals.

- Business logic on the UI layer should be handled by a screen-level state holder, typically an androidx.ViewModel, because it survives configuration changes and integrates with Jetpack Navigation and Hilt.
- UI logic can be managed in the UI for simple cases, but a plain state holder class (named with a `State` suffix in Compose) should be introduced when the UI grows in complexity.
- State should be hoisted to the lowest common ancestor that reads or writes it; state required by business logic must be hoisted in the screen-level ViewModel.
- SavedState APIs preserve UI state across configuration changes and system-initiated process death, while persistent storage is needed to survive unexpected app dismissals.