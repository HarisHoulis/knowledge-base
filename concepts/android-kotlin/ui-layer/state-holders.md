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

This article is the second part of a crash course on the Android UI layer, focusing on state holders and related topics. It distinguishes between business logic (product requirements for data) and UI logic (how to display state changes). Business logic in the UI layer should be handled by a screen-level state holder, typically an androidx.ViewModel, while UI logic can be managed within the UI itself or delegated to a plain class state holder when complexity grows (Vivo, 2023).

The ViewModel is recommended as a screen-level state holder because it survives configuration changes, providing a stable instance that caches UI state and continues executing business logic via viewModelScope. It also integrates with Jetpack libraries like Navigation and Hilt, making instance retention easier. However, ViewModel should not be overused; plain state holders are suitable for simpler UI logic and can safely hold references to Context or Resources because they are scoped to the Composition (Vivo, 2023).

State hoisting principles advise placing state in the lowest common ancestor that reads or writes it. If business logic needs the state, it should be hoisted to the screen-level ViewModel; otherwise, it belongs in the UI tree. To survive system-initiated process death, SavedState APIs are available, while persistent storage is for long-term data. The article provides practical guidance and decision trees for managing state and logic in the Android UI layer (Vivo, 2023).

- Business logic in the UI layer should be handled by a screen-level state holder, typically an androidx.ViewModel.
- UI logic can be kept in the UI or delegated to a plain class state holder when complexity grows.
- ViewModel survives configuration changes, caches UI state, and integrates with Jetpack libraries like Navigation and Hilt.
- State should be hoisted to the lowest common ancestor; if business logic requires it, hoist to the ViewModel.
- SavedState APIs preserve state across process death, while persistent storage is for long-term data.