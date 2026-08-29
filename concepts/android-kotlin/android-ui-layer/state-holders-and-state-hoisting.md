---
domain: android-kotlin
subdomain: android-ui-layer
concept: state-holders-and-state-hoisting
title: Crash course on the Android UI layer | Part 2
sources:
  - title: "Crash course on the Android UI layer | Part 2"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-2-2335171467e0?source=rss-3b5622dd813c------2"
    author: "Manuel Vivo"
    date: "2023-12-19"
---

# Crash course on the Android UI layer | Part 2

In this article, Manuel Vivo continues a crash course on the Android UI layer, focusing on how to manage state and logic within it. He distinguishes two types of logic: business logic, which implements product requirements and handles data creation/storage/modification, and UI logic, which determines how to display state changes. Business logic that lives in the UI layer should be handled at the screen level, typically by a ViewModel, while UI logic can remain in the UI or be delegated to a plain class state holder when complexity grows.

- Business logic in the UI layer should be scoped to the screen level, often via androidx.ViewModel, which survives configuration changes and integrates with Jetpack libraries.
- UI logic can be kept in the UI itself or delegated to plain state holder classes (e.g., DrawerState, NiaAppState) when the UI becomes complex; in Compose, these are named with a State suffix.
- State should be hoisted to the lowest common ancestor; if business logic requires it, hoist to a screen-level ViewModel, otherwise keep it in the appropriate UI node.
- SavedState APIs allow UI state to survive both configuration changes and system-initiated process death, while persistent storage is needed for long-term data.
- viewModelScope should be used carefully; not all logic belongs in a ViewModel, and plain state holders can hold lifecycle-related references safely when scoped to the Composition.