---
domain: android-kotlin
subdomain: android-ui-layer
concept: ui-layer-state-holders
title: Crash course on the Android UI layer | Part 2
sources:
  - title: "Crash course on the Android UI layer | Part 2"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-2-2335171467e0"
    author: "Manuel Vivo"
    date: "2023-12-19"
---

# Crash course on the Android UI layer | Part 2

The article explores the Android UI layer's state holders, distinguishing between business logic and UI logic. Business logic dictates what to do with data, while UI logic determines how to display it. Business logic on the UI layer should be handled by screen-level state holders (androidx.ViewModel), while UI logic can be managed within the UI itself or delegated to plain state holder classes when complexity grows (Manuel Vivo, 2023).

androidx.ViewModel is recommended for screen-level state holders because it survives configuration changes, integrates with Jetpack libraries like Navigation and Hilt, and caches screen UI state. However, developers should be cautious with viewModelScope and follow best practices. For UI complexity, plain state holder classes (e.g., DrawerState, NiaAppState) should be introduced; they can hold lifecycle-related references and are scoped to the Composition. Naming convention for Compose state holders is to end with 'State' (Manuel Vivo, 2023).

State hoisting should place state in the lowest common ancestor. If state is required by business logic, it should be hoisted to the ViewModel; otherwise, it can stay in the UI tree. To survive process death, Android provides SavedState APIs for transient state and persistent storage for longer-term data (Manuel Vivo, 2023).

- Business logic on the UI layer should be in a screen-level state holder (ViewModel); UI logic can be in the UI or a plain state holder.
- ViewModel survives configuration changes and integrates with Jetpack Navigation and Hilt, but viewModelScope must be used carefully.
- Introduce plain state holders when UI complexity grows; in Compose, name them with 'State' suffix.
- Hoist state to the lowest common ancestor; if business logic needs state, place it in the ViewModel.
- Use SavedState APIs for state across system-initiated process death, and persistent storage for data that must survive unexpected app dismissal.