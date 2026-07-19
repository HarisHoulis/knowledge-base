---
domain: android-kotlin
subdomain: ui-layer
concept: ui-layer-architecture
title: Crash course on the Android UI layer | Part 1
sources:
  - title: "Crash course on the Android UI layer | Part 1"
    url: "https://medium.com/bumble-tech/crash-course-on-the-android-ui-layer-part-1-2094221a9be3?source=rss-3b5622dd813c------2"
    author: "Manuel Vivo"
    date: "Wed, 13 Dec 2023 17:03:40 GMT"
---

# Crash course on the Android UI layer | Part 1

This article, part 1 of a series, summarizes Android's official guidance on the UI layer architecture. It defines three distinct entities in the UI layer: the UI (visual representation), UI state (immutable data describing what to display), and state holders (entities that manage state, process events, and expose observable streams of UI state). The core principle is Unidirectional Data Flow (UDF): state holders produce UI state from inputs (events, local/external sources) and expose it via observable data holders like StateFlow. The UI observes this state lifecycle-aware (e.g., using repeatOnLifecycle or collectAsStateWithLifecycle) and renders accordingly. Modeling UI state should avoid inconsistencies by using sealed interfaces or data classes with immutability. For example, a dice roll screen uses a MutableStateFlow inside a state holder, while combining flows from repositories uses .stateIn. The article emphasizes exposing a single stream when fields are dependent to prevent inconsistencies.

- The UI layer consists of UI, UI state, and state holders, with clear separation of concerns.
- Unidirectional Data Flow (UDF) ensures state flows in one direction: state holders produce state, UI consumes and sends events.
- UI state should be immutable, modeled with data classes and sealed interfaces to prevent invalid states.
- Observing UI state should be lifecycle-aware using repeatOnLifecycle (Views) or collectAsStateWithLifecycle (Compose).
- State holders process events, combine multiple sources, and expose a single or multiple streams depending on field independence.