---
domain: android-kotlin
subdomain: ui-layer
concept: state-holders-and-state-saving
title: Crash course on the Android UI layer | Part 2
sources:
  - title: "Crash course on the Android UI layer | Part 2"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-2-2335171467e0"
    author: "Manuel Vivo"
    date: "2023-12-19"
---

# Crash course on the Android UI layer | Part 2

This article is the second part of a series summarising Android Developer guidance on the UI layer, focusing on state holders and saving UI state. It distinguishes between business logic, which dictates what to do with data, and UI logic, which determines how to display state changes. Business logic should be handled by a screen-level state holder, typically an androidx.ViewModel, while UI logic can remain in the UI or be delegated to a plain class state holder when complexity grows (Manuel Vivo, 2023).

- Business logic belongs in a screen-level ViewModel; UI logic can be in the UI or a plain state holder.
- ViewModel survives configuration changes and caches state, making it ideal for screen-level state.
- Introduce plain state holders when UI complexity grows, e.g., NiaAppState or DrawerState.
- Hoist state to the lowest common ancestor; if business logic needs it, hoist to ViewModel.
- SavedState APIs handle configuration changes and process death; persistent storage is for long-term data.