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

This article is the second part of a crash course on the Android UI layer, focusing on state holders and related best practices. State holders simplify the UI by handling logic and/or exposing UI state (Vivo, 2023). The author distinguishes between business logic, which dictates what to do with data, and UI logic, which determines how to display state changes; these respond differently to configuration changes. Business logic on the UI layer should be handled at the screen level, typically by an androidx.ViewModel, because it survives configuration changes and integrates with Jetpack libraries like Navigation and Hilt (Vivo, 2023).

For UI logic, simple cases can remain within the UI composable, but complex logic should be delegated to plain class state holders, such as DrawerState or NiaAppState, which are scoped to the Composition and can safely hold references to lifecycle-related APIs (Vivo, 2023). The article also covers state hoisting principles: place state in the lowest common ancestor that reads or writes it, and hoist state to the ViewModel when business logic requires it. Finally, it mentions SavedState APIs to survive process death and persistent storage for long-term data (Vivo, 2023).

- State holders simplify the UI by managing logic and exposing state; business logic belongs in a screen-level ViewModel.
- UI logic can be delegated to plain class state holders when complexity grows, as demonstrated by DrawerState and NiaAppState.
- State should be hoisted to the lowest common ancestor, and to the ViewModel if business logic needs it.
- SavedState APIs handle process death, while persistent storage is for application data that must survive app termination.