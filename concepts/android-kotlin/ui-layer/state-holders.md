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

This article explores state holders in the Android UI layer, distinguishing between business logic (what to do with data) and UI logic (how to display it). Business logic should be handled by a screen-level state holder, typically an androidx.ViewModel, because it survives configuration changes and integrates with Jetpack libraries. UI logic can live in the composable itself when simple, or be delegated to a plain class state holder when complexity grows (Manuel Vivo, Medium).

The ViewModel is recommended for screen-level state because it survives configuration changes, caches UI state, and continues executing business logic via viewModelScope. It also integrates with Jetpack Navigation and Hilt. However, its scope should not be abused; introduce a state holder only when the UI grows complex, as demonstrated by DrawerState and NiaAppState. Plain state holders follow the UI lifecycle and can hold references to Context or Resources, but business logic should be injected (Manuel Vivo, Medium).

State hoisting should place state in the lowest common ancestor that reads or writes it. If business logic requires the state, it should be hoisted to the screen-level ViewModel; otherwise it stays in the UI tree. For persistence, SavedState APIs handle configuration changes and system-initiated process death, while persistent storage is needed for unexpected app dismissals (Manuel Vivo, Medium).

- Business logic on the UI layer belongs in a screen-level ViewModel; UI logic can be handled by the UI or a plain state holder.
- ViewModel survives configuration changes and integrates with Navigation and Hilt, making it ideal for exposing UI state.
- Introduce plain state holders (e.g., NiaAppState) when UI complexity grows; they are scoped to the UI lifecycle.
- Hoist state to the lowest common ancestor; if business logic needs it, hoist to the ViewModel.
- Use SavedState APIs for process death and persistent storage for unexpected app dismissal.