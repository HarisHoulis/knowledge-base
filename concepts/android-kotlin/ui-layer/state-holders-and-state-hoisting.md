---
domain: android-kotlin
subdomain: ui-layer
concept: state-holders-and-state-hoisting
title: Crash course on the Android UI layer | Part 2
sources:
  - title: "Crash course on the Android UI layer | Part 2"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-2-2335171467e0"
    author: "Manuel Vivo"
    date: "Tue, 19 Dec 2023 15:58:45 GMT"
---

# Crash course on the Android UI layer | Part 2

This article is the second part of a crash course on the Android UI layer, focusing on state holders and related best practices. It distinguishes between business logic (what to do with data) and UI logic (how to display data), recommending that business logic on the UI layer be handled by a screen-level state holder, typically an androidX.ViewModel, while simpler UI logic can be managed in the UI itself or delegated to a plain state holder class. The ViewModel is favored because it survives configuration changes, integrates with Jetpack Navigation and Hilt, and provides a ViewModel-scoped coroutine scope for long-running work. However, its power should not be abused; state should be hoisted to the lowest common ancestor and placed in a ViewModel only when required by business logic. For reusable UI components, plain state holder classes like DrawerState or NiaAppState can simplify the UI and provide external control. The article also covers saving UI state, explaining the differences between configuration-change survival, SavedState APIs for process death, and persistent storage for unexpected app dismissal.

- Business logic in the UI layer should be handled by a screen-level state holder, typically an androidX.ViewModel, because it survives configuration changes and integrates with other Jetpack libraries.
- UI logic (e.g., showing a bottom bar vs. navigation rail based on screen size) can be managed in the UI or delegated to a plain state holder class when it becomes complex.
- State should be hoisted to the lowest common ancestor that reads or writes it; it should be placed in a ViewModel only when business logic requires it.
- Plain state holder classes (e.g., DrawerState, NiaAppState) can hold lifecycle-related references safely because they are scoped to the UI/composition lifecycle.
- To survive process death, use SavedState APIs (Bundle) for transient UI state; use persistent storage for application data that must survive unexpected app dismissal.