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

This article, part 2 of a series, explores state holders and state management in the Android UI layer. It distinguishes between business logic (what to do with data) and UI logic (how to display data), noting that business logic should be handled at the screen level, typically by a ViewModel, while UI logic can be managed in the UI or delegated to plain state holder classes. ViewModels are ideal for screen-level state holders because they survive configuration changes, integrate with Jetpack libraries like Navigation and Hilt, and cache UI state. However, their power should be used judiciously, and plain state holders are recommended for complex UI components (source: Crash course on the Android UI layer | Part 2).

The article also discusses state hoisting principles, advising to place state in the lowest common ancestor that reads or writes it. If state is required by business logic, it should be hoisted to the screen-level ViewModel; otherwise, it can live in the UI tree. It additionally covers saving UI state: SavedState APIs handle configuration changes and system-initiated process death, while persistent storage is for application data. The overall guidance helps developers choose the right state holder implementation based on complexity and lifecycle needs (source: Crash course on the Android UI layer | Part 2).

- Business logic belongs in screen-level state holders (ViewModel), while simple UI logic can stay in the UI or be delegated to plain state holders.
- ViewModel survives configuration changes, integrates with Navigation and Hilt, and caches UI state, making it suitable for screen-level state holders.
- Plain state holders (e.g., NiaAppState, DrawerState) are recommended for reusable or complex UI components and can safely hold lifecycle-related references.
- Hoist state to the lowest common ancestor; if business logic requires it, hoist to the ViewModel.
- Use SavedState APIs for transient UI state across configuration and process death; use persistent storage for application data.