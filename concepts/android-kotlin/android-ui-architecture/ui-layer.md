---
domain: android-kotlin
subdomain: android-ui-architecture
concept: ui-layer
title: Crash course on the Android UI layer | Part 1
sources:
  - title: "Crash course on the Android UI layer | Part 1"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-1-2094221a9be3?source=rss-3b5622dd813c------2"
    author: "Manuel Vivo"
    date: "2023-12-13"
---

# Crash course on the Android UI layer | Part 1

In this first part of the series, Manuel Vivo summarizes Android's official guidance on the UI layer, focusing on the UI and UI state. He explains that the UI layer consists of three entities—UI, UI state, and state holders—and that user events are processed by the state holder, resulting in UI state changes following Unidirectional Data Flow (UDF). The guidance applies to both the View system and Jetpack Compose (Vivo, 2023).

UI state describes the information to display and should be immutable. The article shows how to model UI state with data classes and sealed interfaces, using examples like DiceRollUiState and HomeUiState. For complex screens, sealed interfaces prevent impossible UI states by enforcing mutually exclusive variants—such as Loading vs. LogUserIn or NoPosts vs. HasPosts. State holders produce UI state from inputs such as events, local logic, or external streams from data sources, often using StateFlow combined with operators like .stateIn for asynchronous flows (Vivo, 2023).

State collection should be lifecycle-aware: use repeatOnLifecycle(STARTED) in Android Views and collectAsStateWithLifecycle() in Compose, so the UI only collects state while visible. The article also advises exposing a single stream of UI state when fields depend on each other, while independent fields can potentially be exposed as multiple streams. This summary captures only the topics from Part 1, with state holders and state saving covered in Part 2 (Vivo, 2023).

- The UI layer consists of UI, UI state, and state holders, with Unidirectional Data Flow governing interactions.
- UI state should be immutable and exposed as a read-only observable holder (e.g., StateFlow).
- Use sealed interfaces to model mutually exclusive UI states and prevent impossible combinations.
- Consume UI state lifecycle-aware: repeatOnLifecycle(STARTED) for Views and collectAsStateWithLifecycle() for Compose.
- When fields are interdependent, expose a single UI state stream; independent fields may use multiple streams.