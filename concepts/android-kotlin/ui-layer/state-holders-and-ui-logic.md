---
domain: android-kotlin
subdomain: ui-layer
concept: state-holders-and-ui-logic
title: Crash course on the Android UI layer | Part 2
sources:
  - title: "Crash course on the Android UI layer | Part 2"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-2-2335171467e0"
    author: "Manuel Vivo"
    date: "Tue, 19 Dec 2023 15:58:45 GMT"
---

# Crash course on the Android UI layer | Part 2

This article, the second part of Bumble's crash course on the Android UI layer, dives into state holders and where to hoist UI state. It distinguishes between business logic (what to do with data) and UI logic (how to display data), explaining that business logic should be handled at the screen level by a ViewModel while UI logic can live in the composable or be delegated to a plain state holder class. The author emphasizes that ViewModel survives configuration changes and integrates with Jetpack libraries, making it ideal for exposing screen UI state and running business logic (Manuel Vivo, Crash course on the Android UI layer | Part 2).

The article also discusses plain state holders for reusable or complex UI components, such as DrawerState or NiaAppState, and provides guidance on state hoisting: place state in the lowest common ancestor that reads or writes it, and if business logic requires the state, hoist it to the screen-level ViewModel. Finally, it touches on saving UI state across configuration changes and process death using SavedState APIs, and persistent storage for surviving unexpected app dismissals (Manuel Vivo, Crash course on the Android UI layer | Part 2).

- State holders simplify the UI by managing logic and exposing UI state; business logic belongs in a ViewModel, while UI logic can be handled by plain state holders.
- ViewModel survives configuration changes and integrates with Navigation and Hilt, making it the recommended implementation for screen-level state holders.
- Introduce a plain state holder when UI complexity grows, and use naming conventions ending in 'State' for Compose state holders.
- Hoist state to the lowest common ancestor that reads or writes it, and to the ViewModel if business logic needs it.
- To survive process death, use SavedState APIs for transient UI state and persistent storage for long-term application data.