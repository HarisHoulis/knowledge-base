---
domain: android-kotlin
subdomain: multiplatform-ui
concept: redwood
title: Native UI and multiplatform Compose with Redwood
sources:
  - title: "Native UI and multiplatform Compose with Redwood"
    url: "https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood"
    author: "Jake Wharton"
---

# Native UI and multiplatform Compose with Redwood

Redwood is Cash App's approach to multiplatform mobile UI, prioritizing native UI toolkits on each platform, reusing existing app components, leveraging Kotlin for its multi-platform capabilities, and allowing incremental adoption. Unlike cross-platform rendering solutions, Redwood renders through the native UI toolkit on each platform, ensuring engineers can apply their platform-specific skills and styles.

- Renders with native UI toolkits on each platform while sharing Compose-based logic.
- Defines a schema of widgets that generates composables and platform interfaces.
- Designed for incremental adoption in existing apps via a library, not a full framework.
- Treehouse module uses Zipline for dynamic runtime updates of composable logic.
- Redwood 0.5 is now in beta, with cross-version compatibility for the Treehouse bridge.