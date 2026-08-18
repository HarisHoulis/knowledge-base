---
domain: android-kotlin
subdomain: android-ui-layer
concept: state-holders-and-saved-state
title: Crash course on the Android UI layer | Part 2
sources:
  - title: "Crash course on the Android UI layer | Part 2"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-2-2335171467e0?source=rss-3b5622dd813c------2"
    author: "Manuel Vivo"
    date: "2023-12-19"
---

# Crash course on the Android UI layer | Part 2

The article also covers saving UI state: SavedState APIs preserve transient UI state across configuration changes and system-initiated process death, while persistent storage is reserved for application data that must survive unexpected app dismissals. Overall, the post provides decision trees to help developers manage state and logic effectively in the Android UI layer. (Source: Crash course on the Android UI layer | Part 2.)

- Business logic belongs in screen-level state holders (typically ViewModel); UI logic can be handled by the UI or plain state holder classes.
- ViewModel survives configuration changes and integrates with Jetpack Navigation and Hilt, but viewModelScope should be used carefully and not overused.
- Plain state holders (e.g., NiaAppState, DrawerState) are recommended for reusable UI components and can hold lifecycle-related references safely.
- State should be hoisted to the lowest common ancestor; hoist to a ViewModel only when business logic needs to read or write that state.
- Use SavedState APIs to survive process death and persistent storage for long-term app data that must outlast app dismissal.