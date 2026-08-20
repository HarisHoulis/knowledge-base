---
domain: android-kotlin
subdomain: ui-layer
concept: ui-layer-state-holders
title: Crash course on the Android UI layer | Part 2
sources:
  - title: "Crash course on the Android UI layer | Part 2"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-2-2335171467e0"
    author: "Manuel Vivo"
    date: "Tue, 19 Dec 2023 15:58:45 GMT"
---

# Crash course on the Android UI layer | Part 2

This article explores the Android UI layer, focusing on state holders and related best practices. It distinguishes between business logic (what to do with data) and UI logic (how to display state changes), noting that business logic on the UI layer should be handled at the screen level, typically by an androidx.ViewModel, while UI logic can reside in the UI itself or be delegated to a plain state holder class when complexity grows. State holders simplify the UI by encapsulating logic and exposing UI state, with the ViewModel surviving configuration changes and integrating with Jetpack libraries like Navigation and Hilt (Manuel Vivo).

The article provides guidance on where to hoist state in Compose, recommending that state be placed in the lowest common ancestor that reads or writes it. If business logic requires the state, it should be hoisted in the screen-level state holder; otherwise, it can live in the UI tree. Plain state holder classes, such as NiaAppState or DrawerState, are useful for reusable UI components and can hold lifecycle-related references safely. Finally, the article discusses saving UI state: ViewModels handle configuration changes, SavedState APIs additionally survive system-initiated process death, and persistent storage is reserved for application data that must survive unexpected app dismissal (Manuel Vivo).

- Business logic in the UI layer belongs at the screen level, typically in a ViewModel; UI logic can be managed in the UI or a plain class state holder.
- ViewModel survives configuration changes and integrates with Navigation and Hilt, making it ideal for exposing screen UI state and handling business logic.
- Introduce state holders when UI complexity grows; plain state holders can be scoped to the Composition and safely hold Resources/Context.
- Hoist state in the lowest common ancestor; hoist to ViewModel only when required by business logic.
- For state persistence: ViewModel handles configuration changes, SavedState APIs handle process death, persistent storage handles app dismissal.