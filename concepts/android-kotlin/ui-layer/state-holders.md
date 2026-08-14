---
domain: android-kotlin
subdomain: ui-layer
concept: state-holders
title: Crash course on the Android UI layer | Part 2
sources:
  - title: "Crash course on the Android UI layer | Part 2"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-2-2335171467e0"
    author: "Manuel Vivo"
    date: "Tue, 19 Dec 2023 15:58:45 GMT"
---

# Crash course on the Android UI layer | Part 2

This article continues a series on Android's UI layer, focusing on state holders and related best practices. It distinguishes between business logic (what to do with data) and UI logic (how to display it), recommending that business logic in the UI layer be handled by a screen-level state holder, typically an androidx.ViewModel. UI logic can stay in the UI if simple, or be delegated to a plain state holder class when complexity grows. The ViewModel is favored because it survives configuration changes, integrates with Jetpack libraries, and caches UI state for quick restoration. (Manuel Vivo, 2023)

- Business logic on the UI layer should be handled by a screen-level state holder, usually a ViewModel, to survive configuration changes and integrate with Navigation and Hilt.
- UI logic, such as adapting to screen size, can live in the UI or be delegated to a plain state holder class (e.g., NiaAppState, DrawerState) to keep the UI simple.
- Introduce a state holder when UI complexity grows; for reusable composables, creating a state holder enhances reusability and external control.
- State should be hoisted to the lowest common ancestor; if business logic reads or writes the state, it must be hoisted to the ViewModel.
- SavedState APIs preserve UI state across process death, while persistent storage is for application data that must survive app dismissal.