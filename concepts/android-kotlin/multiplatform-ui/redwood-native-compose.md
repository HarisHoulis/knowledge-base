---
domain: android-kotlin
subdomain: multiplatform-ui
concept: redwood-native-compose
title: Native UI and multiplatform Compose with Redwood
sources:
  - title: "Native UI and multiplatform Compose with Redwood"
    url: "https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood"
    author: "Jake Wharton"
---

# Native UI and multiplatform Compose with Redwood

Redwood is Cash App's approach to multiplatform mobile UI, prioritizing native UI toolkits on each platform while leveraging Kotlin and Compose for state and tree management [1]. The article outlines four core values: using native UI for best quality, reusing existing components to maintain a single source of truth, employing a mobile language with strong tooling (Kotlin), and enabling incremental adoption in existing apps [1].

Redwood defines a common schema of UI widgets as data classes, from which it generates both a composable and an interface for each widget [1]. Each platform binds the interface to its native UI component, and developers write regular Compose code using the generated composables. This plumbing allows the native UI toolkit to be driven by multiplatform Compose logic [1].

Additionally, the Redwood repository includes Treehouse, a module using Zipline to dynamically update composable logic at runtime, enabling app updates between releases [1]. The article announces Redwood 0.5 as a beta release, emphasizing cross-version compatibility when using the Treehouse bridge [1].

- Renders using native UI toolkit per platform while using Compose for state/tree management
- Schema-defined widget data classes generate composables and interfaces for each platform
- Supports incremental adoption in existing apps
- Treehouse and Zipline enable dynamic runtime updates of UI logic
- Redwood 0.5 beta marks a milestone toward broader rollout