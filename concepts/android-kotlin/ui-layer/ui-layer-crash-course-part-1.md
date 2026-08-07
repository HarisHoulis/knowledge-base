---
domain: android-kotlin
subdomain: ui-layer
concept: ui-layer-crash-course-part-1
title: Crash course on the Android UI layer | Part 1
sources:
  - title: "Crash course on the Android UI layer | Part 1"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-1-2094221a9be3"
    author: "Manuel Vivo"
    date: "2023-12-13"
---

# Crash course on the Android UI layer | Part 1

The article by Manuel Vivo (2023) summarizes Android Developer guidance on the UI layer, outlining its core entities: UI, UI state, and state holders. It emphasizes separation of concerns, testability, and reusability, and introduces unidirectional data flow (UDF) where user events are handled by state holders, which expose streams of UI state for the UI to render. This guidance applies to both the View system and Jetpack Compose.

The article details UI state modeling and production. UI state describes the information displayed on screen and should be immutable to ensure consistency. Examples include a dice roll state held in a MutableStateFlow and a ViewModel mapping a user stream to a StateFlow via the stateIn operator. To avoid UI inconsistencies, complex states should use sealed interfaces, such as the HomeUiState example from Jetnews.

For observing UI state, the article recommends lifecycle-aware collection: repeatOnLifecycle for Android Views and collectAsStateWithLifecycle for Compose. It also discusses when to expose a single stream of UI state versus multiple streams, suggesting single streams when fields depend on each other and multiple streams when fields are independent.

- The UI layer consists of three entities: UI, UI state, and state holders, with unidirectional data flow ensuring predictable state updates.
- UI state should be modeled as immutable data classes or sealed interfaces to prevent UI inconsistencies and represent distinct screen states.
- Use StateFlow and stateIn to produce and expose UI state from state holders, isolating business logic and improving testability.
- Collect UI state lifecycle-aware using repeatOnLifecycle in Views and collectAsStateWithLifecycle in Compose.
- Expose a single UI state stream when fields are interdependent; multiple streams are acceptable for independent fields.