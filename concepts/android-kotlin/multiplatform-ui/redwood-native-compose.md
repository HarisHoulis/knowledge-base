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

Redwood is Cash App's approach to multiplatform mobile UI that emphasizes rendering with native UI toolkits on each platform. As stated in the article, the core values are using native UI, reusing existing components, leveraging Kotlin's tooling, and allowing incremental adoption. This differentiates Redwood from cross-platform frameworks that rely on custom-drawn UI, ensuring engineers can utilize platform-specific skills and styles.

- Redwood renders using each platform's native UI toolkit, preserving native look and feel.
- It leverages Kotlin and Compose to provide a familiar development experience and shared state management.
- A schema definition generates composables and interfaces, with platform-specific bindings to native widgets.
- Redwood supports incremental adoption and includes Treehouse for runtime updates using Zipline.
- Redwood 0.5 is released as a beta, allowing future versions to remain compatible with older apps through the Treehouse bridge.