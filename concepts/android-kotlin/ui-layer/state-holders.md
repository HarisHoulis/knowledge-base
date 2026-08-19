---
domain: android-kotlin
subdomain: ui-layer
concept: state-holders
title: Crash course on the Android UI layer | Part 2
sources:
  - title: "Crash course on the Android UI layer | Part 2"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-2-2335171467e0"
    author: "Manuel Vivo"
    date: "2023-12-19"
---

# Crash course on the Android UI layer | Part 2

This article continues the Android UI layer crash course by focusing on state holders and state management. It distinguishes between business logic (what to do with data) and UI logic (how to display it), noting that business logic on the UI layer should be handled at the screen level, typically by a ViewModel, while simple UI logic can live in the UI itself or be delegated to a plain state holder class. ViewModels are recommended for screen-level state holders because they survive configuration changes, integrate with Jetpack libraries like Navigation and Hilt, and provide a scoped coroutine context via viewModelScope.

- Business logic should be handled by a screen-level state holder, usually an androidx.ViewModel, to survive configuration changes and integrate with Jetpack libraries.
- UI logic can be kept in the composable if simple, but for complex UI, delegate to a plain class state holder (e.g., DrawerState, NiaAppState) that follows the UI lifecycle.
- State should be hoisted to the lowest common ancestor; if business logic needs it, place it in the ViewModel, otherwise keep it in the UI tree.
- SavedState APIs preserve state across configuration changes and process death, while persistent storage is for application data.