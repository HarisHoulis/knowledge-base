---
domain: android-kotlin
subdomain: ui-layer
concept: ui-state-holders
title: Crash course on the Android UI layer | Part 2
sources:
  - title: "Crash course on the Android UI layer | Part 2"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-2-2335171467e0?source=rss-3b5622dd813c------2"
    author: "Manuel Vivo"
    date: "2023-12-19"
---

# Crash course on the Android UI layer | Part 2

Part 2 of the crash course on the Android UI layer focuses on state holders and related topics like state hoisting and saving UI state. State holders simplify the UI by handling logic and exposing UI state. The article distinguishes between business logic (what to do with data) and UI logic (how to display data). Business logic should be handled by a screen-level state holder, typically an AndroidX ViewModel, while UI logic can be managed within the UI or a plain class state holder if complexity grows. (Manuel Vivo, 2023)

ViewModel is recommended as the screen-level state holder because it survives configuration changes, caches UI state, and integrates with Jetpack libraries like Navigation and Hilt. However, its power should not be abused; viewModelScope should be used carefully. If configuration changes matter, ViewModel is a good fit, otherwise a plain state holder may suffice. (Manuel Vivo, 2023)

State holders should be introduced when the UI grows complex, and plain state holders can hold lifecycle-related references without leaking memory, as they are scoped to the Composition. State hoisting should place state in the lowest common ancestor that reads or writes it. If state is required by business logic, it should be hoisted to the screen-level ViewModel; otherwise, it can stay in the UI tree. Examples include Compose's DrawerState and Now in Android's NiaAppState. (Manuel Vivo, 2023)

Finally, the article discusses saving UI state: SavedState APIs preserve transient UI state across configuration changes and system-initiated process death, while persistent storage is needed for app data that must survive unexpected dismissals. The article concludes that understanding these tools helps deliver a great user experience. (Manuel Vivo, 2023)

- Business logic belongs in a screen-level state holder, typically AndroidX ViewModel; UI logic can be in the UI or a plain state holder.
- ViewModel survives configuration changes and integrates with Navigation/Hilt, but viewModelScope should be used cautiously.
- Introduce state holders when UI complexity grows; plain state holders are scoped to the Composition and can safely hold Context/Resources.
- Hoist state to the lowest common ancestor; if business logic needs it, hoist to the ViewModel.
- SavedState APIs handle transient UI state across process death; persistent storage is for app data that must survive unexpected termination.