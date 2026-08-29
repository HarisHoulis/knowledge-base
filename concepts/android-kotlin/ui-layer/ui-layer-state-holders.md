---
domain: android-kotlin
subdomain: ui-layer
concept: ui-layer-state-holders
title: Crash course on the Android UI layer | Part 2
sources:
  - title: "Crash course on the Android UI layer | Part 2"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-2-2335171467e0"
    author: "Manuel Vivo"
    date: "2023-12-19"
---

# Crash course on the Android UI layer | Part 2

This article, part 2 of a series by Manuel Vivo, dives into state holders in the Android UI layer. It distinguishes between business logic (what to do with data) and UI logic (how to display state changes). Business logic on the UI layer should be handled at the screen level by a state holder typically extending androidx.ViewModel, while simpler UI logic can live in the composable itself, and complex UI logic can be delegated to a plain class state holder. ViewModels are recommended because they survive configuration changes, integrate with Jetpack Navigation and Hilt, and provide a stable scope for coroutines (viewModelScope). However, they should be used judiciously, and the article shares best practices for avoiding common pitfalls (source: https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-2-2335171467e0).

- State holders simplify the UI by managing logic; business logic belongs in a screen-level ViewModel, while UI logic can stay in the UI or be delegated to a plain state holder.
- ViewModel survives configuration changes, integrates with Navigation and Hilt, and provides a scoped coroutine context, but should not be overused.
- Introduce plain state holders when UI complexity grows or for reusable components; they can safely hold UI lifecycle-bound references.
- Hoist state to the lowest common ancestor, or to the ViewModel if business logic needs it.
- Use SavedState APIs to survive process death and persistent storage for long-lived data; the choice depends on how transient and critical the state is.