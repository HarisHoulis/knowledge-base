---
domain: android-kotlin
subdomain: ui-layer
concept: state-holders
title: Crash course on the Android UI layer | Part 2
sources:
  - title: "Crash course on the Android UI layer | Part 2"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-2-2335171467e0?source=rss-3b5622dd813c------2"
    author: "Manuel Vivo"
    date: "2023-12-19"
---

# Crash course on the Android UI layer | Part 2

This article is the second part of a series summarizing Android Developer guidance on the UI layer, focusing on state holders and state management. It distinguishes between business logic, which should be handled by a screen-level state holder extending androidx.ViewModel, and UI logic, which can be managed within the UI itself or delegated to a plain class state holder for complex components. The ViewModel is highlighted for its ability to survive configuration changes and integrate with Jetpack libraries like Navigation and Hilt, making it ideal for exposing screen UI state and handling business logic. Plain state holders, such as Compose's DrawerState or custom NiaAppState, are recommended for reusable UI components, and they can safely hold references to lifecycle-related APIs since they are scoped to the composition.

- Business logic on the UI layer should be handled by a screen-level state holder, typically extending androidx.ViewModel.
- UI logic can reside in the UI composable, but complex UI logic should be delegated to a plain class state holder.
- ViewModel survives configuration changes and integrates seamlessly with Jetpack Navigation and Hilt.
- State should be hoisted to the lowest common ancestor; if business logic requires the state, hoist it to the ViewModel.
- For persistence across process death, use SavedState APIs; for app data, use persistent storage.