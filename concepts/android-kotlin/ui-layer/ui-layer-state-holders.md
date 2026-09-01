---
domain: android-kotlin
subdomain: ui-layer
concept: ui-layer-state-holders
title: Crash course on the Android UI layer | Part 2
sources:
  - title: "Crash course on the Android UI layer | Part 2"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-2-2335171467e0?source=rss-3b5622dd813c------2"
    author: "Manuel Vivo"
    date: "Tue, 19 Dec 2023 15:58:45 GMT"
---

# Crash course on the Android UI layer | Part 2

This article continues a crash course on the Android UI layer, focusing on state holders and related best practices. It distinguishes between business logic (what to do with data) and UI logic (how to display state), noting that business logic on the UI layer should be handled at the screen level by a state holder that extends `androidx.ViewModel`, while simple UI logic can live in the UI itself or be delegated to a plain class state holder when it becomes complex. [1] The ViewModel is recommended for screen-level state because it survives configuration changes, caches screen UI state, and integrates with Jetpack libraries like Navigation and Hilt. However, it should not be overused; plain state holders are appropriate for UI-specific state and can hold context references without leaking because they follow the UI lifecycle. [1]

The article also explains state hoisting: state should be placed in the lowest common ancestor that reads or writes it, and if the state is required by business logic, it should be hoisted to the screen-level ViewModel. It introduces `SavedState` APIs to survive system-initiated process death, and persistent storage for data that must survive unexpected app dismissal. The key takeaway is to choose state holder types based on the type of logic and lifecycle requirements, and to simplify the UI by introducing state holders as complexity grows. [1]

- Business logic on the UI layer should be managed by a screen-level state holder (typically an `androidx.ViewModel`), while UI logic can be in the UI or a plain state holder.
- ViewModel survives configuration changes and integrates with Jetpack Navigation and Hilt, making it ideal for exposing screen UI state and handling business logic.
- Introduce a plain state holder for UI components when they grow in complexity; these can safely hold references to lifecycle-related APIs because they are scoped to the UI lifecycle.
- Hoist state in the lowest common ancestor composable; use a ViewModel if business logic requires reading or writing that state.
- For preserving state beyond configuration changes, use SavedState APIs for process death and persistent storage for data that must survive unexpected app dismissal.