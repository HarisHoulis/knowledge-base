---
domain: android-kotlin
subdomain: ui-layer
concept: state-holders-and-hoisting
title: Crash course on the Android UI layer | Part 2
sources:
  - title: "Crash course on the Android UI layer | Part 2"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-2-2335171467e0"
    author: "Manuel Vivo"
    date: "2023-12-19"
---

# Crash course on the Android UI layer | Part 2

State holders simplify the UI by handling logic and exposing UI state. The article distinguishes business logic (what to do with data) from UI logic (how to display it), noting that business logic in the UI layer should be handled at the screen level, typically by a ViewModel, while UI logic can remain in the UI or be delegated to a plain state holder class [1]. ViewModel is recommended because it survives configuration changes, integrates with Jetpack Navigation and Hilt, and scopes business logic to a longer-lived object. Plain state holders are introduced when UI complexity grows, as demonstrated by Compose's DrawerState and Now in Android's NiaAppState [1]. State should be hoisted to the lowest common ancestor that reads or writes it; if business logic requires the state, it should be hoisted to the screen-level ViewModel. To survive process death, use SavedState APIs; for persistent data across app dismissals, use persistent storage [1].

- Business logic belongs in a screen-level ViewModel; UI logic can live in the UI or a plain state holder.
- ViewModel survives configuration changes and integrates with Navigation/Hilt, making it ideal for screen-level state.
- Introduce plain state holders as UI complexity grows; name them with the 'State' suffix in Compose.
- Hoist state to the lowest common ancestor that reads/writes it; if business logic needs it, hoist to the ViewModel.
- Use SavedState APIs for process-death survival and persistent storage for long-term data.