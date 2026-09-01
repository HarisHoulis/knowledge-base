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

The article explains the role of state holders in the Android UI layer, simplifying the UI by handling logic and exposing state. It distinguishes between business logic, which dictates what to do with data and should be handled at the screen level by a ViewModel, and UI logic, which determines how to display state changes and can be managed in the UI itself or delegated to a plain state holder when complexity grows (Vivo, 2023).

ViewModel is highlighted as the recommended screen-level state holder because it survives configuration changes, integrates with Jetpack Navigation and Hilt, and provides a viewModelScope for coroutines. However, the article cautions against overusing viewModelScope and notes that ViewModel should be used only when its benefits apply. For simpler UI, a plain class with remember may suffice; for complex or reusable components, a dedicated state holder like DrawerState or NiaAppState is advisable (Vivo, 2023).

State hoisting principles are discussed: state should be placed in the lowest common ancestor that reads or writes it, and if business logic needs it, hoist it to the screen-level ViewModel. To survive configuration changes and system-initiated process death, the article recommends using SavedState APIs, while persistent storage is reserved for application data (Vivo, 2023).

- State holders simplify the UI by managing state and logic; business logic belongs in a screen-level ViewModel, UI logic can be in the UI or a plain state holder.
- ViewModel survives configuration changes and integrates with Navigation and Hilt, but avoid abusing viewModelScope.
- Introduce a state holder when UI complexity grows, and follow the naming convention ending in 'State' for Compose state holders.
- Hoist state to the lowest common ancestor; hoist to ViewModel if business logic needs to read or write it.
- Use SavedState APIs to survive process death, and persistent storage for durable application data.