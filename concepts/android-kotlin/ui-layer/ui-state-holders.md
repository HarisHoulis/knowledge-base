---
domain: android-kotlin
subdomain: ui-layer
concept: ui-state-holders
title: Crash course on the Android UI layer | Part 2
sources:
  - title: "Crash course on the Android UI layer | Part 2"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-2-2335171467e0"
    author: "Manuel Vivo"
    date: "2023-12-19"
---

# Crash course on the Android UI layer | Part 2

This article is the second part of a crash course on the Android UI layer, focusing on state holders and state management. It distinguishes between business logic (what to do with data) and UI logic (how to display data), noting that business logic should be handled by screen-level state holders, typically androidX.ViewModel, while UI logic can be managed by plain state holder classes when complexity grows. The ViewModel is recommended because it survives configuration changes, integrates with Jetpack libraries, and scopes coroutines appropriately, but it should not be overused.

- Business logic on the UI layer should be handled close to the screen, usually by a screen-level state holder extending androidX.ViewModel.
- UI logic, which depends on configuration, can be managed in the UI itself, but should be delegated to a plain state holder class when it becomes complex.
- State should be hoisted to the lowest common ancestor that reads or writes it; if needed by business logic, it should be in the screen-level ViewModel.
- Plain state holders in Compose should be named with a 'State' suffix (e.g., NiaAppState, DrawerState) and can safely hold references to lifecycle-related APIs within the composition.
- To survive configuration changes and system-initiated process death, use Saved State APIs; use persistent storage for application data.