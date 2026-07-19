---
domain: android-kotlin
subdomain: Android UI architecture
concept: state-holders-ui-logic
title: Crash course on the Android UI layer | Part 2
sources:
  - title: "Crash course on the Android UI layer | Part 2"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-2-2335171467e0"
    author: "Manuel Vivo"
    date: "Tue, 19 Dec 2023 15:58:45 GMT"
---

# Crash course on the Android UI layer | Part 2

This article focuses on state holders in the Android UI layer, explaining how to effectively manage state and logic. It distinguishes between business logic (what to do with data) and UI logic (how to display state changes). Business logic should be handled by screen-level state holders, typically extending androidX.ViewModel, because ViewModel survives configuration changes and integrates with Jetpack libraries like Navigation and Hilt. UI logic, on the other hand, can be delegated to plain state holder classes when the UI becomes complex, allowing for cleaner component reuse. The article emphasizes that state should be hoisted to the lowest common ancestor that reads or writes it, and if business logic is involved, it belongs in a ViewModel. It also covers best practices for using ViewModel, such as avoiding over-scoping and considering configuration changes.

- Business logic on the UI layer is best handled by screen-level state holders (androidX.ViewModel) because they survive configuration changes and provide a longer lifetime than the UI itself.
- UI logic (e.g., navigation decisions based on screen size) can be delegated to plain state holder classes without extending ViewModel, improving UI reusability and testability.
- State should be hoisted to the lowest common ancestor that reads or writes it; if business logic is needed, hoist it to a ViewModel.
- ViewModel is recommended for exposing screen UI state and handling business logic due to its scoping, cached state, and seamless integration with Jetpack Navigation and Hilt.