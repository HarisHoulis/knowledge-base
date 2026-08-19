---
domain: android-kotlin
subdomain: kotlin-multiplatform
concept: redwood-multiplatform-compose
title: Native UI and multiplatform Compose with Redwood
sources:
  - title: "Native UI and multiplatform Compose with Redwood"
    url: "https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood"
    author: "Jake Wharton"
---

# Native UI and multiplatform Compose with Redwood

Redwood is Cash App's approach to multiplatform mobile UI, emphasizing native UI toolkits on each platform, reusing existing app components, leveraging Kotlin for its multi-platform capabilities, and enabling incremental adoption. As described in the article, these principles allow engineers to retain their skills and maintain a single source of truth for UI components (https://code.cash.app/native-ui-and-multiplatform-compose-with-redwood).

- Native UI is prioritized on each platform, allowing engineers to use platform-specific skills and maintain existing styles and controls.
- Kotlin is chosen for its ability to compile to Java bytecode, native (LLVM), and JavaScript, supporting Android, iOS, and web.
- A schema defines UI widgets, from which Redwood generates composables and interfaces; each platform binds the interface to its native UI component.
- Treehouse, powered by Zipline, enables dynamic updating of composable logic at runtime, improving development and allowing in-the-wild updates.
- Redwood 0.5 is released as 'beta', allowing breaking changes while maintaining compatibility across the Treehouse bridge for future versions.