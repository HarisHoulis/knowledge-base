---
domain: android-kotlin
subdomain: ui-layer-architecture
concept: state-holders-and-hoisting
title: Crash course on the Android UI layer | Part 2
sources:
  - title: "Crash course on the Android UI layer | Part 2"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-2-2335171467e0"
    author: "Manuel Vivo"
    date: "2023-12-19"
---

# Crash course on the Android UI layer | Part 2

This article, part 2 of a series, explains the roles of state holders in the Android UI layer. It distinguishes between business logic (what to do with data) and UI logic (how to display it), recommending that business logic be handled by screen-level state holders, typically an androidx ViewModel, while UI logic can be managed within the UI or delegated to plain state holder classes as complexity grows. The author emphasizes that ViewModels survive configuration changes, cache UI state, and integrate seamlessly with Jetpack libraries like Navigation and Hilt, making them ideal for exposing screen UI state and handling business logic (Vivo, 2023).

The article also covers state hoisting principles, advising that state should be placed in the lowest common ancestor that reads or writes it. If state is required by business logic, it should be hoisted to the screen-level ViewModel; otherwise, it can live in the UI tree. Examples from Compose and Now in Android illustrate plain state holders (e.g., DrawerState, NiaAppState) that manage UI logic and are scoped to the composition. Finally, the piece touches on state persistence: SavedState APIs handle configuration changes and system-initiated process death, while persistent storage is for long-term data (Vivo, 2023).

- Business logic should be handled at the screen level by a ViewModel-based state holder; UI logic can be delegated to plain state holders when the UI grows complex.
- ViewModel survives configuration changes and caches UI state, ensuring data is instantly available after rotation and during back-stack navigation.
- State should be hoisted to the lowest common ancestor; if business logic reads or writes it, hoist to the ViewModel, otherwise keep it in the UI tree.
- Plain state holders in Compose follow a naming convention ending in 'State' and can safely hold lifecycle-related references because they are scoped to the composition.
- For stronger state preservation, use SavedState APIs to survive process death and persistent storage for app data that must outlive unexpected dismissals.