---
domain: android-kotlin
subdomain: multiplatform-ui
concept: redwood-compose
title: Native UI and multiplatform Compose with Redwood
sources:
  - title: "Native UI and multiplatform Compose with Redwood"
    url: "https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood"
    author: "Jake Wharton"
---

# Native UI and multiplatform Compose with Redwood

Redwood is Cash App's approach to multiplatform mobile UI, prioritizing native UI toolkits per platform while reusing existing components and leveraging Kotlin for cross-platform execution. It combines Compose for state management and UI node creation with a custom tree that interfaces with each platform's native toolkit, requiring a common schema of UI widget definitions. From this schema, Redwood generates both a composable and a widget interface, which each platform binds to its native UI implementation. This allows engineers to write regular Compose code that renders using native controls on Android, iOS, and web, enabling incremental adoption in existing apps without forcing an all-or-nothing migration. (source: https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood)

- Redwood renders using each platform's native UI toolkit, not a cross-platform drawing layer.
- Compose is used for state management and UI tree structure, but with a custom tree rather than Compose UI.
- Widget schemas in Kotlin generate composables and interfaces that each platform binds to native components.
- Treehouse integrates with Zipline to allow dynamic updates of composable logic at runtime.
- Redwood 0.5 beta is now released, allowing incremental adoption and backward-compatible updates via Treehouse.